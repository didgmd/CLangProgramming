"""Content and C-layout checks shared by the question-bank validator."""

from __future__ import annotations

import re


class QualityError(RuntimeError):
    """Raised when a student-facing question is incomplete or poorly formatted."""


def question_body(text: str) -> str:
    match = re.search(r"(?s)## 题目\s*\n(.*?)(?=\n## 常见失分点)", text)
    if not match:
        raise QualityError("missing question body")
    return match.group(1).strip()


def c_blocks(text: str) -> list[str]:
    return [match.strip() for match in re.findall(r"(?s)```c\s*\n(.*?)```", text)]


def strip_literals(line: str) -> str:
    line = re.sub(r'"(?:\\.|[^"\\])*"', '""', line)
    line = re.sub(r"'(?:\\.|[^'\\])*'", "''", line)
    line = re.sub(r"/\*.*?\*/|//.*", "", line)
    return line


def validate_c_layout(question_id: str, code: str) -> None:
    if "\t" in code:
        raise QualityError(f"{question_id}: C code contains a tab")
    lines = code.splitlines()
    if len(lines) == 1 and "{" in code and re.search(r"\w+\s*\([^)]*\)", code):
        raise QualityError(f"{question_id}: complete C function is on one line")
    depth = 0
    for number, line in enumerate(lines, 1):
        clean = strip_literals(line)
        if len(line) > 100 and not line.lstrip().startswith("#") and '"' not in line:
            raise QualityError(f"{question_id}: C line {number} exceeds 100 characters")
        stripped = line.strip()
        expected_depth = max(0, depth - (1 if stripped.startswith("}") else 0))
        if stripped and not stripped.startswith("#"):
            actual_spaces = len(line) - len(line.lstrip(" "))
            if actual_spaces % 4:
                raise QualityError(
                    f"{question_id}: C line {number} is not indented by 4-space units"
                )
            if actual_spaces // 4 != expected_depth:
                raise QualityError(
                    f"{question_id}: C line {number} has inconsistent indentation"
                )
        # A for-header may contain two semicolons; other lines may contain one
        # ordinary statement only.
        semicolons = clean.count(";")
        if semicolons > 1 and not re.search(r"\bfor\s*\(|;\s*\w+\+\+\)", clean):
            raise QualityError(
                f"{question_id}: C line {number} stacks ordinary statements"
            )
        depth += clean.count("{") - clean.count("}")
        if depth < 0:
            raise QualityError(f"{question_id}: C braces close out of order")
    if depth != 0:
        raise QualityError(f"{question_id}: C braces are unbalanced")


def validate_category(question_id: str, category: str, text: str) -> None:
    body = question_body(text)
    blocks = c_blocks(text)
    for code in blocks:
        validate_c_layout(question_id, code)

    if category == "选择题":
        if not re.search(r"(?s)\bA\..*\bB\..*\bC\..*\bD\.", body):
            raise QualityError(f"{question_id}: selection question lacks A-D options")
        if not re.search(r"\*\*答案：[A-D]。?\*\*", text):
            raise QualityError(f"{question_id}: selection answer is incomplete")
    elif category == "判断题":
        if len(body) < 25:
            raise QualityError(f"{question_id}: true/false proposition is incomplete")
        if not re.search(r"\*\*答案：(正确|错误)。?\*\*", text):
            raise QualityError(f"{question_id}: true/false answer is incomplete")
        if "**答案：错误。**" in text and "正确表述" not in text:
            raise QualityError(
                f"{question_id}: false proposition lacks a corrected statement"
            )
    elif category == "程序填空":
        blanks = sorted({int(item) for item in re.findall(r"〔(\d+)〕", body)})
        answers = sorted(
            {int(item) for item in re.findall(r"`〔(\d+)〕`：", text)}
        )
        if not blocks or not blanks or blanks != answers:
            raise QualityError(
                f"{question_id}: program blanks and numbered answers do not match"
            )
        if "### 完整参考程序" not in text:
            raise QualityError(f"{question_id}: restored program is missing")
        if not re.search(r"输入：|无输入", body) or not re.search(r"输出：|无标准输出", body):
            raise QualityError(f"{question_id}: input/output statement is missing")
    elif category == "读程序写结果":
        if not blocks:
            raise QualityError(f"{question_id}: trace question lacks its program")
        if "请写出程序运行后的精确输出" not in body:
            raise QualityError(f"{question_id}: exact-output request is missing")
        if not re.search(r"\*\*输出：\*\*", text):
            raise QualityError(f"{question_id}: exact output answer is missing")
    elif category == "编程题":
        required = (
            "### 输入格式",
            "### 输出格式",
            "### 数据范围与边界",
            "### 样例输入",
            "### 样例输出",
        )
        missing = [heading for heading in required if heading not in body]
        if missing:
            raise QualityError(
                f"{question_id}: programming statement lacks {', '.join(missing)}"
            )
        if "**正常与边界测试：**" not in text:
            raise QualityError(f"{question_id}: answer lacks concrete test data")
        if "### 完整参考程序" not in text:
            raise QualityError(f"{question_id}: reference program is missing")
