#!/usr/bin/env python3
"""Validate the eight student-facing lab task sheets and reference programs."""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

sys.dont_write_bytecode = True


ROOT = Path(__file__).resolve().parents[1]
LAB_ROOT = ROOT / "课件" / "上机"
PAGE_BREAK = '<div style="break-after: page; page-break-after: always;"></div>'
REPORT_NOTICE = (
    "实验报告提交：填写教师发放的实验报告模板，完成后保存为PDF格式并提交至超星学习通。"
)


class ValidationError(RuntimeError):
    """Raised when a lab task sheet violates the published contract."""


@dataclass(frozen=True)
class LabCase:
    stdin: str
    stdout: str
    expected_files: tuple[tuple[str, str], ...] = ()


@dataclass(frozen=True)
class LabSpec:
    lab_id: str
    directory: str
    question_id: str
    chapters: str
    project_name: str
    validation_filename: str
    required_code: tuple[str, ...]
    forbidden_code: tuple[str, ...]
    cases: tuple[LabCase, ...]


SPECS = (
    LabSpec(
        "CW-LAB01", "01-day-of-year", "QB-PG-005", "第1–4章", "日期序号计算", "day_of_year.c",
        ("switch", "case 11", "year % 400", "total = day"),
        ("[", "for (", "while (", "?", "invalid", "scanf(\"%d %d %d\", &year, &month, &day) !="),
        (
            LabCase("2024 2 29\n", "60\n"),
            LabCase("2023 3 1\n", "60\n"),
            LabCase("2024 1 1\n", "1\n"),
            LabCase("2023 12 31\n", "365\n"),
        ),
    ),
    LabSpec(
        "CW-LAB02", "02-character-count", "QB-PG-019", "第1–5章", "四类字符统计", "character_count.c",
        ("getchar()", "else if", "letters", "others"),
        ("fgets", "ctype.h", "char s[", "scanf("),
        (
            LabCase("Ab 3!\n", "2 1 1 1\n"),
            LabCase("\n", "0 0 0 0\n"),
            LabCase("12345\n", "0 5 0 0\n"),
            LabCase("   \n", "0 0 3 0\n"),
        ),
    ),
    LabSpec(
        "CW-LAB03", "03-word-count", "QB-PG-012", "第1–5章", "单词数量统计", "word_count.c",
        ("getchar()", "in_word", "'\\t'", "count++"),
        ("fgets", "string.h", "char s[", "scanf("),
        (
            LabCase("\n", "0\n"),
            LabCase("C\n", "1\n"),
            LabCase("C   language\n", "2\n"),
            LabCase("  C language  \n", "2\n"),
            LabCase("C language practice\n", "3\n"),
        ),
    ),
    LabSpec(
        "CW-LAB04", "04-matrix-transpose", "QB-PG-021", "第1–6章", "三阶矩阵转置", "matrix_transpose.c",
        ("[3][3]", "transpose[j][i] = matrix[i][j]"),
        ("fgets", "malloc", "scanf(\"%d\", &a[i][j]) !="),
        (
            LabCase("1 2 3 4 5 6 7 8 9\n", "1 4 7\n2 5 8\n3 6 9\n"),
            LabCase("1 2 3 2 4 5 3 5 6\n", "1 2 3\n2 4 5\n3 5 6\n"),
            LabCase("-1 -2 -3 -4 -5 -6 -7 -8 -9\n", "-1 -4 -7\n-2 -5 -8\n-3 -6 -9\n"),
        ),
    ),
    LabSpec(
        "CW-LAB05", "05-string-to-integer", "QB-PG-007", "第1–6章", "数字字符串转换", "string_to_integer.c",
        ("char s[64]", 'scanf("%63s", s)', "value = value * 10 + s[i] - '0'", "'\\0'"),
        ("limits.h", "overflow", "invalid", "scanf(\"%63s\", s) !="),
        (
            LabCase("-2048\n", "-2048\n"),
            LabCase("+17\n", "17\n"),
            LabCase("0012\n", "12\n"),
            LabCase("0\n", "0\n"),
        ),
    ),
    LabSpec(
        "CW-LAB06", "06-pascal-triangle", "QB-PG-020", "第1–6章", "杨辉三角", "pascal_triangle.c",
        ("a[10][10]", "a[i][0] = 1", "a[i][i] = 1", "a[i - 1][j - 1] + a[i - 1][j]"),
        ("malloc", "scanf(\"%d\", &n) !="),
        (
            LabCase("1\n", "1\n"),
            LabCase("4\n", "1\n1 1\n1 2 1\n1 3 3 1\n"),
            LabCase("7\n", "1\n1 1\n1 2 1\n1 3 3 1\n1 4 6 4 1\n1 5 10 10 5 1\n1 6 15 20 15 6 1\n"),
        ),
    ),
    LabSpec(
        "CW-LAB07", "07-scenic-sort", "QB-PG-016", "第1–6章", "景点距离排序", "scenic_sort.c",
        ("distance[10]", "id[10]", "k = i", "id[k]", "distance[k]"),
        ("struct", "qsort", "scanf(\"%d\", &distance[i]) !="),
        (
            LabCase("8 3 5 1 9 2 7 4 6 0\n", "9:0 3:1 5:2 1:3 7:4 2:5 8:6 6:7 0:8 4:9\n"),
            LabCase("0 1 2 3 4 5 6 7 8 9\n", "0:0 1:1 2:2 3:3 4:4 5:5 6:6 7:7 8:8 9:9\n"),
            LabCase("9 8 7 6 5 4 3 2 1 0\n", "9:0 8:1 7:2 6:3 5:4 4:5 3:6 2:7 1:8 0:9\n"),
            LabCase("2 1 2 1 3 3 0 0 4 4\n", "6:0 7:0 3:1 1:1 0:2 2:2 4:3 5:3 8:4 9:4\n"),
        ),
    ),
    LabSpec(
        "CW-LAB08", "08-file-score-statistics", "QB-PG-042", "第1–10章", "成绩文件统计", "score_file.c",
        ("FILE *write_file", "FILE *read_file", 'fopen("scores.txt", "w")', "fprintf", 'fopen("scores.txt", "r")', "fscanf", "== NULL", "fclose"),
        ("scanf(\"%lf\", &scores[i]) !=", "malloc", "fgets"),
        (
            LabCase("60 70 80 90 100\n", "average=80.00\nmaximum=100.00\n", (("scores.txt", "60.00\n70.00\n80.00\n90.00\n100.00\n"),)),
            LabCase("75 75 75 75 75\n", "average=75.00\nmaximum=75.00\n", (("scores.txt", "75.00\n75.00\n75.00\n75.00\n75.00\n"),)),
            LabCase("60.5 70.25 80 90.75 98.5\n", "average=80.00\nmaximum=98.50\n", (("scores.txt", "60.50\n70.25\n80.00\n90.75\n98.50\n"),)),
        ),
    ),
)


