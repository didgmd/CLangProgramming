#!/usr/bin/env python3
"""Shared parser for the Markdown question bank."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTIONS_ROOT = ROOT / "题库"
CATEGORY_CODES = {
    "选择题": "SC",
    "判断题": "TF",
    "程序填空": "FB",
    "读程序写结果": "TR",
    "编程题": "PG",
}
REQUIRED_FIELDS = (
    "id",
    "category",
    "chapters",
    "concepts",
    "difficulty",
    "minutes",
    "related_routines",
    "compile_mode",
    "legacy_features",
)
VALID_DIFFICULTIES = {"基础", "常规", "综合"}
VALID_COMPILE_MODES = {"none", "c11-strict", "gnu99-textbook"}
META_BLOCK = re.compile(
    r"\A<!-- question-meta\n(?P<body>.*?)\n-->\n", re.DOTALL
)
META_LINE = re.compile(r"^([a-z_]+):\s*(.*)$")
REFERENCE_CODE = re.compile(
    r"<!-- reference-c:start -->\s*```c\n(?P<code>.*?)\n```\s*"
    r"<!-- reference-c:end -->",
    re.DOTALL,
)


class QuestionError(RuntimeError):
    """Raised when a question file violates the public Markdown contract."""


@dataclass(frozen=True)
class Question:
    question_id: str
    category: str
    chapters: tuple[str, ...]
    concepts: tuple[str, ...]
    difficulty: str
    minutes: int
    related_routines: tuple[str, ...]
    compile_mode: str
    legacy_features: tuple[str, ...]
    path: Path
    text: str
    reference_code: str | None


def read_utf8_lf(path: Path) -> str:
    data = path.read_bytes()
    if data.startswith(b"\xef\xbb\xbf"):
        raise QuestionError(f"UTF-8 BOM is not allowed: {path.relative_to(ROOT)}")
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise QuestionError(f"Non-UTF-8 file: {path.relative_to(ROOT)}") from exc
    if "\ufffd" in text:
        raise QuestionError(f"Replacement character found: {path.relative_to(ROOT)}")
    if "\r" in text:
        raise QuestionError(f"Non-LF line ending found: {path.relative_to(ROOT)}")
    return text


def _split(value: str) -> tuple[str, ...]:
    if not value or value == "无":
        return ()
    return tuple(part.strip() for part in value.split("、") if part.strip())


def parse_question(path: Path) -> Question:
    text = read_utf8_lf(path)
    match = META_BLOCK.match(text)
    if not match:
        raise QuestionError(f"Missing question metadata: {path.relative_to(ROOT)}")
    fields: dict[str, str] = {}
    for line in match.group("body").splitlines():
        item = META_LINE.fullmatch(line)
        if not item:
            raise QuestionError(
                f"Malformed metadata line in {path.relative_to(ROOT)}: {line}"
            )
        fields[item.group(1)] = item.group(2).strip()
    missing = [name for name in REQUIRED_FIELDS if name not in fields]
    if missing:
        raise QuestionError(
            f"Missing metadata in {path.relative_to(ROOT)}: {', '.join(missing)}"
        )

    category = fields["category"]
    if category not in CATEGORY_CODES:
        raise QuestionError(f"Unknown category in {path.relative_to(ROOT)}: {category}")
    code = CATEGORY_CODES[category]
    question_id = fields["id"]
    if not re.fullmatch(rf"QB-{code}-\d{{3}}", question_id):
        raise QuestionError(
            f"ID/category mismatch in {path.relative_to(ROOT)}: {question_id}"
        )
    expected_name = question_id.lower().replace("-", "_") + ".md"
    if path.name != expected_name or path.parent.name != category:
        raise QuestionError(
            f"Path does not match {question_id}: {path.relative_to(ROOT)}"
        )
    if fields["difficulty"] not in VALID_DIFFICULTIES:
        raise QuestionError(f"Invalid difficulty for {question_id}")
    if fields["compile_mode"] not in VALID_COMPILE_MODES:
        raise QuestionError(f"Invalid compile mode for {question_id}")
    try:
        minutes = int(fields["minutes"])
    except ValueError as exc:
        raise QuestionError(f"Invalid minutes for {question_id}") from exc
    if minutes <= 0:
        raise QuestionError(f"Minutes must be positive for {question_id}")

    code_match = REFERENCE_CODE.search(text)
    reference_code = code_match.group("code") if code_match else None
    return Question(
        question_id=question_id,
        category=category,
        chapters=_split(fields["chapters"]),
        concepts=_split(fields["concepts"]),
        difficulty=fields["difficulty"],
        minutes=minutes,
        related_routines=_split(fields["related_routines"]),
        compile_mode=fields["compile_mode"],
        legacy_features=_split(fields["legacy_features"]),
        path=path,
        text=text,
        reference_code=reference_code,
    )


def scan_questions() -> dict[str, Question]:
    if not QUESTIONS_ROOT.is_dir():
        raise QuestionError("Missing question root: 题库/")
    questions: dict[str, Question] = {}
    for path in sorted(QUESTIONS_ROOT.rglob("*.md")):
        if path == QUESTIONS_ROOT / "README.md":
            continue
        question = parse_question(path)
        if question.question_id in questions:
            raise QuestionError(f"Duplicate question ID: {question.question_id}")
        questions[question.question_id] = question
    return dict(sorted(questions.items()))
