"""Deterministic correctness fixes applied while migrating teaching examples.

These edits remove ordinary C defects without modernizing away textbook APIs
such as scanf() or the intentionally retained gets().
"""

from __future__ import annotations

import re


FORMAT_SPECIFIER = re.compile(
    r"%(?:[-+ #0]*)(?:\d+|\*)?(?:\.(?:\d+|\*))?"
    r"(?:hh|h|ll|l|j|z|t|L)?([diuoxXfFeEgGaAcspn%])"
)


def _split_arguments(text: str) -> list[str]:
    result = []
    start = 0
    depth = 0
    quote = None
    escaped = False
    for index, char in enumerate(text):
        if quote:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == quote:
                quote = None
            continue
        if char in {'"', "'"}:
            quote = char
        elif char in "([{":
            depth += 1
        elif char in ")]}":
            depth -= 1
        elif char == "," and depth == 0:
            result.append(text[start:index].strip())
            start = index + 1
    result.append(text[start:].strip())
    return result


def _fix_printf_pointer_line(line: str) -> str:
    if "printf" not in line or "%p" not in line:
        return line
    match = re.match(
        r'^(?P<indent>\s*)printf\s*\(\s*"(?P<fmt>(?:\\.|[^"])*)"\s*,'
        r'(?P<args>.*)\)\s*;\s*(?P<comment>//.*)?$',
        line,
    )
    if not match:
        return line
    specs = [item for item in FORMAT_SPECIFIER.findall(match.group("fmt")) if item != "%"]
    args = _split_arguments(match.group("args"))
    if len(specs) != len(args):
        return line
    for index, spec in enumerate(specs):
        if spec == "p" and not args[index].lstrip().startswith("(void *)"):
            args[index] = f"(void *)({args[index]})"
    comment = match.group("comment") or ""
    return (
        f'{match.group("indent")}printf("{match.group("fmt")}", '
        + ", ".join(args)
        + f");{comment}"
    )


def _fix_pointer_matrix_demo(text: str) -> str:
    lines = text.splitlines()
    seen = 0
    for index, line in enumerate(lines):
        if 'printf("%d,%d\\n"' not in line:
            continue
        seen += 1
        if seen <= 7:
            lines[index] = line.replace('printf("%d,%d\\n"', 'printf("%p,%p\\n"')
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def apply_source_fixes(text: str, source_rel: str) -> str:
    text = re.sub(r"\bscanf_s\s*\(", "scanf(", text)

    # Cast sizeof() to a format supported by both old MSVCRT and modern libc.
    lines = []
    for line in text.splitlines():
        if "printf" in line and "sizeof(" in line:
            line = line.replace("%d", "%lu")
            line = re.sub(
                r"(?<!\(unsigned long\))sizeof\(([^()]*)\)",
                r"(unsigned long)sizeof(\1)",
                line,
            )
        lines.append(line)
    text = "\n".join(lines) + ("\n" if text.endswith("\n") else "")

    text = text.replace(
        "if (c >= 'W' && c <= 'Z' || c >= 'w' && c <= 'z')",
        "if ((c >= 'W' && c <= 'Z') || (c >= 'w' && c <= 'z'))",
    )

    # Make two-dimensional and structure-array initializers explicit.
    text = re.sub(
        r"\{\s*1,\s*3,\s*5,\s*7,\s*9,\s*11,\s*13,\s*15,\s*17,\s*19,\s*21,\s*23\s*\}",
        "{{1, 3, 5, 7}, {9, 11, 13, 15}, {17, 19, 21, 23}}",
        text,
    )
    text = re.sub(
        r"\{\s*1,\s*2,\s*3,\s*4,\s*5,\s*6,\s*7,\s*8,\s*9,\s*10,\s*11,\s*12,"
        r"\s*13,\s*14,\s*15,\s*16,\s*17,\s*18,\s*19,\s*20\s*\}",
        "{{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, "
        "{11, 12, 13, 14, 15}, {16, 17, 18, 19, 20}}",
        text,
    )
    text = re.sub(
        r'\{\s*"Li",\s*0,\s*"Zhang",\s*0,\s*"Sun",\s*0\s*\}',
        '{{"Li", 0}, {"Zhang", 0}, {"Sun", 0}}',
        text,
    )

    if source_rel.endswith("11_Pointer/19_ex_8_11.c"):
        text = _fix_pointer_matrix_demo(text)
    if source_rel.endswith("11_Pointer/03_PointerOutput.c"):
        text = text.replace(
            'printf("指针形式 Pointer           0p%p\\n", *p);',
            'printf("指针形式 Pointer           %p\\n", (void *)p);',
        )

    text = "\n".join(_fix_printf_pointer_line(line) for line in text.splitlines())
    text += "\n"

    if source_rel.endswith("13_Structure/08_ex9_08.c"):
        text = text.replace('printf("%ld %5.1f\\n", p->num, p->score);',
                            'printf("%d %5.1f\\n", p->num, p->score);')
    if source_rel.endswith("13_Structure/09_ex9_09.c"):
        text = re.sub(r"\n};\s*$", "\n}\n", text)
    if source_rel.endswith("20241129/10.4.3.c"):
        text = text.replace("int main()\n{\n    int i;\n", "int main()\n{\n")
    if source_rel.endswith("09_Lab3/2048_Step3.c"):
        text = text.replace(
            "void updateGame(char direction) {",
            "void updateGame(char direction) {\n    (void)direction;",
        )
    if source_rel.endswith("01_HelloC/1_4_2_CalculatorFunction.c"):
        text = text.replace(
            "c = calculator(a, b, op);\n\n\treturn 0;",
            "c = calculator(a, b, op);\n\t(void)c;\n\n\treturn 0;",
        )
        text = text.replace(
            "c = calculator(a, b, op);\n\n    return 0;",
            "c = calculator(a, b, op);\n    (void)c;\n\n    return 0;",
        )

    return text.rstrip() + "\n"
