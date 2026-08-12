#!/usr/bin/env python3
"""Validate the offline interactive HTML courseware lessons."""

from __future__ import annotations

import argparse
import html
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import urlparse

sys.dont_write_bytecode = True

from question_common import scan_questions


ROOT = Path(__file__).resolve().parents[1]
CW_L01 = ROOT / "课件" / "讲授" / "01-course-introduction-and-hello-world" / "index.html"
CW_L02 = ROOT / "课件" / "讲授" / "02-algorithms-and-program-logic" / "index.html"
CW_L03 = ROOT / "课件" / "讲授" / "03-sequential-programming" / "index.html"
CW_L04 = ROOT / "课件" / "讲授" / "04-selection-if" / "index.html"
CW_L05 = ROOT / "课件" / "讲授" / "05-selection-nesting-and-switch" / "index.html"
CW_L06 = ROOT / "课件" / "讲授" / "06-loops-and-state" / "index.html"
CW_L07 = ROOT / "课件" / "讲授" / "07-nested-loops-and-primes" / "index.html"
CW_L08 = ROOT / "课件" / "讲授" / "08-one-dimensional-arrays" / "index.html"
CW_L09 = ROOT / "课件" / "讲授" / "09-matrices-and-strings" / "index.html"
CW_L10 = ROOT / "课件" / "讲授" / "10-functions-and-parameters" / "index.html"
CW_L11 = ROOT / "课件" / "讲授" / "11-recursion" / "index.html"
CW_L12 = ROOT / "课件" / "讲授" / "12-pointer-model-and-arrays" / "index.html"
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
SECTION_BLOCK_PATTERN = re.compile(r'<section\b[^>]*\bdata-section="([^"]+)"[^>]*>(.*?)</section>', re.IGNORECASE | re.DOTALL)

CW_L02_STUDENT_FORBIDDEN = (
    "今天不画流程图",
    "先问自己",
    "再让程序工作",
    "课堂变体",
    "课堂练习变体",
    "本课不要求",
    "教师提示",
    "教师讲稿",
    "评分提醒",
    "制作记录",
    "编程题的共同结构",
    "题面信息如何变成 C 程序",
    "同一程序骨架对应多种考试题型",
    "题型迁移",
    "考试重点",
    "考点",
    "失分点",
    "解题模板",
    "读题动作",
    "代码动作",
    "权威程序",
    "教学变体",
    "课件练习变体",
    "不新增题库 ID",
)

CW_L02_QUESTION_IDS = (
    "QB-SC-003",
    "QB-SC-004",
    "QB-SC-005",
    "QB-SC-007",
    "QB-SC-036",
    "QB-SC-037",
    "QB-SC-055",
    "QB-SC-059",
)

QUESTION_BLOCK_PATTERN = re.compile(
    r'<article\b[^>]*\bdata-question-id="(?P<id>[^"]+)"[^>]*>(?P<body>.*?)</article>',
    re.IGNORECASE | re.DOTALL,
)
QUESTION_TEXT_PATTERN = re.compile(
    r'<p\b[^>]*\bclass="[^"]*question-text[^"]*"[^>]*>(?P<body>.*?)</p>',
    re.IGNORECASE | re.DOTALL,
)
QUESTION_OPTION_PATTERN = re.compile(
    r'<button\b(?P<attrs>[^>]*)\bdata-question-option="(?P<label>[A-D])"(?P<rest>[^>]*)>(?P<body>.*?)</button>',
    re.IGNORECASE | re.DOTALL,
)


