#!/usr/bin/env python3
"""Validate the Markdown question bank and embedded C reference answers."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True

from generate_question_index import INDEX_PATH, render_index
from question_common import (
    CATEGORY_CODES,
    QUESTIONS_ROOT,
    ROOT,
    Question,
    QuestionError,
    scan_questions,
)


EXAM_FILES = {
    "C语言程序设计（2023-2024-1）A卷（补考）.pdf",
    "C语言程序设计（2023-2024-1）B卷（正考）.pdf",
    "C语言程序设计（2024-2025-1）A卷（正考）.pdf",
    "C语言程序设计（2024-2025-1）B卷（补考）.pdf",
    "C语言程序设计（2025-2026-1-R）A卷.doc",
    "C语言程序设计（2025-2026-1-R）B卷.doc",
    "C语言程序设计2025级试题A.doc",
    "C语言程序设计2025级试题B.doc",
}
SOURCE_MARKERS = (
    "正考",
    "补考",
    "A卷",
    "B卷",
    "学年",
    "试卷来源",
)

BEHAVIOR_FIXTURES: dict[str, list[tuple[str, str]]] = {
    "QB-PG-002": [("1 2 3 4 5 6 7 8 9 10\n", "10.000000\n")],
    "QB-PG-003": [("1900\n", "common\n"), ("2000\n", "leap\n")],
    "QB-PG-005": [("2024 2 29\n", "60\n"), ("2023 2 29\n", "invalid\n")],
    "QB-PG-006": [("2\n", "prime\n"), ("1\n", "not prime\n")],
    "QB-PG-007": [("-2048\n", "-2048\n"), ("12x\n", "invalid\n")],
    "QB-PG-010": [("1 2 3 4 5 6 20 8 9 10 11 12\n", "20 1 2\n")],
    "QB-PG-018": [("0\n", "1\n"), ("21\n", "invalid\n")],
    "QB-PG-021": [("1 2 3 4 5 6 7 8 9\n", "1 4 7\n2 5 8\n3 6 9\n")],
    "QB-PG-038": [("hello world\n", "11\n"), ("\n", "0\n")],
}


class ValidationError(RuntimeError):
    """Raised when a question-bank invariant fails."""


def run(
    command: list[str],
    *,
    cwd: Path | None = None,
    input_text: str | None = None,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=cwd,
        input=input_text,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        timeout=30,
    )


def validate_layout() -> None:
    expected = set(CATEGORY_CODES)
    actual = {
        path.name for path in QUESTIONS_ROOT.iterdir()
        if path.is_dir() and not path.name.startswith(".")
    }
    if actual != expected:
        raise ValidationError(
            f"Question category directories are {sorted(actual)}, expected {sorted(expected)}"
        )
    residue = [
        path for path in ROOT.rglob("*")
        if path.is_file() and path.suffix.lower() in {".exe", ".o", ".obj", ".pyc"}
        and ".git" not in path.parts
    ]
    residue.extend(path for path in ROOT.rglob("__pycache__") if path.is_dir())
    if residue:
        raise ValidationError(
            "Process artifacts remain: "
            + ", ".join(str(path.relative_to(ROOT)) for path in residue[:20])
        )


def validate_source_boundary() -> None:
    git = shutil.which("git")
    if not git:
        raise ValidationError("git is required for source-paper checks")
    tracked = run([git, "ls-files", "--", "*.pdf", "*.doc"], cwd=ROOT)
    if tracked.returncode != 0:
        raise ValidationError(tracked.stderr.strip())
    tracked_names = {Path(line).name for line in tracked.stdout.splitlines()}
    leaked = EXAM_FILES & tracked_names
    if leaked:
        raise ValidationError("Original exam file is tracked: " + ", ".join(sorted(leaked)))
    for name in EXAM_FILES:
        ignored = run([git, "check-ignore", "-q", "--", name], cwd=ROOT)
        if ignored.returncode != 0:
            raise ValidationError(f"Original exam file is not ignored: {name}")


def validate_question(question: Question) -> None:
    if not question.chapters or not all(item.isdigit() for item in question.chapters):
        raise ValidationError(f"Invalid chapters for {question.question_id}")
    if not question.concepts:
        raise ValidationError(f"Missing concepts for {question.question_id}")
    if "# " not in question.text[:500]:
        raise ValidationError(f"Missing title for {question.question_id}")
    if "## 题目" not in question.text or "## 常见失分点" not in question.text:
        raise ValidationError(f"Incomplete student sections for {question.question_id}")
    if "<details>" not in question.text or "<summary>参考答案与解析</summary>" not in question.text:
        raise ValidationError(f"Missing folded answer for {question.question_id}")
    if "</details>" not in question.text:
        raise ValidationError(f"Unclosed answer for {question.question_id}")
    for marker in SOURCE_MARKERS:
        if marker in question.text:
            raise ValidationError(
                f"Source identity marker '{marker}' appears in {question.question_id}"
            )
    if re.search(r"20\d{2}\s*[-~/]\s*20\d{2}", question.text):
        raise ValidationError(f"Academic-year marker appears in {question.question_id}")
    needs_code = question.category in {"程序填空", "编程题"}
    if needs_code and question.compile_mode == "none":
        raise ValidationError(f"{question.question_id} must declare a compile mode")
    if needs_code and not question.reference_code:
        raise ValidationError(f"{question.question_id} lacks a complete reference program")
    if question.reference_code and question.compile_mode == "none":
        raise ValidationError(f"{question.question_id} has code but compile mode is none")


def validate_routine_links(questions: dict[str, Question]) -> None:
    routine_ids: set[str] = set()
    for path in (ROOT / "例程").rglob("*.c"):
        text = path.read_text(encoding="utf-8")
        match = re.search(r"例程 ID：([A-Z0-9-]+)", text)
        if match:
            routine_ids.add(match.group(1))
    missing = sorted({
        routine_id
        for question in questions.values()
        for routine_id in question.related_routines
        if routine_id not in routine_ids
    })
    if missing:
        raise ValidationError("Unknown related routine IDs: " + ", ".join(missing))


def validate_compiler(gcc: str) -> None:
    machine = run([gcc, "-dumpmachine"])
    if machine.returncode != 0 or "mingw" not in machine.stdout.lower():
        raise ValidationError("gcc is not MinGW-w64 GCC")
    version = run([gcc, "-dumpversion"])
    try:
        major = int(version.stdout.strip().split(".")[0])
    except ValueError as exc:
        raise ValidationError("Cannot determine GCC version") from exc
    if major < 8:
        raise ValidationError("MinGW-w64 GCC 8.1 or newer is required")


def compile_answers(questions: dict[str, Question], gcc: str) -> tuple[int, int]:
    compiled = 0
    behaviors = 0
    temp_path: Path | None = None
    with tempfile.TemporaryDirectory(prefix="clp-question-validation-") as directory:
        temp_path = Path(directory)
        for question in questions.values():
            if not question.reference_code:
                continue
            source = temp_path / f"{question.question_id}.c"
            executable = temp_path / f"{question.question_id}.exe"
            source.write_text(question.reference_code, encoding="utf-8", newline="\n")
            flags = (
                ["-std=c11", "-Wall", "-Wextra", "-Wpedantic", "-Werror"]
                if question.compile_mode == "c11-strict"
                else ["-std=gnu99", "-Wall", "-Wextra"]
            )
            result = run([gcc, *flags, str(source), "-o", str(executable), "-lm"])
            if result.returncode != 0:
                raise ValidationError(
                    f"Reference program failed for {question.question_id}:\n"
                    f"{result.stderr.strip()}"
                )
            compiled += 1
            for stdin_text, expected_stdout in BEHAVIOR_FIXTURES.get(
                question.question_id, []
            ):
                behavior = run([str(executable)], cwd=temp_path, input_text=stdin_text)
                actual = behavior.stdout.replace("\r\n", "\n")
                if behavior.returncode != 0 or actual != expected_stdout:
                    raise ValidationError(
                        f"Behavior failed for {question.question_id}: "
                        f"expected {expected_stdout!r}, got {actual!r}; "
                        f"stderr={behavior.stderr.strip()!r}"
                    )
                behaviors += 1
    if temp_path is not None and temp_path.exists():
        raise ValidationError(f"Temporary directory was not removed: {temp_path}")
    return compiled, behaviors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", dest="question_id")
    parser.add_argument("--gcc", default=None, help="Path to MinGW-w64 GCC")
    args = parser.parse_args()
    try:
        validate_layout()
        validate_source_boundary()
        questions = scan_questions()
        if args.question_id:
            if args.question_id not in questions:
                raise ValidationError(f"Unknown question ID: {args.question_id}")
            questions = {args.question_id: questions[args.question_id]}
        for question in questions.values():
            validate_question(question)
        validate_routine_links(questions)
        if not args.question_id:
            current = INDEX_PATH.read_text(encoding="utf-8") if INDEX_PATH.is_file() else ""
            if current != render_index(questions):
                raise ValidationError(
                    "题库/README.md is out of date; run generate_question_index.py"
                )
        gcc = args.gcc or shutil.which("gcc")
        if not gcc:
            raise ValidationError("gcc was not found")
        validate_compiler(gcc)
        compiled, behaviors = compile_answers(questions, gcc)
        print(
            f"QUESTION VALIDATION PASS: {len(questions)} questions, "
            f"{compiled} embedded reference programs, {behaviors} behavior cases"
        )
        return 0
    except (OSError, QuestionError, ValidationError, subprocess.TimeoutExpired) as exc:
        print(f"QUESTION VALIDATION FAILED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