def read_utf8_lf(path: Path) -> str:
    data = path.read_bytes()
    if data.startswith(b"\xef\xbb\xbf"):
        raise ValidationError(f"UTF-8 BOM is not allowed: {path.relative_to(ROOT)}")
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValidationError(f"Non-UTF-8 file: {path.relative_to(ROOT)}") from exc
    if "\r" in text:
        raise ValidationError(f"Non-LF line ending: {path.relative_to(ROOT)}")
    if "\t" in text:
        raise ValidationError(f"Tab character is not allowed: {path.relative_to(ROOT)}")
    return text


def extract_reference(text: str, lab_id: str) -> str:
    heading = text.find("## 参考完整程序")
    if heading < 0:
        raise ValidationError(f"{lab_id} lacks 参考完整程序")
    match = re.search(r"```c\n(?P<code>.*?)\n```", text[heading:], re.DOTALL)
    if not match:
        raise ValidationError(f"{lab_id} lacks a fenced C reference program")
    return match.group("code")


def run(command: list[str], cwd: Path, stdin: str = "") -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command, cwd=cwd, input=stdin, text=True, encoding="utf-8", errors="replace",
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False, timeout=30,
    )


def validate_sheet(spec: LabSpec) -> tuple[Path, str]:
    path = LAB_ROOT / spec.directory / "README.md"
    if not path.is_file():
        raise ValidationError(f"Missing task sheet: {path.relative_to(ROOT)}")
    text = read_utf8_lf(path)
    for required in (
        spec.lab_id, "状态：`ready`", f"已学章节：{spec.chapters}", spec.question_id, "90分钟",
        REPORT_NOTICE, "## 实验项目", "## 实验目的", "## 实验步骤", "## 参考完整程序",
    ):
        if required not in text:
            raise ValidationError(f"{spec.lab_id} lacks required text: {required}")
    headings = re.findall(r"^## (.+)$", text, re.MULTILINE)
    expected_headings = ["实验项目", "实验目的", "实验步骤", "参考完整程序"]
    if headings != expected_headings:
        raise ValidationError(
            f"{spec.lab_id} headings must be exactly {expected_headings}, got {headings}"
        )
    project = text.split("## 实验项目\n", 1)[1].split("## 实验目的", 1)[0].strip()
    if project != spec.project_name:
        raise ValidationError(
            f"{spec.lab_id} project must be the short name {spec.project_name!r}, got {project!r}"
        )
    purpose = text.split("## 实验目的\n", 1)[1].split("## 实验步骤", 1)[0]
    purpose_items = re.findall(r"^(\d+)\. .+$", purpose, re.MULTILINE)
    if purpose_items != ["1", "2", "3"]:
        raise ValidationError(f"{spec.lab_id} must contain exactly three top-level purposes")
    if text.count(PAGE_BREAK) != 1:
        raise ValidationError(f"{spec.lab_id} must contain exactly one page break")
    steps = text.index("## 实验步骤")
    page_break = text.index(PAGE_BREAK)
    reference = text.index("## 参考完整程序")
    if not steps < page_break < reference:
        raise ValidationError(f"{spec.lab_id} page break is not between steps and answer")
    if PAGE_BREAK + "\n## 参考完整程序" not in text:
        raise ValidationError(f"{spec.lab_id} reference answer must immediately follow the page break")
    steps_text = text[steps + len("## 实验步骤"):page_break]
    step_items = re.findall(r"^(\d+)\. .+$", steps_text, re.MULTILINE)
    if step_items != ["1", "2", "3", "4", "5", "6"]:
        raise ValidationError(f"{spec.lab_id} must contain exactly six experiment steps")
    if "| 输入 |" not in steps_text or "预期" not in steps_text:
        raise ValidationError(f"{spec.lab_id} must integrate a test table into experiment steps")
    if len(re.findall(r"\bQB-PG-\d{3}\b", text)) != 1:
        raise ValidationError(f"{spec.lab_id} must name exactly one core programming ID once")
    forbidden_student_text = (
        "提交文件名", "源码骨架", "## 编译与运行", "## 测试", "## 提交要求",
        "## 验收标准", "不要", "不得", "禁止", "不使用", "不定义", ".exe", "gcc ",
    )
    for item in forbidden_student_text:
        if item in text:
            raise ValidationError(f"{spec.lab_id} contains forbidden student-facing text: {item}")
    if re.search(r"提交[^\n]*\.c\b", text):
        raise ValidationError(f"{spec.lab_id} asks students to submit C source code")
    code = extract_reference(text, spec.lab_id)
    for item in spec.required_code:
        if item not in code:
            raise ValidationError(f"{spec.lab_id} reference code lacks: {item}")
    for item in spec.forbidden_code:
        if item in code:
            raise ValidationError(f"{spec.lab_id} reference code exceeds scope: {item}")
    return path, code


