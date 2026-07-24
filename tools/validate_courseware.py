#!/usr/bin/env python3
"""Validate the CW-L01 offline interactive HTML courseware."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
CW_L01 = ROOT / "课件" / "讲授" / "01-course-introduction-and-hello-world" / "index.html"
ALLOWED_EXTERNAL_HREFS = frozenset({"https://w3schools.org.cn/c/index.php"})

REQUIRED_MARKERS = (
    'data-courseware="c-freshman"',
    'data-layout="slide-page"',
    'data-course-id="CW-L01"',
    'data-routines="EX-C01-001"',
    'data-questions="QB-SC-001,QB-SC-002"',
    'data-attribution="Kevin@SUT"',
    '<meta name="author" content="Kevin@SUT">',
    '<meta name="copyright" content="Kevin@SUT">',
    "<style>",
    "<script>",
    "data-deck",
    "data-slide",
    "data-interaction=",
    "data-code-line",
    "data-prediction",
    "data-step-line",
    "data-token",
    "data-error-choice",
    "data-preview-practice",
    "data-review-item",
    'id="brace-feedback"',
)

REQUIRED_SECTIONS = {
    "objectives",
    "quiz",
    "overview",
    "concept-include",
    "concept-main",
    "concept-printf",
    "concept-return",
    "interaction-stepper",
    "workflow",
    "diagnosis",
    "exercise",
    "summary",
}

EXTERNAL_PATTERNS = (
    r"//cdn\.",
    r"cdnjs",
    r"unpkg",
    r"jsdelivr",
    r"<link\b[^>]+href=",
    r"<img\b[^>]+src=",
    r"<iframe\b",
    r"@import\s+url",
    r"\bfetch\s*\(",
    r"\bXMLHttpRequest\b",
    r"\blocalStorage\b",
)

TEACHER_ONLY_PATTERNS = (
    r"教师讲稿",
    r"教师提示",
    r"教师备注",
    r"教师节奏",
    r"评分提醒",
    r"制作记录",
    r"lecture script",
    r"teacher[- ]notes?",
)

ANCHOR_PATTERN = re.compile(r'<a\b[^>]*\bhref="(?P<href>[^"]+)"[^>]*>', re.IGNORECASE)
EXTERNAL_URL_PATTERN = re.compile(r'https?://[^\s"<>]+', re.IGNORECASE)
SLIDE_PATTERN = re.compile(r'<section\b[^>]*\bdata-slide(?:\s|>|=)', re.IGNORECASE)
SECTION_PATTERN = re.compile(r'<section\b[^>]*\bdata-section="([^"]+)"', re.IGNORECASE)


def target_for(course_id: str) -> Path:
    if course_id == "CW-L01":
        return CW_L01
    raise ValueError(f"unknown courseware id: {course_id}")


def fail(failures: list[str], message: str) -> None:
    failures.append(message)


def check_links(text: str, path: Path, failures: list[str]) -> None:
    external_seen: list[str] = []
    for match in ANCHOR_PATTERN.finditer(text):
        href = match.group("href")
        parsed = urlparse(href)
        if parsed.scheme or parsed.netloc:
            if href not in ALLOWED_EXTERNAL_HREFS:
                fail(failures, f"external link is not allowlisted: {href}")
            elif 'data-external-resource="optional"' not in match.group(0):
                fail(failures, f"allowlisted external link lacks optional marker: {href}")
            else:
                external_seen.append(href)
            continue
        if href.startswith("#") or not href:
            continue
        target = (path.parent / href.split("#", 1)[0]).resolve()
        try:
            target.relative_to(ROOT.resolve())
        except ValueError:
            fail(failures, f"link escapes repository: {href}")
            continue
        if not target.exists():
            fail(failures, f"broken local link: {href} -> {target}")

    for href in EXTERNAL_URL_PATTERN.findall(text):
        if href not in ALLOWED_EXTERNAL_HREFS:
            fail(failures, f"external URL is not allowlisted: {href}")

    if external_seen.count("https://w3schools.org.cn/c/index.php") != 1:
        fail(failures, "CW-L01 must contain exactly one marked W3Schools optional link")

def validate(path: Path) -> list[str]:
    failures: list[str] = []
    if not path.exists():
        return [f"file not found: {path}"]

    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        fail(failures, "UTF-8 BOM is not allowed")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        return [f"invalid UTF-8: {exc}"]

    if "\t" in text:
        fail(failures, "tab characters are not allowed")
    if "<html" not in text.lower() or "</html>" not in text.lower():
        fail(failures, "document is not a complete HTML file")
    if "overflow: hidden" not in text:
        fail(failures, "slide/page mode must hide page-level overflow")

    for marker in REQUIRED_MARKERS:
        if marker not in text:
            fail(failures, f"missing required marker: {marker}")

    for pattern in EXTERNAL_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            fail(failures, f"external or persistent dependency found: {pattern}")

    for pattern in TEACHER_ONLY_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            fail(failures, f"teacher-only content found: {pattern}")

    slides = SLIDE_PATTERN.findall(text)
    sections = SECTION_PATTERN.findall(text)
    if len(slides) != 12:
        fail(failures, f"expected 12 slides, found {len(slides)}")
    if len(sections) != len(set(sections)):
        fail(failures, "slide sections are not unique")
    missing_sections = REQUIRED_SECTIONS.difference(sections)
    if missing_sections:
        fail(failures, f"missing slide sections: {', '.join(sorted(missing_sections))}")

    if text.count('data-interaction="ask-wait-reveal"') < 5:
        fail(failures, "not enough ask-wait-reveal interactions")
    if len(re.findall(r'data-code-line="', text)) < 6:
        fail(failures, "fewer than six code-line markers")
    if len(re.findall(r'data-prediction="', text)) != 4:
        fail(failures, "output prediction must contain exactly four options")
    if len(re.findall(r'data-step-line="', text)) != 6:
        fail(failures, "stepper must contain exactly six executable code lines")
    if len(re.findall(r'data-token="', text)) != 5:
        fail(failures, "printf token interaction must contain five tokens")
    if len(re.findall(r'data-error-choice="', text)) != 3:
        fail(failures, "error diagnosis must contain three cases")
    if len(re.findall(r'data-review-item(?:\s|>)', text)) != 7:
        fail(failures, "review checklist must contain seven items")
    if "setFeedback(braceFeedback" not in text:
        fail(failures, "brace explanation must target brace-feedback")
    if ".review-item.done strong" not in text or "color: #155e35;" not in text:
        fail(failures, "completed review items must use an explicit dark text color")

    canonical_tokens = (
        "#include &lt;stdio.h&gt;",
        "int main()",
        'printf("This is a C program.\\n");',
        "return 0;",
    )
    for token in canonical_tokens:
        if token not in text:
            fail(failures, f"canonical EX-C01-001 token missing: {token}")

    for marker in (
        "data-reset-prediction",
        "data-step-next",
        "data-step-reset",
        "data-preview-practice",
        "data-reset-practice",
        "data-stage-button",
    ):
        if marker not in text:
            fail(failures, f"missing interaction control: {marker}")

    if "Hello World" not in text:
        fail(failures, "Hello World practice variant is missing")
    if "不是真实C编译" not in text:
        fail(failures, "simulated execution boundary is not visible to students")

    check_links(text, path, failures)
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--id", default="CW-L01", help="courseware id, currently CW-L01")
    parser.add_argument("--path", type=Path, help="explicit HTML path for local validation")
    args = parser.parse_args()

    try:
        path = args.path.resolve() if args.path else target_for(args.id)
    except ValueError as exc:
        print(f"COURSEWARE VALIDATION FAILED: {exc}")
        return 2

    failures = validate(path)
    if failures:
        print("COURSEWARE VALIDATION FAILED")
        for item in failures:
            print(f"- {item}")
        return 1

    print(f"COURSEWARE VALIDATION PASS: {args.id}, slides=12, offline-core=ok, optional_external=1, links=ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