def normalize_visible_text(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    value = html.unescape(value).replace("`", "")
    return re.sub(r"\s+", " ", value).strip()


def question_source_parts(text: str) -> tuple[str, dict[str, str]]:
    match = re.search(
        r"## 题目\s*(?P<body>.*?)\s*## 常见失分点",
        text,
        re.DOTALL,
    )
    if not match:
        raise ValueError("missing question body")
    prompt_lines: list[str] = []
    options: dict[str, str] = {}
    for raw_line in match.group("body").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        option = re.fullmatch(r"([A-D])\.\s*(.*)", line)
        if option:
            options[option.group(1)] = normalize_visible_text(option.group(2))
        else:
            prompt_lines.append(line)
    return normalize_visible_text(" ".join(prompt_lines)), options


def validate_embedded_questions(
    text: str,
    failures: list[str],
    expected_ids: tuple[str, ...],
    course_id: str,
) -> None:
    source_questions = scan_questions()
    blocks = list(QUESTION_BLOCK_PATTERN.finditer(text))
    block_ids = [match.group("id") for match in blocks]
    if sorted(block_ids) != sorted(expected_ids):
        fail(
            failures,
            f"{course_id} embedded choice-question IDs do not match the declared set",
        )
        return

    for block in blocks:
        question_id = block.group("id")
        body = block.group("body")
        prompt_match = QUESTION_TEXT_PATTERN.search(body)
        if not prompt_match:
            fail(failures, f"{question_id} lacks a visible question prompt")
            continue
        html_prompt = normalize_visible_text(prompt_match.group("body"))
        option_matches = list(QUESTION_OPTION_PATTERN.finditer(body))
        html_options = {
            option.group("label"): normalize_visible_text(option.group("body"))[3:].strip()
            if normalize_visible_text(option.group("body")).startswith(f"{option.group('label')}. ")
            else normalize_visible_text(option.group("body"))
            for option in option_matches
        }
        if set(html_options) != {"A", "B", "C", "D"}:
            fail(failures, f"{question_id} must expose options A-D")
        for option in option_matches:
            attrs = option.group("attrs") + option.group("rest")
            if 'data-feedback="' not in attrs or 'data-correct="' not in attrs:
                fail(failures, f"{question_id} option {option.group('label')} lacks feedback metadata")

        source_prompt, source_options = question_source_parts(
            source_questions[question_id].text
        )
        if html_prompt != source_prompt:
            fail(failures, f"{question_id} prompt differs from the question bank")
        if html_options != source_options:
            fail(failures, f"{question_id} options differ from the question bank")


def target_for(course_id: str) -> Path:
    if course_id == "CW-L01":
        return CW_L01
    if course_id == "CW-L02":
        return CW_L02
    if course_id == "CW-L03":
        return CW_L03
    if course_id == "CW-L04":
        return CW_L04
    if course_id == "CW-L05":
        return CW_L05
    if course_id == "CW-L06":
        return CW_L06
    if course_id == "CW-L07":
        return CW_L07
    if course_id == "CW-L08":
        return CW_L08
    if course_id == "CW-L09":
        return CW_L09
    if course_id == "CW-L10":
        return CW_L10
    if course_id == "CW-L11":
        return CW_L11
    if course_id == "CW-L12":
        return CW_L12
    raise ValueError(f"unknown courseware id: {course_id}")


def fail(failures: list[str], message: str) -> None:
    failures.append(message)


def check_links(
    text: str,
    path: Path,
    failures: list[str],
    *,
    require_optional_external: bool = True,
) -> None:
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

    if require_optional_external and external_seen.count("https://w3schools.org.cn/c/index.php") != 1:
        fail(failures, "CW-L01 must contain exactly one marked W3Schools optional link")
    if not require_optional_external and external_seen:
        fail(failures, "courseware must remain fully offline and contain no external links")


def validate_cw_l02(path: Path) -> list[str]:
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

    required_markers = (
        'data-courseware="c-freshman-interactive-html"',
        'data-layout="slide-page"',
        'data-course-id="CW-L02"',
        'data-chapter="2"',
        'data-routines="EX-C01-001"',
        'data-lesson-variants="hello-world-to-variable,scanf-score-input,three-score-practice"',
        'data-questions="QB-SC-003,QB-SC-004,QB-SC-005,QB-SC-007,QB-SC-036,QB-SC-037,QB-SC-055,QB-SC-059"',
        'data-attribution="Kevin@SUT"',
        '<meta name="author" content="Kevin@SUT">',
        '<meta name="copyright" content="Kevin@SUT">',
        "<style>",
        "<script>",
        "data-deck",
        "data-slide",
        'data-interaction="ask-wait-reveal"',
        'class="code-line',
        "data-lesson-variants",
        "data-review-item",
        "scanf",
        "三门成绩",
    )
    for marker in required_markers:
        if marker not in text:
            fail(failures, f"missing CW-L02 marker: {marker}")

    for pattern in EXTERNAL_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            fail(failures, f"external or persistent dependency found: {pattern}")
    for pattern in TEACHER_ONLY_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            fail(failures, f"teacher-only content found: {pattern}")
    for phrase in CW_L02_STUDENT_FORBIDDEN:
        if phrase in text:
            fail(failures, f"student-facing teacher-prep phrase found: {phrase}")

    slides = SLIDE_PATTERN.findall(text)
    sections = SECTION_PATTERN.findall(text)
    if len(slides) != 25:
        fail(failures, f"CW-L02 expected 25 slides, found {len(slides)}")
    if len(sections) != len(set(sections)):
        fail(failures, "CW-L02 slide sections are not unique")
    section_blocks = SECTION_BLOCK_PATTERN.findall(text)
    if len(section_blocks) != 25:
        fail(failures, f"CW-L02 expected 25 complete section blocks, found {len(section_blocks)}")
    for section_id, block in section_blocks:
        if not re.search(r"\b(definition|rule-card|code-panel|data-table|feedback|review-item)\b", block):
            fail(failures, f"CW-L02 slide lacks a student-facing explanation or example: {section_id}")

    first_half = section_blocks[:13]
    for index, (section_id, block) in enumerate(first_half, start=1):
        visible = normalize_visible_text(block)
        forbidden_first_half = ("scanf", "%lf", "&score", "输入函数", "变量地址", "输入格式说明符")
        for marker in forbidden_first_half:
            if marker.lower() in visible.lower():
                fail(failures, f"CW-L02 slide {index} introduces input content early: {marker} ({section_id})")
    if "scanf" not in normalize_visible_text(section_blocks[13][1]).lower():
        fail(failures, "CW-L02 slide 14 must be the first visible scanf introduction")

    if text.count("<details") != 0:
        fail(failures, "CW-L02 must not hide knowledge or exercises in details elements")
    if text.count('data-interaction="ask-wait-reveal"') < 8:
        fail(failures, "CW-L02 needs at least eight ask-wait-reveal interactions")
    if len(re.findall(r'class="[^"]*\bcode-line\b', text)) < 50:
        fail(failures, "CW-L02 needs at least fifty code-line markers")
    if len(re.findall(r'data-variable-step="', text)) != 3:
        fail(failures, "CW-L02 variable stepper must contain three steps")
    if len(re.findall(r'data-fixed-step="', text)) != 8:
        fail(failures, "CW-L02 fixed-data stepper must contain eight steps")
    if len(re.findall(r'data-input-step="', text)) != 6:
        fail(failures, "CW-L02 input stepper must contain six steps")
    if len(re.findall(r'data-output-token="', text)) != 5:
        fail(failures, "CW-L02 printf interaction must contain five format tokens")
    if len(re.findall(r'data-scanf-part="', text)) != 2:
        fail(failures, "CW-L02 scanf interaction must contain two parts")
    if len(re.findall(r'data-score-input="', text)) != 3:
        fail(failures, "CW-L02 score simulator must contain three valid fixtures")
    if len(re.findall(r'data-practice-input="', text)) != 3:
        fail(failures, "CW-L02 practice simulator must contain three valid fixtures")
    if len(re.findall(r'data-error-id="', text)) != 2:
        fail(failures, "CW-L02 input diagnosis must contain two repair cases")
    if len(re.findall(r'data-review-item(?:\s|>)', text)) != 7:
        fail(failures, "CW-L02 review checklist must contain seven items")
    validate_embedded_questions(text, failures, CW_L02_QUESTION_IDS, "CW-L02")

    pre_blocks = "\n".join(re.findall(r"<pre\b[^>]*>(.*?)</pre>", text, re.IGNORECASE | re.DOTALL))
    code_text = html.unescape(re.sub(r"<[^>]+>", "", pre_blocks))
    if re.search(r"\bif\s*\(", code_text):
        fail(failures, "CW-L02 C blocks must not introduce if")
    if re.search(r"\breturn\s+1\s*;", code_text):
        fail(failures, "CW-L02 C blocks must not introduce return 1")
    if "scanf(\"%d\", &score);" not in code_text:
        fail(failures, "CW-L02 simplified scanf example is missing")
    if "scanf(\"%d %d %d\", &score1, &score2, &score3);" not in code_text:
        fail(failures, "CW-L02 three-score scanf example is missing")
    if text.count("输入约束") < 10:
        fail(failures, "CW-L02 must state input constraints near the scanf examples")
    if "sum=240\naverage=80.00" not in text:
        fail(failures, "CW-L02 fixed-data program must declare its exact output")
    if len(re.findall(r'data-question-option="[A-D]"', text)) != 32:
        fail(failures, "CW-L02 must expose four options for each of eight questions")

    diagnostics = next((block for section_id, block in section_blocks if section_id == "input-diagnostics"), "")
    diagnostics_visible = normalize_visible_text(diagnostics)
    for obsolete in ("数量不匹配", "三个变量需要三个格式说明符", "声明变量就必须赋值"):
        if obsolete in diagnostics_visible:
            fail(failures, f"CW-L02 P22 retains an incorrect variable-count rule: {obsolete}")
    required_diagnostics = (
        'scanf("%d,%d,%d", &amp;a, &amp;b, &amp;c);',
        '"%d%d%d"',
        '"%d %d %d"',
        '"%d,%d,%d"',
        "逗号必须实际出现",
        "变量是否需要赋值取决于后续是否使用",
    )
    for marker in required_diagnostics:
        if marker not in diagnostics:
            fail(failures, f"CW-L02 P22 separator rule is incomplete: {marker}")

    simple_command = "gcc score.c -o score.exe\n.\\score.exe"
    if simple_command not in text:
        fail(failures, "CW-L02 P25 must show the two-line beginner GCC command")
    if "gcc -std=c11 -Wall -Wextra -Wpedantic score.c -o score.exe" in text:
        fail(failures, "CW-L02 P25 still exposes the strict maintenance command")

    check_links(text, path, failures, require_optional_external=False)
    return failures


def validate_cw_l03(path: Path) -> list[str]:
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

    required_markers = (
        'data-courseware="c-freshman-interactive-html"',
        'data-layout="slide-page"',
        'data-course-id="CW-L03"',
        'data-chapter="3"',
        'data-routines="EX-C03-004"',
        'data-questions="QB-PG-014,QB-SC-008,QB-SC-059"',
        'data-lesson-variants="four-digit-cube-sum-sequential,heron-triangle-area-input"',
        'data-attribution="Kevin@SUT"',
        '<meta name="author" content="Kevin@SUT">',
        '<meta name="copyright" content="Kevin@SUT">',
        'data-programming-question-id="QB-PG-014"',
        'data-interaction="ask-wait-reveal"',
        "data-code-line",
        "active-code-line",
    )
    for marker in required_markers:
        if marker not in text:
            fail(failures, f"missing CW-L03 marker: {marker}")

    for pattern in EXTERNAL_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            fail(failures, f"external or persistent dependency found: {pattern}")
    for pattern in TEACHER_ONLY_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            fail(failures, f"teacher-only content found: {pattern}")
    for phrase in CW_L02_STUDENT_FORBIDDEN:
        if phrase in text:
            fail(failures, f"student-facing teacher-prep phrase found: {phrase}")

    slides = SLIDE_PATTERN.findall(text)
    sections = SECTION_PATTERN.findall(text)
    section_blocks = SECTION_BLOCK_PATTERN.findall(text)
    if len(slides) != 25:
        fail(failures, f"CW-L03 expected 25 slides, found {len(slides)}")
    if len(sections) != len(set(sections)):
        fail(failures, "CW-L03 slide sections are not unique")
    if len(section_blocks) != 25:
        fail(failures, f"CW-L03 expected 25 complete section blocks, found {len(section_blocks)}")
    if text.count("<details") != 0:
        fail(failures, "CW-L03 must expose all knowledge and exercises directly")

    validate_embedded_questions(
        text,
        failures,
        ("QB-SC-008", "QB-SC-059"),
        "CW-L03",
    )
    if len(re.findall(r'data-question-option="[A-D]"', text)) != 8:
        fail(failures, "CW-L03 must expose four options for each choice question")

    question_source = scan_questions()["QB-PG-014"].text
    source_prompt_match = re.search(
        r"## 题目\s*(.*?)\s*### 输入格式",
        question_source,
        re.DOTALL,
    )
    source_prompt = ""
    if not source_prompt_match:
        fail(failures, "QB-PG-014 lacks a parseable prompt in the question bank")
    else:
        source_prompt = normalize_visible_text(source_prompt_match.group(1))
    programming_block_match = re.search(
        r'<article\b[^>]*data-programming-question-id="QB-PG-014"[^>]*>(.*?)</article>',
        text,
        re.IGNORECASE | re.DOTALL,
    )
    if not programming_block_match:
        fail(failures, "CW-L03 must visibly embed QB-PG-014")
    else:
        programming_text = normalize_visible_text(programming_block_match.group(1))
        if source_prompt and source_prompt not in programming_text:
            fail(failures, "QB-PG-014 prompt differs from the question bank")
        for expected in (
            "一个四位正整数。",
            "输出四个数位的立方和。",
            "1000至9999",
        ):
            if expected not in programming_text:
                fail(failures, f"QB-PG-014 visible contract is incomplete: {expected}")

    if text.count("海伦公式") < 2:
        fail(failures, "CW-L03 must name Heron's formula at least twice")
    for marker in (
        'data-formula="s=(a+b+c)/2"',
        'data-formula="S=sqrt(s(s-a)(s-b)(s-c))"',
        'data-symbol="a-b-c"',
        'data-symbol="s"',
        'data-symbol="S"',
        'data-symbol="sqrt"',
    ):
        if marker not in text:
            fail(failures, f"CW-L03 Heron explanation is incomplete: {marker}")

    pre_blocks = "\n".join(
        re.findall(r'<pre\b[^>]*class="[^"]*code-block[^"]*"[^>]*>(.*?)</pre>', text, re.IGNORECASE | re.DOTALL)
    )
    code_text = html.unescape(re.sub(r"<[^>]+>", "", pre_blocks))
    for forbidden, label in (
        (r"\bif\s*\(", "if"),
        (r"\bfor\s*\(", "for"),
        (r"\bwhile\s*\(", "while"),
        (r"\bswitch\s*\(", "switch"),
        (r"\breturn\s+1\s*;", "return 1"),
        (r"\[[^\]]*\]", "array syntax"),
    ):
        if re.search(forbidden, code_text):
            fail(failures, f"CW-L03 positive C examples must not introduce {label}")
    if re.search(r"if\s*\(\s*scanf|scanf\s*\([^;]+\)\s*[!=]=", code_text):
        fail(failures, "CW-L03 must not check scanf return values")

    required_code = (
        'scanf("%d", &n);',
        "thousands = n / 1000;",
        "hundreds = n / 100 % 10;",
        "tens = n / 10 % 10;",
        "ones = n % 10;",
        "#include <math.h>",
        'scanf("%lf %lf %lf", &a, &b, &c);',
        "s = (a + b + c) / 2.0;",
        "area = sqrt(s * (s - a) * (s - b) * (s - c));",
        'printf("%.2f\\n", area);',
    )
    for marker in required_code:
        if marker not in code_text:
            fail(failures, f"CW-L03 positive program is incomplete: {marker}")

    interaction_counts = (
        ('data-digit-input="', 3, "digit fixtures"),
        ('data-digit-step="', 10, "digit execution steps"),
        ('data-digit-error="', 3, "digit diagnosis cases"),
        ('data-digit-test="', 3, "digit tests"),
        ('data-symbol="', 4, "Heron symbols"),
        ('data-factor="', 4, "Heron factors"),
        ('data-area-step="', 7, "area execution steps"),
        ('data-area-error="', 3, "area diagnosis cases"),
        ('data-area-test="', 3, "area tests"),
        ('data-review-answer="', 7, "review questions"),
    )
    for marker, expected_count, label in interaction_counts:
        actual = text.count(marker)
        if actual != expected_count:
            fail(failures, f"CW-L03 expected {expected_count} {label}, found {actual}")

    for fixture in (
        'data-digit-test="1234" data-expected-output="100"',
        'data-digit-test="1000" data-expected-output="1"',
        'data-digit-test="9999" data-expected-output="2916"',
        'data-area-test="3 4 5" data-expected-output="6.00"',
        'data-area-test="2 2 2" data-expected-output="1.73"',
        'data-area-test="3.67 5.43 6.21" data-expected-output="9.90"',
    ):
        if fixture not in text:
            fail(failures, f"CW-L03 deterministic fixture is missing: {fixture}")

    for command in (
        "gcc digits.c -o digits.exe\n.\\digits.exe",
        "gcc triangle.c -o triangle.exe\n.\\triangle.exe",
    ):
        if command not in text:
            fail(failures, f"CW-L03 beginner command is missing: {command.splitlines()[0]}")

    check_links(text, path, failures, require_optional_external=False)
    return failures


def validate_cw_l04(path: Path) -> list[str]:
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
    if "overflow:hidden" not in text.replace(" ", ""):
        fail(failures, "slide/page mode must hide page-level overflow")

    required_markers = (
        'data-courseware="c-freshman-interactive-html"',
        'data-layout="slide-page"',
        'data-course-id="CW-L04"',
        'data-chapter="4"',
        'data-routines="EX-C04-002"',
        'data-questions="QB-PG-003,QB-SC-009,QB-SC-035,QB-SC-039,QB-TR-013"',
        'data-lesson-variants="two-number-ordering-normalized-io,leap-year-if-else"',
        'data-attribution="Kevin@SUT"',
        '<meta name="author" content="Kevin@SUT">',
        '<meta name="copyright" content="Kevin@SUT">',
        'data-programming-question-id="QB-PG-003"',
        'data-trace-question-id="QB-TR-013"',
        'data-interaction="ask-wait-reveal"',
        "data-code-line",
        "active-code-line",
    )
    for marker in required_markers:
        if marker not in text:
            fail(failures, f"missing CW-L04 marker: {marker}")

    for pattern in EXTERNAL_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            fail(failures, f"external or persistent dependency found: {pattern}")
    for pattern in TEACHER_ONLY_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            fail(failures, f"teacher-only content found: {pattern}")
    for phrase in CW_L02_STUDENT_FORBIDDEN:
        if phrase in text:
            fail(failures, f"student-facing teacher-prep phrase found: {phrase}")

    slides = SLIDE_PATTERN.findall(text)
    section_blocks = SECTION_BLOCK_PATTERN.findall(text)
    if len(slides) != 26:
        fail(failures, f"CW-L04 expected 26 slides, found {len(slides)}")
    if len(section_blocks) != 26:
        fail(failures, f"CW-L04 expected 26 complete section blocks, found {len(section_blocks)}")
    if text.count("<details") != 0:
        fail(failures, "CW-L04 must expose all knowledge and exercises directly")

    validate_embedded_questions(
        text,
        failures,
        ("QB-SC-009", "QB-SC-035", "QB-SC-039"),
        "CW-L04",
    )
    if text.count('data-question-option="') != 12:
        fail(failures, "CW-L04 must expose four options for each choice question")

    programming_source = scan_questions()["QB-PG-003"].text
    source_prompt_match = re.search(
        r"## 题目\s*(.*?)\s*### 输入格式",
        programming_source,
        re.DOTALL,
    )
    source_prompt = (
        normalize_visible_text(source_prompt_match.group(1))
        if source_prompt_match
        else ""
    )
    programming_match = re.search(
        r'<section\b[^>]*data-programming-question-id="QB-PG-003"[^>]*>(.*?)</section>',
        text,
        re.IGNORECASE | re.DOTALL,
    )
    programming_block = (
        normalize_visible_text(programming_match.group(1))
        if programming_match
        else ""
    )
    if not programming_match:
        fail(failures, "CW-L04 must visibly embed QB-PG-003")
    if not source_prompt_match:
        fail(failures, "QB-PG-003 lacks a parseable prompt in the question bank")
    if source_prompt and source_prompt not in programming_block:
        fail(failures, "QB-PG-003 prompt differs from the question bank")
    for marker in ("一个整数年份。", "闰年输出 leap，否则输出 common。", "按公历闰年规则判断。"):
        if marker not in programming_block:
            fail(failures, f"QB-PG-003 visible contract is incomplete: {marker}")

    positive_blocks = "\n".join(
        re.findall(
            r'<pre\b[^>]*class="[^"]*code-block[^"]*"[^>]*>(.*?)</pre>',
            text,
            re.IGNORECASE | re.DOTALL,
        )
    )
    code_text = html.unescape(re.sub(r"<[^>]+>", "", positive_blocks))
    for forbidden, label in (
        (r"\belse\s+if\b", "else if"),
        (r"\bswitch\s*\(", "switch"),
        (r"\bfor\s*\(", "for loop"),
        (r"\bwhile\s*\(", "while loop"),
        (r"\bdo\s*\{", "do loop"),
        (r"\[[^\]]*\]", "array syntax"),
        (r"\?[^:\n]+:", "conditional operator"),
        (r"\breturn\s+1\s*;", "return 1"),
    ):
        if re.search(forbidden, code_text):
            fail(failures, f"CW-L04 positive examples must not introduce {label}")
    if re.search(r"if\s*\(\s*scanf|scanf\s*\([^;]+\)\s*[!=]=", code_text):
        fail(failures, "CW-L04 must not check scanf return values")
    if len(re.findall(r"\b(?:int|void|float|double|char)\s+(?!main\b)\w+\s*\([^;]*\)\s*\{", code_text)) != 0:
        fail(failures, "CW-L04 must not introduce custom functions")

    required_code = (
        'scanf("%f %f", &a, &b);',
        "if (a > b)",
        "t = a;",
        "a = b;",
        "b = t;",
        'printf("%.2f %.2f\\n", a, b);',
        'scanf("%d", &year);',
        "if (year % 400 == 0",
        "|| (year % 4 == 0 && year % 100 != 0))",
        'printf("leap\\n");',
        'printf("common\\n");',
    )
    for marker in required_code:
        if marker not in code_text:
            fail(failures, f"CW-L04 positive program is incomplete: {marker}")

    interaction_counts = (
        ('data-swap-line', 3, "swap steps"),
        ('data-order-step', 6, "ordering execution steps"),
        ('data-order-test="', 3, "ordering tests"),
        ('data-order-error="', 3, "ordering diagnosis cases"),
        ('data-div-year="', 4, "divisibility fixtures"),
        ('data-leap-predict="', 4, "condition fixtures"),
        ('data-branch="', 2, "branch fixtures"),
        ('data-leap-step', 5, "leap-year execution steps"),
        ('data-trace-answer="', 4, "trace answer options"),
        ('data-leap-error="', 3, "leap-year diagnosis cases"),
        ('data-leap-test="', 4, "leap-year tests"),
        ('data-review="', 14, "review questions"),
    )
    for marker, expected_count, label in interaction_counts:
        if marker.endswith('"'):
            actual = text.count(marker)
        else:
            actual = len(re.findall(r"\b" + re.escape(marker) + r"(?:\s|>)", text))
        if actual != expected_count:
            fail(failures, f"CW-L04 expected {expected_count} {label}, found {actual}")

    for fixture in (
        'data-order-test="5,3" data-expected="3.00 5.00"',
        'data-order-test="2,8" data-expected="2.00 8.00"',
        'data-order-test="4,4" data-expected="4.00 4.00"',
        'data-leap-test="2000" data-expected="leap"',
        'data-leap-test="1900" data-expected="common"',
        'data-leap-test="2024" data-expected="leap"',
        'data-leap-test="2023" data-expected="common"',
    ):
        if fixture not in text:
            fail(failures, f"CW-L04 deterministic fixture is missing: {fixture}")

    for marker in (
        "零是假，非零是真",
        "能被400整除",
        "能被4整除且不能被100整除",
        "故意错误示例",
        "本题程序不读取外部输入",
        "x变为6",
        "最后输出9",
    ):
        if marker not in text:
            fail(failures, f"CW-L04 student explanation is incomplete: {marker}")

    for command in (
        "gcc order.c -o order.exe\n.\\order.exe",
        "gcc leap.c -o leap.exe\n.\\leap.exe",
    ):
        if command not in text:
            fail(failures, f"CW-L04 beginner command is missing: {command.splitlines()[0]}")

    check_links(text, path, failures, require_optional_external=False)
    return failures


def validate_cw_l05(path: Path) -> list[str]:
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
    if "overflow:hidden" not in text.replace(" ", ""):
        fail(failures, "slide/page mode must hide page-level overflow")

    required_markers = (
        'data-courseware="c-freshman-interactive-html"',
        'data-layout="slide-page"',
        'data-course-id="CW-L05"',
        'data-chapter="4"',
        'data-routines="EX-C04-008"',
        'data-questions="QB-PG-001,QB-TR-002,QB-TR-007,QB-SC-010"',
        'data-lesson-variants="quadratic-equation-explicit-nested-selection,grade-range-switch"',
        'data-attribution="Kevin@SUT"',
        '<meta name="author" content="Kevin@SUT">',
        '<meta name="copyright" content="Kevin@SUT">',
        'data-programming-question-id="QB-PG-001"',
        'data-trace-question-id="QB-TR-002"',
        'data-trace-question-id="QB-TR-007"',
        'data-positive-program="grade-switch"',
        "data-code-line",
        "active-code-line",
    )
    for marker in required_markers:
        if marker not in text:
            fail(failures, f"missing CW-L05 marker: {marker}")

    for pattern in EXTERNAL_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            fail(failures, f"external or persistent dependency found: {pattern}")
    for pattern in TEACHER_ONLY_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            fail(failures, f"teacher-only content found: {pattern}")
    for phrase in CW_L02_STUDENT_FORBIDDEN:
        if phrase in text:
            fail(failures, f"student-facing teacher-prep phrase found: {phrase}")

    if len(SLIDE_PATTERN.findall(text)) != 26:
        fail(failures, f"CW-L05 expected 26 slides, found {len(SLIDE_PATTERN.findall(text))}")
    if len(SECTION_BLOCK_PATTERN.findall(text)) != 26:
        fail(failures, "CW-L05 must contain 26 complete section blocks")
    if 'data-section="decision-tree"' in text:
        fail(failures, "CW-L05 must not repeat the three-result table as a separate decision-tree page")
    merged_match = re.search(
        r'<section\b[^>]*data-section="quadratic-and-discriminant"[^>]*>(.*?)</section>',
        text,
        re.IGNORECASE | re.DOTALL,
    )
    merged_block = merged_match.group(1) if merged_match else ""
    if 'data-formula="ax^2+bx+c=0"' not in merged_block or 'data-formula="Delta=b^2-4ac"' not in merged_block:
        fail(failures, "CW-L05 page 3 must combine the standard form and discriminant")
    if " / 26 · Kevin@SUT" not in text:
        fail(failures, "CW-L05 footer total must be 26")
    if ".code-block.equation-full{font-size:14.6px" not in text:
        fail(failures, "CW-L05 page 8 must retain the projection-tested 14.6px program font")
    if text.count("<details") != 0:
        fail(failures, "CW-L05 must expose all knowledge and exercises directly")

    validate_embedded_questions(text, failures, ("QB-SC-010",), "CW-L05")
    if text.count('data-question-option="') != 4:
        fail(failures, "CW-L05 must expose four options for QB-SC-010")

    questions = scan_questions()
    pg_source = questions["QB-PG-001"].text
    pg_prompt_match = re.search(r"## 题目\s*(.*?)\s*### 输入格式", pg_source, re.DOTALL)
    pg_block_match = re.search(
        r'<section\b[^>]*data-programming-question-id="QB-PG-001"[^>]*>(.*?)</section>',
        text,
        re.IGNORECASE | re.DOTALL,
    )
    pg_prompt = normalize_visible_text(pg_prompt_match.group(1)) if pg_prompt_match else ""
    pg_block = normalize_visible_text(pg_block_match.group(1)) if pg_block_match else ""
    if not pg_prompt_match or not pg_block_match or pg_prompt not in pg_block:
        fail(failures, "CW-L05 must visibly embed the QB-PG-001 prompt")
    for marker in (
        "三个实数 a b c。",
        "按判别式输出两个实根、重根或共轭复根。",
    ):
        if marker not in pg_block:
            fail(failures, f"QB-PG-001 visible contract is incomplete: {marker}")
    for forbidden in ("数据范围与边界", "|a|>=1e-12"):
        if forbidden in pg_block:
            fail(failures, f"CW-L05 page 2 must not expose confusing boundary text: {forbidden}")

    for question_id, expected_output in (("QB-TR-002", "over!"), ("QB-TR-007", "0")):
        source = questions[question_id].text
        source_code_match = re.search(r"```c\s*(.*?)```", source, re.DOTALL)
        html_block_match = re.search(
            rf'<section\b[^>]*data-trace-question-id="{question_id}"[^>]*>(.*?)</section>',
            text,
            re.IGNORECASE | re.DOTALL,
        )
        if not source_code_match or not html_block_match:
            fail(failures, f"CW-L05 lacks complete trace question {question_id}")
            continue
        source_tokens = re.sub(r"\s+", "", source_code_match.group(1))
        html_code_match = re.search(r'<pre\b[^>]*class="[^"]*trace-code[^"]*"[^>]*>(.*?)</pre>', html_block_match.group(1), re.DOTALL)
        html_tokens = re.sub(r"\s+", "", html.unescape(re.sub(r"<[^>]+>", "", html_code_match.group(1)))) if html_code_match else ""
        if source_tokens != html_tokens:
            fail(failures, f"{question_id} program differs from the question bank")
        if expected_output not in normalize_visible_text(html_block_match.group(1)):
            fail(failures, f"{question_id} expected output is not represented")

    positive_blocks = "\n".join(re.findall(
        r'<pre\b[^>]*class="[^"]*code-block[^"]*"[^>]*>(.*?)</pre>',
        text,
        re.IGNORECASE | re.DOTALL,
    ))
    code_text = html.unescape(re.sub(r"<[^>]+>", "", positive_blocks))
    for forbidden, label in (
        (r"\bfor\s*\(", "for loop"),
        (r"\bwhile\s*\(", "while loop"),
        (r"\bdo\s*\{", "do loop"),
        (r"\[[^\]]*\]", "array syntax"),
        (r"\?[^:\n]+:", "conditional operator"),
        (r"\breturn\s+1\s*;", "return 1"),
    ):
        if re.search(forbidden, code_text):
            fail(failures, f"CW-L05 positive examples must not introduce {label}")
    if re.search(r"if\s*\(\s*scanf|scanf\s*\([^;]+\)\s*[!=]=", code_text):
        fail(failures, "CW-L05 must not check scanf return values")
    if len(re.findall(r"\b(?:int|void|float|double|char)\s+(?!main\b)\w+\s*\([^;]*\)\s*\{", code_text)):
        fail(failures, "CW-L05 must not introduce custom functions")

    equation_program_match = re.search(
        r'<section\b[^>]*data-section="equation-program"[^>]*>(.*?)</section>',
        text,
        re.IGNORECASE | re.DOTALL,
    )
    equation_program = equation_program_match.group(1) if equation_program_match else ""
    equation_code_blocks = re.findall(
        r'<pre\b[^>]*class="[^"]*code-block[^"]*"[^>]*>(.*?)</pre>',
        equation_program,
        re.IGNORECASE | re.DOTALL,
    )
    if len(equation_code_blocks) != 1:
        fail(failures, "CW-L05 page 8 must present the equation as one continuous code block")
    for marker in ("/* 输入、判别式和两个实根 */", "/* 重根、复根和程序结束 */"):
        if marker not in html.unescape(re.sub(r"<[^>]+>", "", equation_program)):
            fail(failures, f"CW-L05 page 8 lacks section comment: {marker}")
    if "program-pair" in equation_program:
        fail(failures, "CW-L05 page 8 must not split the equation program into two panels")

    for marker in (
        'scanf("%lf %lf %lf", &a, &b, &c);',
        "d = b * b - 4.0 * a * c;",
        "if (d > 1e-12)",
        "else if (fabs(d) <= 1e-12)",
        "x1 = (-b + sqrt(d)) / (2.0 * a);",
        "imag_part = sqrt(-d) / fabs(2.0 * a);",
        'scanf("%c", &grade);',
        "switch (grade)",
        "case 'A':",
        "case 'B':",
        "case 'C':",
        "case 'D':",
        "default:",
    ):
        if marker not in code_text:
            fail(failures, f"CW-L05 positive program is incomplete: {marker}")

    grade_program_match = re.search(
        r'<pre\b[^>]*data-positive-program="grade-switch"[^>]*>(.*?)</pre>',
        text,
        re.IGNORECASE | re.DOTALL,
    )
    grade_code = html.unescape(re.sub(r"<[^>]+>", "", grade_program_match.group(1))) if grade_program_match else ""
    if len(re.findall(r"\bcase\s+'[A-D]'\s*:", grade_code)) != 4:
        fail(failures, "CW-L05 grade switch must contain exactly case A-D")
    if len(re.findall(r"\bbreak\s*;", grade_code)) != 4:
        fail(failures, "CW-L05 grade switch must contain four break statements")
    if len(re.findall(r"\bdefault\s*:", grade_code)) != 1:
        fail(failures, "CW-L05 grade switch must contain one default label")

    counts = (
        ('data-equation-input="', 3, "equation stepper inputs"),
        ("data-equation-step", 6, "equation steps"),
        ('data-trace-002="', 4, "QB-TR-002 options"),
        ('data-trace-007="', 4, "QB-TR-007 options"),
        ("data-grade-a-step", 5, "grade A steps"),
        ('data-grade-input="', 3, "grade executor inputs"),
        ('data-fallthrough-step="', 3, "fallthrough steps"),
        ('data-switch-error="', 3, "switch diagnosis cases"),
        ('data-equation-test="', 3, "equation tests"),
        ('data-grade-test="', 5, "grade tests"),
        ('data-review="', 14, "review questions"),
    )
    for marker, expected, label in counts:
        actual = text.count(marker) if marker.endswith('"') else len(re.findall(r"\b" + re.escape(marker) + r"(?:\s|>)", text))
        if actual != expected:
            fail(failures, f"CW-L05 expected {expected} {label}, found {actual}")

    fixtures = (
        'data-equation-test="1 2 1" data-expected="-1.000000"',
        'data-equation-test="1 -3 2" data-expected="2.000000 1.000000"',
        'data-equation-test="1 2 5" data-expected="-1.000000+2.000000i -1.000000-2.000000i"',
        'data-grade-test="A" data-expected="Your score:85～100"',
        'data-grade-test="B" data-expected="Your score:70～84"',
        'data-grade-test="C" data-expected="Your score:60～69"',
        'data-grade-test="D" data-expected="Your score:&lt;60"',
        'data-grade-test="X" data-expected="Your score:enter data error!"',
    )
    for fixture in fixtures:
        if fixture not in text:
            fail(failures, f"CW-L05 deterministic fixture is missing: {fixture}")

    for marker in (
        "判别式对应三种结果",
        "else 与最近且尚未配对的 if 配对",
        "贯穿不是重新进行匹配",
        "以上均为故意错误示例",
        "输入约束：三个系数均符合规定的实数格式。",
    ):
        if marker not in normalize_visible_text(text):
            fail(failures, f"CW-L05 student explanation is incomplete: {marker}")
    for marker in (
        'data-formula="ax^2+bx+c=0"',
        'data-formula="Delta=b^2-4ac"',
        'data-formula="x12=(-b+-sqrt(Delta))/(2a)"',
        'data-formula="x=-b/(2a)"',
        'data-formula="x12=-b/(2a)+-sqrt(-Delta)/abs(2a)i"',
        'class="fraction"',
    ):
        if marker not in text:
            fail(failures, f"CW-L05 mathematical formula markup is incomplete: {marker}")
    if "退化" in normalize_visible_text(text):
        fail(failures, "CW-L05 must not introduce degenerate-equation handling")
    if ".nav-buttons button" not in text or "white-space:nowrap" not in text.replace(" ", ""):
        fail(failures, "CW-L05 navigation buttons must not wrap")
    for command in (
        "gcc equation.c -o equation.exe\n.\\equation.exe",
        "gcc grade.c -o grade.exe\n.\\grade.exe",
    ):
        if command not in text:
            fail(failures, f"CW-L05 beginner command is missing: {command.splitlines()[0]}")

    check_links(text, path, failures, require_optional_external=False)
    return failures


def validate_cw_l06(path: Path) -> list[str]:
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
    if "overflow:hidden" not in text.replace(" ", ""):
        fail(failures, "slide/page mode must hide page-level overflow")

    required_markers = (
        'data-courseware="c-freshman-interactive-html"',
        'data-layout="slide-page"',
        'data-course-id="CW-L06"',
        'data-chapter="5"',
        'data-routines="EX-C05-001,EX-C05-002"',
        'data-questions="QB-PG-006,QB-PG-011,QB-TR-020,QB-SC-032,QB-SC-033"',
        'data-lesson-variants="prime-check-while-state,narcissistic-number-single-for"',
        'data-attribution="Kevin@SUT"',
        '<meta name="author" content="Kevin@SUT">',
        '<meta name="copyright" content="Kevin@SUT">',
        'data-programming-question-id="QB-PG-006"',
        'data-programming-question-id="QB-PG-011"',
        'data-trace-question-id="QB-TR-020"',
        'data-positive-program="prime-while"',
        'data-positive-program="narcissistic-for"',
        "data-code-line",
        "active-code-line",
    )
    for marker in required_markers:
        if marker not in text:
            fail(failures, f"missing CW-L06 marker: {marker}")

    for pattern in EXTERNAL_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            fail(failures, f"external or persistent dependency found: {pattern}")
    for pattern in TEACHER_ONLY_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            fail(failures, f"teacher-only content found: {pattern}")
    for phrase in CW_L02_STUDENT_FORBIDDEN:
        if phrase in text:
            fail(failures, f"student-facing teacher-prep phrase found: {phrase}")

    slides = len(SLIDE_PATTERN.findall(text))
    sections = len(SECTION_BLOCK_PATTERN.findall(text))
    if slides != 28:
        fail(failures, f"CW-L06 expected 28 slides, found {slides}")
    if sections != 28:
        fail(failures, f"CW-L06 expected 28 complete section blocks, found {sections}")
    if text.count("<details") != 0:
        fail(failures, "CW-L06 must expose all knowledge and exercises directly")
    if " / 28 · Kevin@SUT" not in text:
        fail(failures, "CW-L06 footer total must be 28")

    validate_embedded_questions(text, failures, ("QB-SC-032", "QB-SC-033"), "CW-L06")
    if text.count('data-question-option="') != 8:
        fail(failures, "CW-L06 must expose eight options across two choice questions")

    questions = scan_questions()
    for question_id in ("QB-PG-006", "QB-PG-011"):
        source = questions[question_id].text
        prompt_match = re.search(r"## 题目\s*(.*?)\s*### 输入格式", source, re.DOTALL)
        html_match = re.search(
            rf'<section\b[^>]*data-programming-question-id="{question_id}"[^>]*>(.*?)</section>',
            text,
            re.IGNORECASE | re.DOTALL,
        )
        source_prompt = normalize_visible_text(prompt_match.group(1)) if prompt_match else ""
        html_prompt = normalize_visible_text(html_match.group(1)) if html_match else ""
        if not source_prompt or source_prompt not in html_prompt:
            fail(failures, f"CW-L06 must visibly embed the {question_id} prompt")

    trace_source = questions["QB-TR-020"].text
    trace_source_match = re.search(r"```c\s*(.*?)```", trace_source, re.DOTALL)
    trace_html_match = re.search(
        r'<section\b[^>]*data-trace-question-id="QB-TR-020"[^>]*>(.*?)</section>',
        text,
        re.IGNORECASE | re.DOTALL,
    )
    trace_html_code = re.search(
        r'<pre\b[^>]*class="[^"]*trace-code[^"]*"[^>]*>(.*?)</pre>',
        trace_html_match.group(1) if trace_html_match else "",
        re.DOTALL,
    )
    source_tokens = re.sub(r"\s+", "", trace_source_match.group(1)) if trace_source_match else ""
    html_tokens = re.sub(
        r"\s+",
        "",
        html.unescape(re.sub(r"<[^>]+>", "", trace_html_code.group(1))),
    ) if trace_html_code else ""
    if source_tokens != html_tokens:
        fail(failures, "QB-TR-020 program differs from the question bank")
    if "0,9" not in normalize_visible_text(trace_html_match.group(1) if trace_html_match else ""):
        fail(failures, "QB-TR-020 expected output is not represented")
    if 'b.getAttribute("data-trace-020")==="0,9"' not in text:
        fail(failures, "QB-TR-020 correct-answer handler must read the numeric data attribute explicitly")

    for marker in (
        '[data-section="prime-errors"] [data-prime-error] h3',
        '[data-section="narcissistic-errors"] [data-narcissistic-error] h3',
        "color:#5f1f1f",
    ):
        if marker not in text:
            fail(failures, f"CW-L06 diagnosis title contrast rule is missing: {marker}")

    program_blocks = {
        match.group("id"): html.unescape(re.sub(r"<[^>]+>", "", match.group("body")))
        for match in re.finditer(
            r'<pre\b[^>]*data-positive-program="(?P<id>[^"]+)"[^>]*>(?P<body>.*?)</pre>',
            text,
            re.IGNORECASE | re.DOTALL,
        )
    }
    if set(program_blocks) != {"prime-while", "narcissistic-for"}:
        fail(failures, "CW-L06 must contain exactly the two declared positive programs")
    code_text = "\n".join(program_blocks.values())
    for forbidden, label in (
        (r"\[[^\]]*\]", "array syntax"),
        (r"\bbreak\s*;", "break"),
        (r"\bcontinue\s*;", "continue"),
        (r"\bswitch\s*\(", "switch"),
        (r"\bgoto\b", "goto"),
        (r"\?[^:\n]+:", "conditional operator"),
        (r"\breturn\s+1\s*;", "return 1"),
    ):
        if re.search(forbidden, code_text):
            fail(failures, f"CW-L06 positive programs must not introduce {label}")
    if re.search(r"if\s*\(\s*scanf|scanf\s*\([^;]+\)\s*[!=]=", code_text):
        fail(failures, "CW-L06 student programs must not check scanf return values")
    if len(re.findall(r"\b(?:int|void|float|double|char)\s+(?!main\b)\w+\s*\([^;]*\)\s*\{", code_text)):
        fail(failures, "CW-L06 must not introduce custom functions")

    prime_code = program_blocks.get("prime-while", "")
    narcissistic_code = program_blocks.get("narcissistic-for", "")
    if len(re.findall(r"\b(?:while|for|do)\b", prime_code)) != 1:
        fail(failures, "CW-L06 prime program must contain exactly one loop")
    if len(re.findall(r"\b(?:while|for|do)\b", narcissistic_code)) != 1:
        fail(failures, "CW-L06 narcissistic program must contain exactly one loop")
    for marker in (
        "int i = 2;",
        "int is_prime = 1;",
        "if (n < 2)",
        "while (is_prime && i <= n / i)",
        "if (n % i == 0)",
        "i++;",
        'printf("prime\\n");',
        'printf("not prime\\n");',
    ):
        if marker not in prime_code:
            fail(failures, f"CW-L06 prime program is incomplete: {marker}")
    for marker in (
        "for (n = 100; n <= 999; n++)",
        "hundreds = n / 100;",
        "tens = n / 10 % 10;",
        "ones = n % 10;",
        "sum = hundreds * hundreds * hundreds",
        "if (sum == n)",
    ):
        if marker not in narcissistic_code:
            fail(failures, f"CW-L06 narcissistic program is incomplete: {marker}")

    counts = (
        ('data-prime-test="', 5, "prime tests"),
        ('data-prime-case="', 4, "prime alternate inputs"),
        ('data-prime-error="', 4, "prime diagnosis cases"),
        ('data-candidate="', 3, "candidate checks"),
        ('data-narcissistic-error="', 4, "narcissistic diagnosis cases"),
        ('data-review="', 14, "review questions"),
    )
    for marker, expected, label in counts:
        actual = text.count(marker)
        if actual != expected:
            fail(failures, f"CW-L06 expected {expected} {label}, found {actual}")
    for fixture in (
        'data-prime-test="17" data-expected="prime"',
        'data-prime-test="21" data-expected="not prime"',
        'data-prime-test="2" data-expected="prime"',
        'data-prime-test="1" data-expected="not prime"',
        'data-prime-test="49" data-expected="not prime"',
        'data-narcissistic-test data-expected="153|370|371|407"',
    ):
        if fixture not in text:
            fail(failures, f"CW-L06 deterministic fixture is missing: {fixture}")

    for marker in (
        "初始化、条件、循环体和更新",
        "循环有两种结束原因",
        "先输出5",
        "^是按位异或运算符",
        "循环范围是闭区间",
    ):
        if marker not in normalize_visible_text(text):
            fail(failures, f"CW-L06 student explanation is incomplete: {marker}")
    if "浏览器进行确定性" not in text:
        fail(failures, "CW-L06 must disclose that browser execution is simulated")
    for command in (
        "gcc prime.c -o prime.exe\n.\\prime.exe",
        "gcc narcissistic.c -o narcissistic.exe\n.\\narcissistic.exe",
    ):
        if command not in text:
            fail(failures, f"CW-L06 beginner command is missing: {command.splitlines()[0]}")

    check_links(text, path, failures, require_optional_external=False)
    return failures


def validate_cw_l07(path: Path) -> list[str]:
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
    if "overflow:hidden" not in text.replace(" ", ""):
        fail(failures, "slide/page mode must hide page-level overflow")

    required_markers = (
        'data-courseware="c-freshman-interactive-html"',
        'data-layout="slide-page"',
        'data-course-id="CW-L07"',
        'data-chapter="5"',
        'data-routines="EX-C05-007"',
        'data-questions="QB-PG-009,QB-FB-012,QB-SC-011,QB-SC-057"',
        'data-lesson-variants="four-by-five-product-table,interval-primes-nested-break"',
        'data-attribution="Kevin@SUT"',
        '<meta name="author" content="Kevin@SUT">',
        '<meta name="copyright" content="Kevin@SUT">',
        'data-positive-program="product-table"',
        'data-positive-program="interval-primes"',
        'data-programming-question-id="QB-PG-009"',
        'data-fill-question-id="QB-FB-012"',
        "data-code-line",
        "active-code-line",
    )
    for marker in required_markers:
        if marker not in text:
            fail(failures, f"missing CW-L07 marker: {marker}")

    for pattern in EXTERNAL_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            fail(failures, f"external or persistent dependency found: {pattern}")
    for pattern in TEACHER_ONLY_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            fail(failures, f"teacher-only content found: {pattern}")
    for phrase in CW_L02_STUDENT_FORBIDDEN:
        if phrase in text:
            fail(failures, f"student-facing teacher-prep phrase found: {phrase}")

    slides = len(SLIDE_PATTERN.findall(text))
    sections = len(SECTION_BLOCK_PATTERN.findall(text))
    if slides != 30:
        fail(failures, f"CW-L07 expected 30 slides, found {slides}")
    if sections != 30:
        fail(failures, f"CW-L07 expected 30 complete section blocks, found {sections}")
    if text.count("<details") != 0:
        fail(failures, "CW-L07 must expose all knowledge and exercises directly")
    if " / 30 · Kevin@SUT" not in text:
        fail(failures, "CW-L07 footer total must be 30")

    validate_embedded_questions(text, failures, ("QB-SC-011", "QB-SC-057"), "CW-L07")
    if text.count('data-question-option="') != 8:
        fail(failures, "CW-L07 must expose eight options across two choice questions")

    questions = scan_questions()
    source = questions["QB-PG-009"].text
    prompt_match = re.search(r"## 题目\s*(.*?)\s*### 输入格式", source, re.DOTALL)
    html_match = re.search(
        r'<section\b[^>]*data-programming-question-id="QB-PG-009"[^>]*>(.*?)</section>',
        text,
        re.IGNORECASE | re.DOTALL,
    )
    source_prompt = normalize_visible_text(prompt_match.group(1)) if prompt_match else ""
    html_prompt = normalize_visible_text(html_match.group(1)) if html_match else ""
    if not source_prompt or source_prompt not in html_prompt:
        fail(failures, "CW-L07 must visibly embed the QB-PG-009 prompt")

    fill_source = questions["QB-FB-012"].text
    fill_source_body = re.search(
        r"## 题目\s*(?P<prompt>.*?)\x60\x60\x60c\s*(?P<code>.*?)\x60\x60\x60",
        fill_source,
        re.DOTALL,
    )
    fill_html = re.search(
        r'<section\b[^>]*data-fill-question-id="QB-FB-012"[^>]*>(.*?)</section>',
        text,
        re.IGNORECASE | re.DOTALL,
    )
    fill_html_prompt = re.search(
        r'<p\b[^>]*class="[^"]*question-text[^"]*"[^>]*>(.*?)</p>',
        fill_html.group(1) if fill_html else "",
        re.DOTALL,
    )
    fill_html_code = re.search(
        r'<pre\b[^>]*class="[^"]*trace-code[^"]*"[^>]*>(.*?)</pre>',
        fill_html.group(1) if fill_html else "",
        re.DOTALL,
    )
    source_fill_prompt = normalize_visible_text(fill_source_body.group("prompt")) if fill_source_body else ""
    actual_fill_prompt = normalize_visible_text(fill_html_prompt.group(1)) if fill_html_prompt else ""
    if source_fill_prompt != actual_fill_prompt:
        fail(failures, "QB-FB-012 prompt differs from the question bank")
    source_fill_tokens = re.sub(r"\s+", "", fill_source_body.group("code")) if fill_source_body else ""
    actual_fill_tokens = re.sub(
        r"\s+",
        "",
        html.unescape(re.sub(r"<[^>]+>", "", fill_html_code.group(1))),
    ) if fill_html_code else ""
    if source_fill_tokens != actual_fill_tokens:
        fail(failures, "QB-FB-012 program differs from the question bank")
    if text.count('data-fill="') != 4:
        fail(failures, "QB-FB-012 must expose four fill-answer controls")
    if "逐空答案" in normalize_visible_text(text):
        fail(failures, "QB-FB-012 answers must remain hidden until a reveal button is clicked")
    for answer in ("n&lt;=200", "i*i&lt;=n", "n%i==0", "if(prime)"):
        if f'data-answer="{answer}"' not in text:
            fail(failures, f"QB-FB-012 answer is missing: {answer}")

    program_blocks = {
        match.group("id"): html.unescape(re.sub(r"<[^>]+>", "", match.group("body")))
        for match in re.finditer(
            r'<pre\b[^>]*data-positive-program="(?P<id>[^"]+)"[^>]*>(?P<body>.*?)</pre>',
            text,
            re.IGNORECASE | re.DOTALL,
        )
    }
    if set(program_blocks) != {"product-table", "interval-primes"}:
        fail(failures, "CW-L07 must contain exactly the two declared positive programs")

    validate_cw_l07_programs(text, program_blocks, failures)
    check_links(text, path, failures, require_optional_external=False)
    return failures


def loop_nesting_depth(code: str) -> int:
    """Return the maximum braced loop nesting depth in formatted C code."""
    stripped = re.sub(r"/\*.*?\*/|//[^\n]*", "", code, flags=re.DOTALL)
    stack: list[bool] = []
    pending_loop = False
    depth = 0
    maximum = 0
    for token in re.findall(r"\b(?:for|while|do)\b|[{}]", stripped):
        if token in {"for", "while", "do"}:
            pending_loop = True
        elif token == "{":
            stack.append(pending_loop)
            if pending_loop:
                depth += 1
                maximum = max(maximum, depth)
            pending_loop = False
        elif token == "}" and stack:
            if stack.pop():
                depth -= 1
    return maximum


def validate_cw_l07_programs(
    text: str,
    program_blocks: dict[str, str],
    failures: list[str],
) -> None:
    code_text = "\n".join(program_blocks.values())
    for forbidden, label in (
        (r"\[[^\]]*\]", "array syntax"),
        (r"\bswitch\s*\(", "switch"),
        (r"\bgoto\b", "goto"),
        (r"\?[^:\n]+:", "conditional operator"),
        (r"\breturn\s+1\s*;", "return 1"),
    ):
        if re.search(forbidden, code_text):
            fail(failures, f"CW-L07 positive programs must not introduce {label}")
    if re.search(r"if\s*\(\s*scanf|scanf\s*\([^;]+\)\s*[!=]=", code_text):
        fail(failures, "CW-L07 student programs must not check scanf return values")
    if len(re.findall(r"\b(?:int|void|float|double|char)\s+(?!main\b)\w+\s*\([^;]*\)\s*\{", code_text)):
        fail(failures, "CW-L07 must not introduce custom functions")
    for program_id, code in program_blocks.items():
        if loop_nesting_depth(code) != 2:
            fail(failures, f"CW-L07 {program_id} must have loop nesting depth exactly two")

    table_code = program_blocks.get("product-table", "")
    for marker in (
        "for (i = 1; i <= 4; i++)",
        "for (j = 1; j <= 5; j++)",
        'printf("%4d", i * j);',
        'printf("\\n");',
    ):
        if marker not in table_code:
            fail(failures, f"CW-L07 product-table program is incomplete: {marker}")
    prime_code = program_blocks.get("interval-primes", "")
    for marker in (
        "for (n = 100; n <= 200; n++)",
        "is_prime = 1;",
        "for (i = 2; i <= n / i; i++)",
        "if (n % i == 0)",
        "is_prime = 0;",
        "break;",
        "if (count % 5 != 0)",
        "if (count % 5 == 0)",
    ):
        if marker not in prime_code:
            fail(failures, f"CW-L07 interval-primes program is incomplete: {marker}")
    if prime_code.count("break;") != 1:
        fail(failures, "CW-L07 prime program must use one explicit inner-loop break")
    if "continue;" in code_text:
        fail(failures, "CW-L07 positive programs must keep continue in the marked demonstration only")

    exact_product = "   1   2   3   4   5\n   2   4   6   8  10\n   3   6   9  12  15\n   4   8  12  16  20"
    exact_primes = "101 103 107 109 113\n127 131 137 139 149\n151 157 163 167 173\n179 181 191 193 197\n199"
    if text.count(exact_product) < 2:
        fail(failures, "CW-L07 product-table exact output must appear in task and review")
    if text.count(exact_primes) < 2:
        fail(failures, "CW-L07 interval-primes exact output must appear in task and review")
    visible = normalize_visible_text(text)
    for marker in (
        'data-prime-count="21"',
        'data-line-distribution="5,5,5,5,1"',
        "内层初始化",
        "4 × 5 = 20",
        "只结束直接包围它的内层循环",
        "每个候选数开始时",
        "浏览器进行确定性",
    ):
        if marker not in text and marker not in visible:
            fail(failures, f"CW-L07 student explanation is incomplete: {marker}")

    counts = (
        ('data-state-row="', 3, "product state-row controls"),
        ('data-break-row="', 2, "break demonstrations"),
        ('data-continue-demo="', 2, "continue demonstrations"),
        ('data-pair="', 4, "prime state-pair controls"),
        ('data-prime-candidate="', 3, "prime candidate controls"),
        ('data-prime-error="', 4, "prime diagnosis cases"),
        ("data-review ", 14, "review questions"),
    )
    for marker, expected, label in counts:
        actual = text.count(marker)
        if actual != expected:
            fail(failures, f"CW-L07 expected {expected} {label}, found {actual}")
    for command in (
        "gcc table.c -o table.exe\n.\\table.exe",
        "gcc primes.c -o primes.exe\n.\\primes.exe",
    ):
        if command not in text:
            fail(failures, f"CW-L07 beginner command is missing: {command.splitlines()[0]}")
    compile_cw_l07_programs(program_blocks, failures, exact_product, exact_primes)


def compile_cw_l07_programs(
    program_blocks: dict[str, str],
    failures: list[str],
    exact_product: str,
    exact_primes: str,
) -> None:
    gcc = shutil.which("gcc")
    if not gcc:
        fail(failures, "CW-L07 MinGW GCC was not found")
        return
    machine = subprocess.run(
        [gcc, "-dumpmachine"],
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        check=False,
    )
    if machine.returncode != 0 or "mingw" not in machine.stdout.lower():
        fail(failures, f"CW-L07 compiler is not MinGW GCC: {machine.stdout.strip()}")
        return

    fixtures = {
        "product-table": exact_product + "\n",
        "interval-primes": exact_primes + "\n",
    }
    with tempfile.TemporaryDirectory(prefix="cw-l07-validation-") as temp_name:
        temp_dir = Path(temp_name)
        for program_id, expected in fixtures.items():
            source = temp_dir / f"{program_id}.c"
            executable = temp_dir / f"{program_id}.exe"
            source.write_text(program_blocks[program_id], encoding="utf-8", newline="\n")
            build = subprocess.run(
                [
                    gcc,
                    "-std=c11",
                    "-Wall",
                    "-Wextra",
                    "-Wpedantic",
                    "-Werror",
                    str(source),
                    "-o",
                    str(executable),
                ],
                text=True,
                encoding="utf-8",
                errors="replace",
                capture_output=True,
                check=False,
            )
            if build.returncode != 0:
                fail(failures, f"CW-L07 {program_id} compile failed: {build.stderr.strip()}")
                continue
            run_result = subprocess.run(
                [str(executable)],
                text=True,
                encoding="utf-8",
                errors="replace",
                capture_output=True,
                check=False,
                timeout=10,
            )
            actual = run_result.stdout.replace("\r\n", "\n")
            if run_result.returncode != 0 or actual != expected:
                fail(
                    failures,
                    f"CW-L07 {program_id} output mismatch: "
                    f"exit={run_result.returncode}, actual={actual!r}",
                )


def validate_cw_l08(path: Path) -> list[str]:
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
    required = (
        'data-course-id="CW-L08"',
        'data-chapter="6"',
        'data-routines="EX-C06-001,EX-C06-003"',
        'data-questions="QB-PG-002,QB-PG-004,QB-SC-012,QB-SC-013,QB-SC-042,QB-TR-005"',
        'data-lesson-variants="array-maximum-fixed-ten,bubble-sort-fixed-ten"',
        'data-positive-program="array-maximum"',
        'data-positive-program="bubble-sort"',
        'data-programming-question-id="QB-PG-002"',
        'data-programming-question-id="QB-PG-004"',
        'data-trace-question-id="QB-TR-005"',
        '<meta name="author" content="Kevin@SUT">',
        'data-attribution="Kevin@SUT"',
        "data-code-line",
    )
    for marker in required:
        if marker not in text:
            fail(failures, f"missing CW-L08 marker: {marker}")
    for pattern in EXTERNAL_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            fail(failures, f"external or persistent dependency found: {pattern}")
    for pattern in TEACHER_ONLY_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            fail(failures, f"teacher-only content found: {pattern}")
    for phrase in CW_L02_STUDENT_FORBIDDEN:
        if phrase in text:
            fail(failures, f"student-facing teacher-prep phrase found: {phrase}")

    if len(SLIDE_PATTERN.findall(text)) != 30:
        fail(failures, "CW-L08 must contain exactly 30 slides")
    if len(SECTION_BLOCK_PATTERN.findall(text)) != 30:
        fail(failures, "CW-L08 must contain exactly 30 complete slide sections")
    if text.count("<details") != 0:
        fail(failures, "CW-L08 must expose all exercises directly")
    if " / 30 · Kevin@SUT" not in text:
        fail(failures, "CW-L08 footer total must be 30")

    validate_embedded_questions(
        text,
        failures,
        ("QB-SC-012", "QB-SC-013", "QB-SC-042"),
        "CW-L08",
    )
    if text.count('data-question-option="') != 12:
        fail(failures, "CW-L08 must expose twelve options across three choice questions")

    questions = scan_questions()
    for question_id in ("QB-PG-002", "QB-PG-004"):
        source = questions[question_id].text
        prompt_match = re.search(r"## 题目\s*(.*?)\s*### 输入格式", source, re.DOTALL)
        html_match = re.search(
            rf'<section\b[^>]*data-programming-question-id="{question_id}"[^>]*>(.*?)</section>',
            text,
            re.IGNORECASE | re.DOTALL,
        )
        source_prompt = normalize_visible_text(prompt_match.group(1)) if prompt_match else ""
        html_prompt = normalize_visible_text(html_match.group(1)) if html_match else ""
        if not source_prompt or source_prompt not in html_prompt:
            fail(failures, f"CW-L08 must visibly embed the {question_id} prompt")

    trace_source = questions["QB-TR-005"].text
    trace_code = re.search(r"```c\s*(.*?)```", trace_source, re.DOTALL)
    trace_html = re.search(
        r'<section\b[^>]*data-trace-question-id="QB-TR-005"[^>]*>(.*?)</section>',
        text,
        re.IGNORECASE | re.DOTALL,
    )
    trace_html_code = re.search(
        r'<pre\b[^>]*class="[^"]*trace-code[^"]*"[^>]*>(.*?)</pre>',
        trace_html.group(1) if trace_html else "",
        re.DOTALL,
    )
    source_tokens = re.sub(r"\s+", "", trace_code.group(1)) if trace_code else ""
    html_tokens = re.sub(
        r"\s+",
        "",
        html.unescape(re.sub(r"<[^>]+>", "", trace_html_code.group(1))),
    ) if trace_html_code else ""
    if source_tokens != html_tokens:
        fail(failures, "QB-TR-005 program differs from the question bank")

    program_blocks = {
        match.group("id"): html.unescape(re.sub(r"<[^>]+>", "", match.group("body")))
        for match in re.finditer(
            r'<pre\b[^>]*data-positive-program="(?P<id>[^"]+)"[^>]*>(?P<body>.*?)</pre>',
            text,
            re.IGNORECASE | re.DOTALL,
        )
    }
    if set(program_blocks) != {"array-maximum", "bubble-sort"}:
        fail(failures, "CW-L08 must contain exactly the two declared positive programs")
    validate_cw_l08_programs(text, program_blocks, failures)
    check_links(text, path, failures, require_optional_external=False)
    return failures


def validate_cw_l08_programs(
    text: str,
    program_blocks: dict[str, str],
    failures: list[str],
) -> None:
    code_text = "\n".join(program_blocks.values())
    for forbidden, label in (
        (r"\[[^\]]*\]\s*\[", "two-dimensional array syntax"),
        (r"\bchar\s+\w+\s*\[", "character array"),
        (r"#include\s*<string\.h>", "string library"),
        (r"\b(?:strlen|strcpy|strcmp|strcat)\s*\(", "string function"),
        (r"\b(?:int|double|float|char)\s*\*+\s*\w+", "pointer declaration"),
        (r"\breturn\s+1\s*;", "return 1"),
        (r"\?[^:\n]+:", "conditional operator"),
    ):
        if re.search(forbidden, code_text):
            fail(failures, f"CW-L08 positive programs must not introduce {label}")
    if re.search(r"if\s*\(\s*scanf|scanf\s*\([^;]+\)\s*[!=]=", code_text):
        fail(failures, "CW-L08 student programs must not check scanf return values")
    if len(re.findall(r"\b(?:int|void|float|double|char)\s+(?!main\b)\w+\s*\([^;]*\)\s*\{", code_text)):
        fail(failures, "CW-L08 must not introduce custom functions")

    maximum = program_blocks.get("array-maximum", "")
    bubble = program_blocks.get("bubble-sort", "")
    if loop_nesting_depth(maximum) != 1:
        fail(failures, "CW-L08 maximum program must have loop nesting depth one")
    if loop_nesting_depth(bubble) != 2:
        fail(failures, "CW-L08 bubble program must have loop nesting depth two")
    for marker in (
        "double a[10];",
        "maximum = a[0];",
        "for (i = 1; i < 10; i++)",
        "if (a[i] > maximum)",
        'printf("%.6f\\n", maximum);',
    ):
        if marker not in maximum:
            fail(failures, f"CW-L08 maximum program is incomplete: {marker}")
    for marker in (
        "int a[10];",
        "for (j = 0; j < 9; j++)",
        "for (i = 0; i < 9 - j; i++)",
        "if (a[i] > a[i + 1])",
        "t = a[i];",
        "a[i] = a[i + 1];",
        "a[i + 1] = t;",
    ):
        if marker not in bubble:
            fail(failures, f"CW-L08 bubble program is incomplete: {marker}")

    visible = normalize_visible_text(text)
    for marker in (
        "有效下标是0至9",
        "maximum = a[0]",
        "全为负数",
        "a[i + 1]",
        "i < 9 - j",
        "9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 45",
        "浏览器进行确定性预演",
    ):
        if marker not in text and marker not in visible:
            fail(failures, f"CW-L08 student explanation is incomplete: {marker}")
    counts = (
        ('data-index="', 3, "index checks"),
        ('data-neighbor="', 2, "neighbor demonstrations"),
        ('data-max-case="', 2, "maximum cases"),
        ('data-pair="', 3, "adjacent comparisons"),
        ('data-equal="', 3, "duplicate comparisons"),
        ('data-error="', 4, "bubble diagnosis cases"),
        ('data-test="', 3, "bubble behavior tests"),
        ("data-review ", 14, "review questions"),
    )
    for marker, expected, label in counts:
        actual = text.count(marker)
        if actual != expected:
            fail(failures, f"CW-L08 expected {expected} {label}, found {actual}")
    for command in (
        "gcc maximum.c -o maximum.exe\n.\\maximum.exe",
        "gcc bubble.c -o bubble.exe\n.\\bubble.exe",
    ):
        if command not in text:
            fail(failures, f"CW-L08 beginner command is missing: {command.splitlines()[0]}")
    compile_cw_l08_programs(program_blocks, failures)


def compile_cw_l08_programs(
    program_blocks: dict[str, str],
    failures: list[str],
) -> None:
    gcc = shutil.which("gcc")
    if not gcc:
        fail(failures, "CW-L08 MinGW GCC was not found")
        return
    machine = subprocess.run(
        [gcc, "-dumpmachine"],
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        check=False,
    )
    if machine.returncode != 0 or "mingw" not in machine.stdout.lower():
        fail(failures, f"CW-L08 compiler is not MinGW GCC: {machine.stdout.strip()}")
        return
    fixtures = {
        "array-maximum": (
            ("1 2 3 4 5 6 7 8 9 10\n", "10.000000\n"),
            ("-8.5 -2 -3 -4 -5 -6 -7 -8 -9 -10\n", "-2.000000\n"),
            ("9.5 1 9.5 3 2 8 7 6 5 4\n", "9.500000\n"),
        ),
        "bubble-sort": (
            ("10 9 8 7 6 5 4 3 2 1\n", "1 2 3 4 5 6 7 8 9 10\n"),
            ("1 2 3 4 5 6 7 8 9 10\n", "1 2 3 4 5 6 7 8 9 10\n"),
            ("3 1 3 2 0 -1 2 3 1 0\n", "-1 0 0 1 1 2 2 3 3 3\n"),
        ),
    }
    with tempfile.TemporaryDirectory(prefix="cw-l08-validation-") as temp_name:
        temp_dir = Path(temp_name)
        for program_id, cases in fixtures.items():
            source = temp_dir / f"{program_id}.c"
            executable = temp_dir / f"{program_id}.exe"
            source.write_text(program_blocks[program_id], encoding="utf-8", newline="\n")
            build = subprocess.run(
                [gcc, "-std=c11", "-Wall", "-Wextra", "-Wpedantic", "-Werror", str(source), "-o", str(executable)],
                text=True,
                encoding="utf-8",
                errors="replace",
                capture_output=True,
                check=False,
            )
            if build.returncode != 0:
                fail(failures, f"CW-L08 {program_id} compile failed: {build.stderr.strip()}")
                continue
            for stdin_text, expected in cases:
                result = subprocess.run(
                    [str(executable)],
                    input=stdin_text,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                    capture_output=True,
                    check=False,
                    timeout=10,
                )
                actual = result.stdout.replace("\r\n", "\n")
                if result.returncode != 0 or actual != expected:
                    fail(
                        failures,
                        f"CW-L08 {program_id} output mismatch: exit={result.returncode}, actual={actual!r}",
                    )


def validate_cw_l09(path: Path) -> list[str]:
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
    required = (
        'data-course-id="CW-L09"',
        'data-chapter="6"',
        'data-routines="EX-C06-005,EX-C06-006"',
        'data-questions="QB-PG-008,QB-PG-010,QB-TR-029,QB-SC-014,QB-SC-052,QB-SC-015,QB-SC-016,QB-SC-061"',
        'data-lesson-variants="selection-sort-fixed-ten,matrix-maximum-three-by-four,string-terminator-basics"',
        'data-positive-program="selection-sort"',
        'data-positive-program="matrix-maximum"',
        'data-programming-question-id="QB-PG-008"',
        'data-programming-question-id="QB-PG-010"',
        'data-trace-question-id="QB-TR-029"',
        'data-string-snippet',
        '<meta name="author" content="Kevin@SUT">',
        'data-attribution="Kevin@SUT"',
    )
    for marker in required:
        if marker not in text:
            fail(failures, f"missing CW-L09 marker: {marker}")
    for pattern in EXTERNAL_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            fail(failures, f"external or persistent dependency found: {pattern}")
    for pattern in TEACHER_ONLY_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            fail(failures, f"teacher-only content found: {pattern}")
    for phrase in CW_L02_STUDENT_FORBIDDEN:
        if phrase in text:
            fail(failures, f"student-facing teacher-prep phrase found: {phrase}")

    if len(SLIDE_PATTERN.findall(text)) != 34:
        fail(failures, "CW-L09 must contain exactly 34 slides")
    if len(SECTION_BLOCK_PATTERN.findall(text)) != 34:
        fail(failures, "CW-L09 must contain exactly 34 complete slide sections")
    if text.count("<details") != 0:
        fail(failures, "CW-L09 must expose all exercises directly")
    if " / 34 · Kevin@SUT" not in text:
        fail(failures, "CW-L09 footer total must be 34")

    validate_embedded_questions(
        text,
        failures,
        ("QB-SC-014", "QB-SC-052", "QB-SC-015", "QB-SC-016", "QB-SC-061"),
        "CW-L09",
    )
    if text.count('data-question-option="') != 20:
        fail(failures, "CW-L09 must expose twenty options across five choice questions")

    questions = scan_questions()
    for question_id in ("QB-PG-008", "QB-PG-010"):
        source = questions[question_id].text
        prompt_match = re.search(r"## 题目\s*(.*?)\s*### 输入格式", source, re.DOTALL)
        html_match = re.search(
            rf'<section\b[^>]*data-programming-question-id="{question_id}"[^>]*>(.*?)</section>',
            text,
            re.IGNORECASE | re.DOTALL,
        )
        source_prompt = normalize_visible_text(prompt_match.group(1)) if prompt_match else ""
        html_prompt = normalize_visible_text(html_match.group(1)) if html_match else ""
        if not source_prompt or source_prompt not in html_prompt:
            fail(failures, f"CW-L09 must visibly embed the {question_id} prompt")

    trace_source = questions["QB-TR-029"].text
    trace_code = re.search(r"```c\s*(.*?)```", trace_source, re.DOTALL)
    trace_html = re.search(
        r'<section\b[^>]*data-trace-question-id="QB-TR-029"[^>]*>(.*?)</section>',
        text,
        re.IGNORECASE | re.DOTALL,
    )
    trace_html_code = re.search(
        r'<pre\b[^>]*class="[^"]*trace-code[^"]*"[^>]*>(.*?)</pre>',
        trace_html.group(1) if trace_html else "",
        re.DOTALL,
    )
    source_tokens = re.sub(r"\s+", "", trace_code.group(1)) if trace_code else ""
    html_tokens = re.sub(
        r"\s+",
        "",
        html.unescape(re.sub(r"<[^>]+>", "", trace_html_code.group(1))),
    ) if trace_html_code else ""
    if source_tokens != html_tokens:
        fail(failures, "QB-TR-029 program differs from the question bank")

    program_blocks = {
        match.group("id"): html.unescape(re.sub(r"<[^>]+>", "", match.group("body")))
        for match in re.finditer(
            r'<pre\b[^>]*data-positive-program="(?P<id>[^"]+)"[^>]*>(?P<body>.*?)</pre>',
            text,
            re.IGNORECASE | re.DOTALL,
        )
    }
    if set(program_blocks) != {"selection-sort", "matrix-maximum"}:
        fail(failures, "CW-L09 must contain exactly the two declared positive programs")
    validate_cw_l09_programs(text, program_blocks, failures)
    check_links(text, path, failures, require_optional_external=False)
    return failures


def validate_cw_l09_programs(
    text: str,
    program_blocks: dict[str, str],
    failures: list[str],
) -> None:
    code_text = "\n".join(program_blocks.values())
    for forbidden, label in (
        (r"#include\s*<string\.h>", "string library"),
        (r"\b(?:strlen|strcpy|strcmp|strcat|gets|fgets)\s*\(", "string function or input"),
        (r"\b(?:int|double|float|char)\s*\*+\s*\w+", "pointer declaration"),
        (r"\breturn\s+1\s*;", "return 1"),
        (r"\?[^:\n]+:", "conditional operator"),
    ):
        if re.search(forbidden, code_text):
            fail(failures, f"CW-L09 positive programs must not introduce {label}")
    if re.search(r"if\s*\(\s*scanf|scanf\s*\([^;]+\)\s*[!=]=", code_text):
        fail(failures, "CW-L09 student programs must not check scanf return values")
    if len(re.findall(r"\b(?:int|void|float|double|char)\s+(?!main\b)\w+\s*\([^;]*\)\s*\{", code_text)):
        fail(failures, "CW-L09 must not introduce custom functions")

    selection = program_blocks.get("selection-sort", "")
    matrix = program_blocks.get("matrix-maximum", "")
    if loop_nesting_depth(selection) != 2:
        fail(failures, "CW-L09 selection program must have loop nesting depth two")
    if loop_nesting_depth(matrix) != 2:
        fail(failures, "CW-L09 matrix program must have loop nesting depth two")
    for marker in (
        "int a[10];", "k = i;", "for (j = i + 1; j < 10; j++)",
        "if (a[j] < a[k])", "k = j;", "t = a[i];", "a[i] = a[k];", "a[k] = t;",
    ):
        if marker not in selection:
            fail(failures, f"CW-L09 selection program is incomplete: {marker}")
    for marker in (
        "int a[3][4];", "maximum = a[0][0];", "row = 0;", "column = 0;",
        "if (a[i][j] > maximum)", "maximum = a[i][j];", "row = i;", "column = j;",
    ):
        if marker not in matrix:
            fail(failures, f"CW-L09 matrix program is incomplete: {marker}")

    visible = normalize_visible_text(text)
    for marker in (
        "9 + 8 + 7 + … + 1 = 45", "行下标", "列下标", "全负矩阵",
        "C字符串必须以空字符 \\0 结束", "\\n表示换行", "\\0表示字符串结束",
        "while (s[i] != '\\0')", "浏览器进行确定性预演",
    ):
        if marker not in text and marker not in visible:
            fail(failures, f"CW-L09 student explanation is incomplete: {marker}")
    counts = (
        ('data-selection-error="', 4, "selection diagnosis cases"),
        ('data-matrix-cell="', 3, "matrix cell demonstrations"),
        ('data-matrix-case="', 3, "matrix behavior cases"),
        ('data-matrix-error="', 4, "matrix diagnosis cases"),
        ("data-review ", 21, "review questions"),
    )
    for marker, expected, label in counts:
        actual = text.count(marker)
        if actual != expected:
            fail(failures, f"CW-L09 expected {expected} {label}, found {actual}")
    for command in (
        "gcc selection.c -o selection.exe\n.\\selection.exe",
        "gcc matrix_max.c -o matrix_max.exe\n.\\matrix_max.exe",
    ):
        if command not in text:
            fail(failures, f"CW-L09 beginner command is missing: {command.splitlines()[0]}")
    compile_cw_l09_programs(program_blocks, failures)


def compile_cw_l09_programs(
    program_blocks: dict[str, str],
    failures: list[str],
) -> None:
    gcc = shutil.which("gcc")
    if not gcc:
        fail(failures, "CW-L09 MinGW GCC was not found")
        return
    machine = subprocess.run(
        [gcc, "-dumpmachine"], text=True, encoding="utf-8", errors="replace",
        capture_output=True, check=False,
    )
    if machine.returncode != 0 or "mingw" not in machine.stdout.lower():
        fail(failures, f"CW-L09 compiler is not MinGW GCC: {machine.stdout.strip()}")
        return
    fixtures = {
        "selection-sort": (
            ("10 9 8 7 6 5 4 3 2 1\n", "1 2 3 4 5 6 7 8 9 10\n"),
            ("1 2 3 4 5 6 7 8 9 10\n", "1 2 3 4 5 6 7 8 9 10\n"),
            ("3 1 3 2 0 -1 2 3 1 0\n", "-1 0 0 1 1 2 2 3 3 3\n"),
        ),
        "matrix-maximum": (
            ("1 2 3 4 5 6 20 8 9 10 11 12\n", "20 1 2\n"),
            ("5 5 5 5 5 5 5 5 5 5 5 5\n", "5 0 0\n"),
            ("-1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12\n", "-1 0 0\n"),
        ),
    }
    with tempfile.TemporaryDirectory(prefix="cw-l09-validation-") as temp_name:
        temp_dir = Path(temp_name)
        for program_id, cases in fixtures.items():
            source = temp_dir / f"{program_id}.c"
            executable = temp_dir / f"{program_id}.exe"
            source.write_text(program_blocks[program_id], encoding="utf-8", newline="\n")
            build = subprocess.run(
                [gcc, "-std=c11", "-Wall", "-Wextra", "-Wpedantic", "-Werror", str(source), "-o", str(executable)],
                text=True, encoding="utf-8", errors="replace", capture_output=True, check=False,
            )
            if build.returncode != 0:
                fail(failures, f"CW-L09 {program_id} compile failed: {build.stderr.strip()}")
                continue
            for stdin_text, expected in cases:
                result = subprocess.run(
                    [str(executable)], input=stdin_text, text=True, encoding="utf-8",
                    errors="replace", capture_output=True, check=False, timeout=10,
                )
                actual = result.stdout.replace("\r\n", "\n")
                if result.returncode != 0 or actual != expected:
                    fail(failures, f"CW-L09 {program_id} output mismatch: exit={result.returncode}, actual={actual!r}")


def validate_cw_l10(path: Path) -> list[str]:
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
    required = (
        'data-course-id="CW-L10"',
        'data-chapter="7"',
        'data-routines="EX-C07-002,EX-C07-012"',
        'data-questions="QB-PG-013,QB-FB-003,QB-FB-013,QB-SC-019,QB-SC-044,QB-TF-004,QB-TF-005"',
        'data-lesson-variants="scalar-max-value-parameters,float-array-sort-function"',
        'data-positive-program="scalar-maximum"',
        'data-positive-program="float-array-sort"',
        'data-programming-question-id="QB-PG-013"',
        'data-fill-question-id="QB-FB-003"',
        'data-fill-question-id="QB-FB-013"',
        '<meta name="author" content="Kevin@SUT">',
        'data-attribution="Kevin@SUT"',
    )
    for marker in required:
        if marker not in text:
            fail(failures, f"missing CW-L10 marker: {marker}")
    for pattern in EXTERNAL_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            fail(failures, f"external or persistent dependency found: {pattern}")
    for pattern in TEACHER_ONLY_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            fail(failures, f"teacher-only content found: {pattern}")
    for phrase in CW_L02_STUDENT_FORBIDDEN:
        if phrase in text:
            fail(failures, f"student-facing teacher-prep phrase found: {phrase}")

    if len(SLIDE_PATTERN.findall(text)) != 32:
        fail(failures, "CW-L10 must contain exactly 32 slides")
    if len(SECTION_BLOCK_PATTERN.findall(text)) != 32:
        fail(failures, "CW-L10 must contain exactly 32 complete slide sections")
    if text.count("<details") != 0:
        fail(failures, "CW-L10 must expose all exercises directly")
    if " / 32 · Kevin@SUT" not in text:
        fail(failures, "CW-L10 footer total must be 32")

    choice_text = "".join(
        match.group(0)
        for match in QUESTION_BLOCK_PATTERN.finditer(text)
        if match.group("id") in {"QB-SC-019", "QB-SC-044"}
    )
    validate_embedded_questions(
        choice_text,
        failures,
        ("QB-SC-019", "QB-SC-044"),
        "CW-L10",
    )
    if text.count('data-question-option="') != 12:
        fail(failures, "CW-L10 must expose eight choice options and four true/false options")

    questions = scan_questions()
    pg_source = questions["QB-PG-013"].text
    pg_prompt = re.search(r"## 题目\s*(.*?)\s*### 输入格式", pg_source, re.DOTALL)
    pg_html = re.search(
        r'<section\b[^>]*data-programming-question-id="QB-PG-013"[^>]*>(.*?)</section>',
        text,
        re.IGNORECASE | re.DOTALL,
    )
    source_prompt = normalize_visible_text(pg_prompt.group(1)) if pg_prompt else ""
    html_prompt = normalize_visible_text(pg_html.group(1)) if pg_html else ""
    if not source_prompt or source_prompt not in html_prompt:
        fail(failures, "CW-L10 must visibly embed the QB-PG-013 prompt")

    for question_id in ("QB-TF-004", "QB-TF-005"):
        source = questions[question_id].text
        statement = re.search(r"^>\s*(.+)$", source, re.MULTILINE)
        block = re.search(
            rf'<article\b[^>]*data-question-id="{question_id}"[^>]*>(.*?)</article>',
            text,
            re.IGNORECASE | re.DOTALL,
        )
        visible = normalize_visible_text(block.group(1)) if block else ""
        if not statement or normalize_visible_text(statement.group(1)) not in visible:
            fail(failures, f"{question_id} statement differs from the question bank")
        if not block or len(QUESTION_OPTION_PATTERN.findall(block.group(1))) != 2:
            fail(failures, f"{question_id} must expose correct and incorrect choices")

    for question_id in ("QB-FB-003", "QB-FB-013"):
        source = questions[question_id].text
        source_code = re.search(r"```c\s*(.*?)```", source, re.DOTALL)
        block = re.search(
            rf'<section\b[^>]*data-fill-question-id="{question_id}"[^>]*>(.*?)</section>',
            text,
            re.IGNORECASE | re.DOTALL,
        )
        html_code = re.search(
            r'<pre\b[^>]*class="[^"]*fill-code[^"]*"[^>]*>(.*?)</pre>',
            block.group(1) if block else "",
            re.DOTALL,
        )
        source_tokens = re.sub(r"\s+", "", source_code.group(1)) if source_code else ""
        html_tokens = re.sub(
            r"\s+",
            "",
            html.unescape(re.sub(r"<[^>]+>", "", html_code.group(1))),
        ) if html_code else ""
        if source_tokens != html_tokens:
            fail(failures, f"{question_id} program differs from the question bank")

    program_blocks = {
        match.group("id"): html.unescape(re.sub(r"<[^>]+>", "", match.group("body")))
        for match in re.finditer(
            r'<pre\b[^>]*data-positive-program="(?P<id>[^"]+)"[^>]*>(?P<body>.*?)</pre>',
            text,
            re.IGNORECASE | re.DOTALL,
        )
    }
    if set(program_blocks) != {"scalar-maximum", "float-array-sort"}:
        fail(failures, "CW-L10 must contain exactly the two declared positive programs")
    validate_cw_l10_programs(text, program_blocks, failures)
    check_links(text, path, failures, require_optional_external=False)
    return failures


def validate_cw_l10_programs(
    text: str,
    program_blocks: dict[str, str],
    failures: list[str],
) -> None:
    code_text = "\n".join(program_blocks.values())
    for forbidden, label in (
        (r"\b(?:int|double|float|char|void)\s*\*+\s*\w+", "pointer declaration"),
        (r"\breturn\s+1\s*;", "return 1"),
        (r"\?[^:\n]+:", "conditional operator"),
        (r"\b(?:static|extern)\b", "global or static storage"),
        (r"\b(?:malloc|calloc|realloc|free)\s*\(", "dynamic memory"),
        (r"\bstruct\b", "structure"),
    ):
        if re.search(forbidden, code_text):
            fail(failures, f"CW-L10 positive programs must not introduce {label}")
    if re.search(r"if\s*\(\s*scanf|scanf\s*\([^;]+\)\s*[!=]=", code_text):
        fail(failures, "CW-L10 student programs must not check scanf return values")

    maximum = program_blocks.get("scalar-maximum", "")
    sorting = program_blocks.get("float-array-sort", "")
    for marker in (
        "int max(int x, int y);", "result = max(a, b);", "int max(int x, int y)",
        "if (x > y)", "result = x;", "result = y;", "return result;",
    ):
        if marker not in maximum:
            fail(failures, f"CW-L10 maximum program is incomplete: {marker}")
    if maximum.count("max(") != 3:
        fail(failures, "CW-L10 maximum program must contain one declaration, call, and definition")
    if loop_nesting_depth(maximum) != 0:
        fail(failures, "CW-L10 maximum program must not introduce loops")

    for marker in (
        "void sort(double a[], int n);", "sort(a, 10);", "void sort(double a[], int n)",
        "for (i = 0; i < n - 1; i++)", "for (j = 0; j < n - 1 - i; j++)",
        "if (a[j] > a[j + 1])", "a[j] = a[j + 1];", "a[j + 1] = t;",
    ):
        if marker not in sorting:
            fail(failures, f"CW-L10 sorting program is incomplete: {marker}")
    if sorting.count("sort(") != 3:
        fail(failures, "CW-L10 sorting program must contain one declaration, call, and definition")
    if loop_nesting_depth(sorting) != 2:
        fail(failures, "CW-L10 sorting program must have loop nesting depth two")

    visible = normalize_visible_text(text)
    for marker in (
        "普通参数按值传递", "实参按位置对应形参", "void函数", "不展开数组参数的底层实现",
        "main负责输入、调用和输出", "sort负责排列数组元素", "浏览器进行确定性预演",
    ):
        if marker not in text and marker not in visible:
            fail(failures, f"CW-L10 student explanation is incomplete: {marker}")
    counts = (
        ('data-max-case="', 3, "maximum behavior cases"),
        ('data-fill-answer="', 4, "QB-FB-013 answer controls"),
        ('data-fb003-answer="', 4, "QB-FB-003 answer controls"),
        ('data-function-error="', 4, "function diagnosis cases"),
        ("data-review ", 14, "review questions"),
    )
    for marker, expected, label in counts:
        actual = text.count(marker)
        if actual != expected:
            fail(failures, f"CW-L10 expected {expected} {label}, found {actual}")
    for command in (
        "gcc maximum.c -o maximum.exe\n.\\maximum.exe",
        "gcc sort.c -o sort.exe\n.\\sort.exe",
    ):
        if command not in text:
            fail(failures, f"CW-L10 beginner command is missing: {command.splitlines()[0]}")
    compile_cw_l10_programs(program_blocks, failures)


def compile_cw_l10_programs(
    program_blocks: dict[str, str],
    failures: list[str],
) -> None:
    gcc = shutil.which("gcc")
    if not gcc:
        fail(failures, "CW-L10 MinGW GCC was not found")
        return
    machine = subprocess.run(
        [gcc, "-dumpmachine"], text=True, encoding="utf-8", errors="replace",
        capture_output=True, check=False,
    )
    if machine.returncode != 0 or "mingw" not in machine.stdout.lower():
        fail(failures, f"CW-L10 compiler is not MinGW GCC: {machine.stdout.strip()}")
        return
    fixtures = {
        "scalar-maximum": (
            ("8 5\n", "8\n"),
            ("-3 -7\n", "-3\n"),
            ("4 4\n", "4\n"),
        ),
        "float-array-sort": (
            ("9 8 7 6 5 4 3 2 1 0\n", "0.00 1.00 2.00 3.00 4.00 5.00 6.00 7.00 8.00 9.00\n"),
            ("0 1 2 3 4 5 6 7 8 9\n", "0.00 1.00 2.00 3.00 4.00 5.00 6.00 7.00 8.00 9.00\n"),
            ("3.5 -1 3.5 2 0 -1 2 3 1 0\n", "-1.00 -1.00 0.00 0.00 1.00 2.00 2.00 3.00 3.50 3.50\n"),
        ),
    }
    with tempfile.TemporaryDirectory(prefix="cw-l10-validation-") as temp_name:
        temp_dir = Path(temp_name)
        for program_id, cases in fixtures.items():
            source = temp_dir / f"{program_id}.c"
            executable = temp_dir / f"{program_id}.exe"
            source.write_text(program_blocks[program_id], encoding="utf-8", newline="\n")
            build = subprocess.run(
                [gcc, "-std=c11", "-Wall", "-Wextra", "-Wpedantic", "-Werror", str(source), "-o", str(executable)],
                text=True, encoding="utf-8", errors="replace", capture_output=True, check=False,
            )
            if build.returncode != 0:
                fail(failures, f"CW-L10 {program_id} compile failed: {build.stderr.strip()}")
                continue
            for stdin_text, expected in cases:
                result = subprocess.run(
                    [str(executable)], input=stdin_text, text=True, encoding="utf-8",
                    errors="replace", capture_output=True, check=False, timeout=10,
                )
                actual = result.stdout.replace("\r\n", "\n")
                if result.returncode != 0 or actual != expected:
                    fail(failures, f"CW-L10 {program_id} output mismatch: exit={result.returncode}, actual={actual!r}")


def validate_cw_l11(path: Path) -> list[str]:
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
    required = (
        'data-course-id="CW-L11"',
        'data-chapter="7"',
        'data-routines="EX-C07-007,EX-C07-022"',
        'data-questions="QB-PG-018,QB-PG-015,QB-SC-017,QB-SC-046,QB-TR-017,QB-TR-026"',
        'data-lesson-variants="recursive-factorial-valid-range,recursive-fibonacci-first-twenty"',
        'data-positive-program="recursive-factorial"',
        'data-positive-program="recursive-fibonacci"',
        'data-programming-question-id="QB-PG-018"',
        'data-programming-question-id="QB-PG-015"',
        'data-trace-question-id="QB-TR-017"',
        'data-trace-question-id="QB-TR-026"',
        '<meta name="author" content="Kevin@SUT">',
        'data-attribution="Kevin@SUT"',
    )
    for marker in required:
        if marker not in text:
            fail(failures, f"missing CW-L11 marker: {marker}")
    for pattern in EXTERNAL_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            fail(failures, f"external or persistent dependency found: {pattern}")
    for pattern in TEACHER_ONLY_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            fail(failures, f"teacher-only content found: {pattern}")
    for phrase in CW_L02_STUDENT_FORBIDDEN:
        if phrase in text:
            fail(failures, f"student-facing teacher-prep phrase found: {phrase}")
    if len(SLIDE_PATTERN.findall(text)) != 34:
        fail(failures, "CW-L11 must contain exactly 34 slides")
    if len(SECTION_BLOCK_PATTERN.findall(text)) != 34:
        fail(failures, "CW-L11 must contain exactly 34 complete slide sections")
    if text.count("<details") != 0:
        fail(failures, "CW-L11 must expose all exercises directly")
    if " / 34 · Kevin@SUT" not in text:
        fail(failures, "CW-L11 footer total must be 34")

    choice_text = "".join(
        match.group(0)
        for match in QUESTION_BLOCK_PATTERN.finditer(text)
        if match.group("id") in {"QB-SC-017", "QB-SC-046"}
    )
    validate_embedded_questions(
        choice_text,
        failures,
        ("QB-SC-017", "QB-SC-046"),
        "CW-L11",
    )
    if text.count('data-question-option="') != 8:
        fail(failures, "CW-L11 must expose eight choice options")

    questions = scan_questions()
    for question_id in ("QB-PG-018", "QB-PG-015"):
        source = questions[question_id].text
        prompt = re.search(r"## 题目\s*(.*?)\s*### 输入格式", source, re.DOTALL)
        block = re.search(
            rf'<section\b[^>]*data-programming-question-id="{question_id}"[^>]*>(.*?)</section>',
            text,
            re.IGNORECASE | re.DOTALL,
        )
        source_prompt = normalize_visible_text(prompt.group(1)) if prompt else ""
        html_prompt = normalize_visible_text(block.group(1)) if block else ""
        if not source_prompt or source_prompt not in html_prompt:
            fail(failures, f"CW-L11 must visibly embed the {question_id} prompt")

    for question_id in ("QB-TR-017", "QB-TR-026"):
        source_code = re.search(r"```c\s*(.*?)```", questions[question_id].text, re.DOTALL)
        block = re.search(
            rf'<section\b[^>]*data-trace-question-id="{question_id}"[^>]*>(.*?)</section>',
            text,
            re.IGNORECASE | re.DOTALL,
        )
        html_code = re.search(
            r'<pre\b[^>]*data-trace-code[^>]*>(.*?)</pre>',
            block.group(1) if block else "",
            re.DOTALL,
        )
        source_tokens = re.sub(r"\s+", "", source_code.group(1)) if source_code else ""
        html_tokens = re.sub(
            r"\s+",
            "",
            html.unescape(re.sub(r"<[^>]+>", "", html_code.group(1))),
        ) if html_code else ""
        if source_tokens != html_tokens:
            fail(failures, f"{question_id} program differs from the question bank")

    program_blocks = {
        match.group("id"): html.unescape(re.sub(r"<[^>]+>", "", match.group("body")))
        for match in re.finditer(
            r'<pre\b[^>]*data-positive-program="(?P<id>[^"]+)"[^>]*>(?P<body>.*?)</pre>',
            text,
            re.IGNORECASE | re.DOTALL,
        )
    }
    if set(program_blocks) != {"recursive-factorial", "recursive-fibonacci"}:
        fail(failures, "CW-L11 must contain exactly the two declared positive programs")
    validate_cw_l11_programs(text, program_blocks, failures)
    check_links(text, path, failures, require_optional_external=False)
    return failures


def validate_cw_l12(path: Path) -> list[str]:
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
    required = (
        'data-course-id="CW-L12"',
        'data-chapter="8"',
        'data-routines="EX-C08-002,EX-C08-008"',
        'data-questions="QB-PG-038,QB-SC-058,QB-SC-023,QB-SC-065,QB-SC-021,QB-SC-049,QB-TR-018,QB-TF-014"',
        'data-lesson-variants="pointer-order-by-swapping-addresses,string-length-pointer-difference"',
        'data-positive-program="pointer-order"',
        'data-positive-program="pointer-string-length"',
        'data-programming-question-id="QB-PG-038"',
        'data-trace-question-id="QB-TR-018"',
        'data-true-false="QB-TF-014"',
        '<meta name="author" content="Kevin@SUT">',
        'data-attribution="Kevin@SUT"',
    )
    for marker in required:
        if marker not in text:
            fail(failures, f"missing CW-L12 marker: {marker}")
    for pattern in EXTERNAL_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            fail(failures, f"external or persistent dependency found: {pattern}")
    for pattern in TEACHER_ONLY_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            fail(failures, f"teacher-only content found: {pattern}")
    for phrase in CW_L02_STUDENT_FORBIDDEN:
        if phrase in text:
            fail(failures, f"student-facing teacher-prep phrase found: {phrase}")
    if len(SLIDE_PATTERN.findall(text)) != 36:
        fail(failures, "CW-L12 must contain exactly 36 slides")
    if text.count("<details") != 0:
        fail(failures, "CW-L12 must expose all exercises directly")
    if ">36</span>" not in text and " / 36" not in text:
        fail(failures, "CW-L12 footer total must be 36")

    choice_text = "".join(
        match.group(0)
        for match in QUESTION_BLOCK_PATTERN.finditer(text)
        if match.group("id") in {"QB-SC-058", "QB-SC-023", "QB-SC-065", "QB-SC-021", "QB-SC-049"}
    )
    validate_embedded_questions(
        choice_text,
        failures,
        ("QB-SC-058", "QB-SC-023", "QB-SC-065", "QB-SC-021", "QB-SC-049"),
        "CW-L12",
    )
    if text.count('data-question-option="') != 20:
        fail(failures, "CW-L12 must expose twenty choice options")

    questions = scan_questions()
    source_prompt = re.search(
        r"## 题目\s*(.*?)\s*### 输入格式",
        questions["QB-PG-038"].text,
        re.DOTALL,
    )
    pg_block = re.search(
        r'<article\b[^>]*data-programming-question-id="QB-PG-038"[^>]*>(.*?)</article>',
        text,
        re.IGNORECASE | re.DOTALL,
    )
    if not source_prompt or not pg_block or normalize_visible_text(source_prompt.group(1)) not in normalize_visible_text(pg_block.group(1)):
        fail(failures, "CW-L12 must visibly embed the QB-PG-038 prompt")

    source_code = re.search(r"```c\s*(.*?)```", questions["QB-TR-018"].text, re.DOTALL)
    html_code = re.search(r'<pre\b[^>]*data-trace-code[^>]*>(.*?)</pre>', text, re.DOTALL)
    source_tokens = re.sub(r"\s+", "", source_code.group(1)) if source_code else ""
    html_tokens = re.sub(
        r"\s+", "", html.unescape(re.sub(r"<[^>]+>", "", html_code.group(1)))
    ) if html_code else ""
    if source_tokens != html_tokens:
        fail(failures, "QB-TR-018 program differs from the question bank")
    tf_statement = "指针变量遍历到数组末尾后会自动恢复为数组首地址。"
    if tf_statement not in normalize_visible_text(text):
        fail(failures, "CW-L12 must visibly embed the QB-TF-014 statement")

    program_blocks = {
        match.group("id"): html.unescape(re.sub(r"<[^>]+>", "", match.group("body")))
        for match in re.finditer(
            r'<pre\b[^>]*data-positive-program="(?P<id>[^"]+)"[^>]*>(?P<body>.*?)</pre>',
            text,
            re.IGNORECASE | re.DOTALL,
        )
    }
    if set(program_blocks) != {"pointer-order", "pointer-string-length"}:
        fail(failures, "CW-L12 must contain exactly the two declared positive programs")
    validate_cw_l12_programs(text, program_blocks, failures)
    check_links(text, path, failures, require_optional_external=False)
    return failures


def validate_cw_l12_programs(
    text: str,
    program_blocks: dict[str, str],
    failures: list[str],
) -> None:
    code_text = "\n".join(program_blocks.values())
    for forbidden, label in (
        (r"\*\s*\*", "double pointer"),
        (r"\bstruct\b", "structure"),
        (r"\b(?:FILE|fopen|fclose|fprintf|fscanf|fread|fwrite)\b", "file API"),
        (r"\b(?:malloc|calloc|realloc|free)\s*\(", "dynamic memory"),
        (r"\(\s*\*\s*\w+\s*\)\s*\(", "function pointer"),
        (r"\[[^\]]+\]\s*\[[^\]]+\]", "multidimensional array"),
    ):
        if re.search(forbidden, code_text):
            fail(failures, f"CW-L12 positive programs must not introduce {label}")
    if re.search(r"\b\w+\s+\w+\s*\([^)]*\*[^)]*\)", code_text):
        fail(failures, "CW-L12 positive programs must not introduce pointer parameters")
    if re.search(r"if\s*\(\s*(?:scanf|fgets)|(?:scanf|fgets)\s*\([^;]+\)\s*[!=]=", code_text):
        fail(failures, "CW-L12 student programs must not check input return values")

    order = program_blocks.get("pointer-order", "")
    for marker in (
        "int *p1, *p2, *temp;", "p1 = &a;", "p2 = &b;", "if (*p1 < *p2)",
        "temp = p1;", "p1 = p2;", "p2 = temp;",
        'printf("max=%d min=%d\\n", *p1, *p2);',
    ):
        if marker not in order:
            fail(failures, f"CW-L12 pointer-order program is incomplete: {marker}")
    if re.search(r"\b[ab]\s*=", order):
        fail(failures, "CW-L12 pointer-order program must not assign new values to a or b")

    length = program_blocks.get("pointer-string-length", "")
    for marker in (
        'char s[] = "hello world\\n";', "char *start;", "char *p;",
        "start = s;", "p = s;", "while (*p != '\\0' && *p != '\\n')",
        "p++;", 'printf("%d\\n", (int)(p - start));',
    ):
        if marker not in length:
            fail(failures, f"CW-L12 string-length program is incomplete: {marker}")
    if "start++" in length or "++start" in length:
        fail(failures, "CW-L12 string-length program must preserve start")

    visible = normalize_visible_text(text)
    for marker in (
        "存储位置", "取地址", "解引用", "指针指向改变", "数组名不能自增",
        "同一数组", "不能再解引用", "换行符", "字符串结束标志",
    ):
        if marker not in text and marker not in visible:
            fail(failures, f"CW-L12 student explanation is incomplete: {marker}")
    counts = (
        ('data-pointer-error="', 4, "pointer diagnosis cases"),
        ('data-string-error="', 4, "string diagnosis cases"),
        ('data-order-case="', 4, "pointer-order test selectors"),
        ('data-string-case="', 4, "string-length test selectors"),
        ('data-trace-reveal>', 1, "trace answer control"),
        ('data-tf-answer="', 2, "true-false controls"),
        ('data-review>', 14, "review questions"),
    )
    for marker, expected, label in counts:
        actual = text.count(marker)
        if actual != expected:
            fail(failures, f"CW-L12 expected {expected} {label}, found {actual}")
    for command in (
        "gcc pointer_order.c -o pointer_order.exe&#10;.\\pointer_order.exe",
        "gcc string_length.c -o string_length.exe&#10;.\\string_length.exe",
    ):
        if command not in text:
            fail(failures, f"CW-L12 beginner command is missing: {command.split('&#10;')[0]}")
    compile_cw_l12_programs(program_blocks, failures)


def compile_cw_l12_programs(
    program_blocks: dict[str, str],
    failures: list[str],
) -> None:
    gcc = shutil.which("gcc")
    if not gcc:
        fail(failures, "CW-L12 MinGW GCC was not found")
        return
    machine = subprocess.run(
        [gcc, "-dumpmachine"], text=True, encoding="utf-8", errors="replace",
        capture_output=True, check=False,
    )
    if machine.returncode != 0 or "mingw" not in machine.stdout.lower():
        fail(failures, f"CW-L12 compiler is not MinGW GCC: {machine.stdout.strip()}")
        return
    fixtures = {
        "pointer-order": (
            ("5 8\n", "max=8 min=5\n"),
            ("8 5\n", "max=8 min=5\n"),
            ("4 4\n", "max=4 min=4\n"),
            ("-3 -8\n", "max=-3 min=-8\n"),
        ),
        "pointer-string-length": (("", "11\n"),),
    }
    with tempfile.TemporaryDirectory(prefix="cw-l12-validation-") as temp_name:
        temp_dir = Path(temp_name)
        for program_id, cases in fixtures.items():
            source = temp_dir / f"{program_id}.c"
            executable = temp_dir / f"{program_id}.exe"
            source.write_text(program_blocks[program_id], encoding="utf-8", newline="\n")
            build = subprocess.run(
                [gcc, "-std=c11", "-Wall", "-Wextra", "-Wpedantic", "-Werror", str(source), "-o", str(executable)],
                text=True, encoding="utf-8", errors="replace", capture_output=True, check=False,
            )
            if build.returncode != 0:
                fail(failures, f"CW-L12 {program_id} compile failed: {build.stderr.strip()}")
                continue
            for stdin_text, expected in cases:
                result = subprocess.run(
                    [str(executable)], input=stdin_text, text=True, encoding="utf-8",
                    errors="replace", capture_output=True, check=False, timeout=10,
                )
                actual = result.stdout.replace("\r\n", "\n")
                if result.returncode != 0 or actual != expected:
                    fail(failures, f"CW-L12 {program_id} output mismatch: exit={result.returncode}, actual={actual!r}")


def validate_cw_l11_programs(
    text: str,
    program_blocks: dict[str, str],
    failures: list[str],
) -> None:
    code_text = "\n".join(program_blocks.values())
    for forbidden, label in (
        (r"\b(?:int|double|float|char|void|long)\s*\*+\s*\w+", "pointer declaration"),
        (r"\w+\s*\[[^\]]*\]", "array"),
        (r"\?[^:\n]+:", "conditional operator"),
        (r"\b(?:static|extern)\b", "global or static storage"),
        (r"\b(?:malloc|calloc|realloc|free)\s*\(", "dynamic memory"),
        (r"\bstruct\b", "structure"),
        (r"\b(?:FILE|fopen|fclose|fprintf|fscanf)\b", "file API"),
    ):
        if re.search(forbidden, code_text):
            fail(failures, f"CW-L11 positive programs must not introduce {label}")
    if re.search(r"if\s*\(\s*scanf|scanf\s*\([^;]+\)\s*[!=]=", code_text):
        fail(failures, "CW-L11 student programs must not check scanf return values")

    factorial = program_blocks.get("recursive-factorial", "")
    fibonacci = program_blocks.get("recursive-fibonacci", "")
    for marker in (
        "long long factorial(int n);",
        "if (n < 0 || n > 20)",
        'printf("invalid\\n");',
        "if (n <= 1)",
        "return n * factorial(n - 1);",
    ):
        if marker not in factorial:
            fail(failures, f"CW-L11 factorial program is incomplete: {marker}")
    if factorial.count("factorial(") != 4:
        fail(failures, "CW-L11 factorial program must contain declaration, call, definition, and one recursive call")
    for marker in (
        "int fibonacci(int n);",
        "for (i = 0; i < 20; i++)",
        "if (n == 0)",
        "if (n == 1)",
        "return fibonacci(n - 1) + fibonacci(n - 2);",
    ):
        if marker not in fibonacci:
            fail(failures, f"CW-L11 fibonacci program is incomplete: {marker}")
    if fibonacci.count("fibonacci(") != 5:
        fail(failures, "CW-L11 fibonacci program must contain declaration, output call, definition, and two recursive calls")
    for forbidden_call in ("factorial(factorial", "fibonacci(fibonacci"):
        if forbidden_call in code_text:
            fail(failures, "CW-L11 recursive arguments must move directly toward a base case")

    visible = normalize_visible_text(text)
    for marker in (
        "递归出口", "规模缩小", "每一层都有自己的形参", "逐层返回",
        "两个出口", "重复子问题", "单链", "双分支",
        "浏览器进行确定性预演",
    ):
        if marker not in text and marker not in visible:
            fail(failures, f"CW-L11 student explanation is incomplete: {marker}")
    counts = (
        ('data-factorial-error="', 4, "factorial diagnosis cases"),
        ('data-fibonacci-error="', 4, "fibonacci diagnosis cases"),
        ('data-fibonacci-case="', 5, "fibonacci value checks"),
        ('data-trace-reveal="', 2, "trace answer controls"),
        ("data-review ", 14, "review questions"),
    )
    for marker, expected, label in counts:
        actual = text.count(marker)
        if actual != expected:
            fail(failures, f"CW-L11 expected {expected} {label}, found {actual}")
    for command in (
        "gcc factorial.c -o factorial.exe&#10;.\\factorial.exe",
        "gcc fibonacci.c -o fibonacci.exe&#10;.\\fibonacci.exe",
    ):
        if command not in text:
            fail(failures, f"CW-L11 beginner command is missing: {command.split('&#10;')[0]}")
    compile_cw_l11_programs(program_blocks, failures)


def compile_cw_l11_programs(
    program_blocks: dict[str, str],
    failures: list[str],
) -> None:
    gcc = shutil.which("gcc")
    if not gcc:
        fail(failures, "CW-L11 MinGW GCC was not found")
        return
    machine = subprocess.run(
        [gcc, "-dumpmachine"], text=True, encoding="utf-8", errors="replace",
        capture_output=True, check=False,
    )
    if machine.returncode != 0 or "mingw" not in machine.stdout.lower():
        fail(failures, f"CW-L11 compiler is not MinGW GCC: {machine.stdout.strip()}")
        return
    fixtures = {
        "recursive-factorial": (
            ("0\n", "1\n"),
            ("5\n", "120\n"),
            ("20\n", "2432902008176640000\n"),
            ("-1\n", "invalid\n"),
            ("21\n", "invalid\n"),
        ),
        "recursive-fibonacci": (
            ("", "0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181\n"),
        ),
    }
    with tempfile.TemporaryDirectory(prefix="cw-l11-validation-") as temp_name:
        temp_dir = Path(temp_name)
        for program_id, cases in fixtures.items():
            source = temp_dir / f"{program_id}.c"
            executable = temp_dir / f"{program_id}.exe"
            source.write_text(program_blocks[program_id], encoding="utf-8", newline="\n")
            build = subprocess.run(
                [gcc, "-std=c11", "-Wall", "-Wextra", "-Wpedantic", "-Werror", "-D__USE_MINGW_ANSI_STDIO=1", str(source), "-o", str(executable)],
                text=True, encoding="utf-8", errors="replace", capture_output=True, check=False,
            )
            if build.returncode != 0:
                fail(failures, f"CW-L11 {program_id} compile failed: {build.stderr.strip()}")
                continue
            for stdin_text, expected in cases:
                result = subprocess.run(
                    [str(executable)], input=stdin_text, text=True, encoding="utf-8",
                    errors="replace", capture_output=True, check=False, timeout=10,
                )
                actual = result.stdout.replace("\r\n", "\n")
                if result.returncode != 0 or actual != expected:
                    fail(failures, f"CW-L11 {program_id} output mismatch: exit={result.returncode}, actual={actual!r}")


def validate(path: Path, course_id: str = "CW-L01") -> list[str]:
    if course_id == "CW-L12":
        return validate_cw_l12(path)
    if course_id == "CW-L11":
        return validate_cw_l11(path)
    if course_id == "CW-L02":
        return validate_cw_l02(path)
    if course_id == "CW-L03":
        return validate_cw_l03(path)
    if course_id == "CW-L04":
        return validate_cw_l04(path)
    if course_id == "CW-L05":
        return validate_cw_l05(path)
    if course_id == "CW-L06":
        return validate_cw_l06(path)
    if course_id == "CW-L07":
        return validate_cw_l07(path)
    if course_id == "CW-L08":
        return validate_cw_l08(path)
    if course_id == "CW-L09":
        return validate_cw_l09(path)
    if course_id == "CW-L10":
        return validate_cw_l10(path)
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
    parser.add_argument("--id", default="CW-L01", help="courseware id: CW-L01 through CW-L12")
    parser.add_argument("--path", type=Path, help="explicit HTML path for local validation")
    args = parser.parse_args()

    try:
        path = args.path.resolve() if args.path else target_for(args.id)
    except ValueError as exc:
        print(f"COURSEWARE VALIDATION FAILED: {exc}")
        return 2

    failures = validate(path, args.id)
    if failures:
        print("COURSEWARE VALIDATION FAILED")
        for item in failures:
            print(f"- {item}")
        return 1

    slide_count = 36 if args.id == "CW-L12" else 34 if args.id in {"CW-L09", "CW-L11"} else 32 if args.id == "CW-L10" else 12 if args.id == "CW-L01" else 30 if args.id in {"CW-L07", "CW-L08"} else 28 if args.id == "CW-L06" else 26 if args.id in {"CW-L04", "CW-L05"} else 25
    optional_external = 1 if args.id == "CW-L01" else 0
    print(f"COURSEWARE VALIDATION PASS: {args.id}, slides={slide_count}, offline-core=ok, optional_external={optional_external}, links=ok, text_encoding=UTF-8, bom=utf8-no-bom")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
