"""Strict C layout and fill-in consistency checks for program-bearing questions."""

from __future__ import annotations

import re


class ProgramQualityError(RuntimeError):
    """Raised when a C block violates the student-facing program contract."""


def code_blocks(text: str) -> list[tuple[str, str]]:
    marker = text.find("<!-- reference-c:start -->")
    blocks: list[tuple[str, str]] = []
    for match in re.finditer(r"(?s)```c\s*\n(.*?)```", text):
        role = "reference" if marker >= 0 and match.start() > marker else "question"
        blocks.append((role, match.group(1).strip()))
    return blocks


def strip_literals(line: str) -> str:
    line = re.sub(r'"(?:\\.|[^"\\])*"', '""', line)
    line = re.sub(r"'(?:\\.|[^'\\])*'", "''", line)
    return re.sub(r"/\*.*?\*/|//.*", "", line)


def control_headers(line: str) -> list[tuple[int, int]]:
    clean = strip_literals(line)
    headers: list[tuple[int, int]] = []
    for match in re.finditer(r"\b(?:if|for|while|switch)\s*\(", clean):
        start = clean.find("(", match.start())
        depth = 0
        for position in range(start, len(clean)):
            if clean[position] == "(":
                depth += 1
            elif clean[position] == ")":
                depth -= 1
                if depth == 0:
                    headers.append((match.start(), position))
                    break
    return headers


def semicolons_outside_parentheses(line: str) -> int:
    depth = 0
    count = 0
    for char in strip_literals(line):
        if char == "(":
            depth += 1
        elif char == ")":
            depth = max(0, depth - 1)
        elif char == ";" and depth == 0:
            count += 1
    return count


def validate_block(question_id: str, role: str, code: str) -> None:
    if "\t" in code:
        raise ProgramQualityError(f"{question_id}: C code contains a tab")
    lines = code.splitlines()
    depth = 0
    paren_depth = 0
    for number, line in enumerate(lines, 1):
        clean = strip_literals(line)
        stripped = clean.strip()
        if len(line) > 100 and not line.lstrip().startswith("#") and '"' not in line:
            raise ProgramQualityError(
                f"{question_id}: C line {number} exceeds 100 characters"
            )
        spaces = len(line) - len(line.lstrip(" "))
        if spaces % 4:
            raise ProgramQualityError(
                f"{question_id}: C line {number} is not indented by 4-space units"
            )
        expected = max(0, depth - (1 if stripped.startswith("}") else 0))
        if paren_depth and not stripped.startswith(")"):
            expected += 1
        actual = spaces // 4
        if role == "reference" and stripped and not stripped.startswith("#") and actual != expected:
            raise ProgramQualityError(
                f"{question_id}: C line {number} has inconsistent indentation"
            )
        if role == "question" and actual < expected:
            raise ProgramQualityError(
                f"{question_id}: C line {number} is under-indented"
            )
        if re.search(r"\b(?:if|for|while|switch)\(", clean):
            raise ProgramQualityError(
                f"{question_id}: C line {number} lacks control-keyword spacing"
            )
        if re.search(r"(?:[A-Za-z_]\w*|\])\s+\[", clean):
            raise ProgramQualityError(
                f"{question_id}: C line {number} has a space before a subscript"
            )
        headers = control_headers(line)
        if len(headers) > 1:
            raise ProgramQualityError(
                f"{question_id}: C line {number} stacks control statements"
            )
        if headers and clean[headers[0][1] + 1 :].strip():
            raise ProgramQualityError(
                f"{question_id}: C line {number} puts a control body on its header line"
            )
        is_else_if_header = (
            clean.lstrip().startswith("else if ")
            and len(headers) == 1
            and not clean[headers[0][1] + 1 :].strip()
        )
        if re.match(r"^\s*else\b.+", clean) and not is_else_if_header:
            raise ProgramQualityError(
                f"{question_id}: C line {number} puts an else body on the same line"
            )
        if semicolons_outside_parentheses(line) > 1:
            raise ProgramQualityError(
                f"{question_id}: C line {number} stacks ordinary statements"
            )
        depth += clean.count("{") - clean.count("}")
        paren_depth += clean.count("(") - clean.count(")")
        if depth < 0:
            raise ProgramQualityError(f"{question_id}: C braces close out of order")
    if depth:
        raise ProgramQualityError(f"{question_id}: C braces are unbalanced")
    if role == "reference":
        for number, line in enumerate(lines):
            stripped = strip_literals(line).strip()
            if not control_headers(line) and stripped != "else":
                continue
            following = next(
                (item.strip() for item in lines[number + 1 :] if item.strip()),
                "",
            )
            if following != "{":
                raise ProgramQualityError(
                    f"{question_id}: reference control at line {number + 1} lacks braces"
                )
        if re.search(r"(?m)=\s*\n\s*\{", code):
            raise ProgramQualityError(
                f"{question_id}: reference initializer is formatted like a control block"
            )
        if re.search(r"(?m)^(\s*)\}\s*\n\1;\s*$", code):
            raise ProgramQualityError(
                f"{question_id}: structure terminator must be written as '}};'"
            )


def c_tokens(code: str) -> list[str]:
    return re.findall(
        r'"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'|'
        r"//[^\n]*|/\*.*?\*/|"
        r"==|!=|<=|>=|\+\+|--|&&|\|\||\+=|-=|\*=|/=|%=|->|"
        r"[A-Za-z_]\w*|\d+(?:\.\d+)?(?:[eE][+-]?\d+)?|[^\s]",
        code,
        flags=re.S,
    )


def validate_filled_program(
    question_id: str,
    text: str,
    blocks: list[tuple[str, str]],
) -> None:
    question_code = next(code for role, code in blocks if role == "question")
    reference = next(code for role, code in blocks if role == "reference")
    answers = {
        number: answer
        for number, answer in re.findall(r"`〔(\d+)〕`：`([^`]*)`", text)
    }
    restored = re.sub(
        r"/\*〔(\d+)〕\*/",
        lambda match: answers.get(match.group(1), match.group(0)),
        question_code,
    )
    ignored = {"{", "}"}
    left = [token for token in c_tokens(restored) if token not in ignored]
    right = [token for token in c_tokens(reference) if token not in ignored]
    if left != right:
        raise ProgramQualityError(
            f"{question_id}: filled program differs from its complete reference"
        )


def validate_program_quality(
    question_id: str,
    category: str,
    text: str,
) -> None:
    if category not in {"程序填空", "读程序写结果", "编程题"}:
        return
    blocks = code_blocks(text)
    for role, code in blocks:
        validate_block(question_id, role, code)
    if category == "程序填空":
        validate_filled_program(question_id, text, blocks)