def validate_programs(programs: dict[str, str]) -> tuple[int, int]:
    gcc = shutil.which("gcc")
    if not gcc:
        raise ValidationError("gcc was not found")
    machine = subprocess.run(
        [gcc, "-dumpmachine"], text=True, encoding="utf-8", errors="replace",
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
    )
    if machine.returncode != 0 or "mingw" not in machine.stdout.lower():
        raise ValidationError("gcc is not MinGW-w64 GCC")
    compiled = 0
    cases = 0
    with tempfile.TemporaryDirectory(prefix="clp-lab-validation-") as directory:
        root = Path(directory)
        for spec in SPECS:
            work = root / spec.lab_id
            work.mkdir()
            source = work / spec.validation_filename
            executable = work / f"{Path(spec.validation_filename).stem}.exe"
            source.write_text(programs[spec.lab_id], encoding="utf-8", newline="\n")
            result = run([
                gcc, "-std=c11", "-Wall", "-Wextra", "-Wpedantic", "-Werror",
                "-D__USE_MINGW_ANSI_STDIO=1", str(source), "-o", str(executable),
            ], work)
            if result.returncode != 0:
                raise ValidationError(
                    f"{spec.lab_id} reference program failed to compile:\n{result.stderr.strip()}"
                )
            compiled += 1
            for index, case in enumerate(spec.cases, 1):
                case_dir = work / f"case-{index}"
                case_dir.mkdir()
                behavior = run([str(executable)], case_dir, case.stdin)
                actual = behavior.stdout.replace("\r\n", "\n")
                if behavior.returncode != 0 or actual != case.stdout:
                    raise ValidationError(
                        f"{spec.lab_id} case {index} failed: expected {case.stdout!r}, "
                        f"got {actual!r}, exit={behavior.returncode}, stderr={behavior.stderr!r}"
                    )
                for filename, expected in case.expected_files:
                    output = case_dir / filename
                    if not output.is_file():
                        raise ValidationError(f"{spec.lab_id} case {index} lacks {filename}")
                    actual_file = output.read_text(encoding="utf-8").replace("\r\n", "\n")
                    if actual_file != expected:
                        raise ValidationError(
                            f"{spec.lab_id} case {index} file {filename} differs"
                        )
                cases += 1
    return compiled, cases


def main() -> int:
    try:
        if not LAB_ROOT.is_dir():
            raise ValidationError("Missing lab root")
        actual_dirs = {path.name for path in LAB_ROOT.iterdir() if path.is_dir()}
        expected_dirs = {spec.directory for spec in SPECS}
        if actual_dirs != expected_dirs:
            raise ValidationError(
                f"Lab directories are {sorted(actual_dirs)}, expected {sorted(expected_dirs)}"
            )
        programs: dict[str, str] = {}
        for spec in SPECS:
            path, code = validate_sheet(spec)
            if list(path.parent.glob("*.c")):
                raise ValidationError(f"Source skeleton is not allowed in {spec.directory}")
            programs[spec.lab_id] = code
        compiled, cases = validate_programs(programs)
        print(
            f"LAB VALIDATION PASS: {len(SPECS)} task sheets, "
            f"{compiled} reference programs, {cases} behavior cases"
        )
        return 0
    except (OSError, subprocess.TimeoutExpired, ValidationError) as exc:
        print(f"LAB VALIDATION FAILED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
