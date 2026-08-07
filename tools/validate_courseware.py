#!/usr/bin/env python3
"""Validate the offline interactive HTML courseware lessons."""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

from question_common import scan_questions


ROOT = Path(__file__).resolve().parents[1]
CW_L01 = ROOT / "课件" / "讲授" / "01-course-introduction-and-hello-world" / "index.html"
CW_L02 = ROOT / "课件" / "讲授" / "02-algorithms-and-program-logic" / "index.html"
CW_L03 = ROOT / "课件" / "讲授" / "03-sequential-programming" / "index.html"
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

def validate(path: Path, course_id: str = "CW-L01") -> list[str]:
    if course_id == "CW-L02":
        return validate_cw_l02(path)
    if course_id == "CW-L03":
        return validate_cw_l03(path)
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
    parser.add_argument("--id", default="CW-L01", help="courseware id: CW-L01, CW-L02, or CW-L03")
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

    slide_count = 12 if args.id == "CW-L01" else 25
    optional_external = 1 if args.id == "CW-L01" else 0
    print(f"COURSEWARE VALIDATION PASS: {args.id}, slides={slide_count}, offline-core=ok, optional_external={optional_external}, links=ok, text_encoding=UTF-8, bom=utf8-no-bom")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
