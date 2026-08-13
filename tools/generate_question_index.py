#!/usr/bin/env python3
"""Generate the student-facing question index from Markdown metadata."""

from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict

sys.dont_write_bytecode = True

from question_common import (
    CATEGORY_CODES,
    QUESTIONS_ROOT,
    Question,
    QuestionError,
    scan_questions,
)


INDEX_PATH = QUESTIONS_ROOT / "README.md"


def _link(question: Question) -> str:
    relative = question.path.relative_to(QUESTIONS_ROOT).as_posix()
    title = question.text.splitlines()[11].removeprefix("# ").strip()
    return f"[{question.question_id} {title}]({relative})"


def render_index(questions: dict[str, Question] | None = None) -> str:
    if questions is None:
        questions = scan_questions()
    categories: dict[str, list[Question]] = defaultdict(list)
    chapters: dict[str, list[Question]] = defaultdict(list)
    concepts: dict[str, list[Question]] = defaultdict(list)
    for question in questions.values():
        categories[question.category].append(question)
        for chapter in question.chapters:
            chapters[chapter].append(question)
        for concept in question.concepts:
            concepts[concept].append(question)
    counts = Counter(item.category for item in questions.values())

    lines = [
        "# C 语言程序设计题库",
        "",
        "本题库提供选择题、判断题、程序填空、读程序写结果和编程题，适合按题型、章节或知识点自主练习。",
        "",
        "## 使用方法",
        "",
        "1. 从下方题型列表选择题目。",
        "2. 先独立作答，再展开同一文件中的“参考答案与解析”。",
        "3. 对照解析重新跟踪变量或编译参考程序。",
        "",
        f"当前共 {len(questions)} 道题：" + "、".join(
            f"{name}{counts[name]}道" for name in CATEGORY_CODES
        ) + "。",
    ]

    for category in CATEGORY_CODES:
        lines.extend(("", f"## {category}", ""))
        lines.extend(
            f"- {_link(item)} — 第{'、'.join(item.chapters)}章；"
            f"{'、'.join(item.concepts)}；{item.difficulty}；建议 {item.minutes} 分钟"
            for item in categories[category]
        )

    lines.extend(("", "## 按教材章节查找", ""))
    for chapter in sorted(chapters, key=lambda value: int(value)):
        links = "、".join(_link(item) for item in chapters[chapter])
        lines.append(f"- 第 {chapter} 章：{links}")

    lines.extend(("", "## 按知识点查找", ""))
    for concept in sorted(concepts):
        links = "、".join(_link(item) for item in concepts[concept])
        lines.append(f"- {concept}：{links}")

    lines.extend(
        (
            "",
            "## 更多入口",
            "",
            "- [返回仓库首页](../README.md)",
            "- [交互讲授课](../课件/讲授/README.md)",
            "- [MIT License](../LICENSE)",
            "- [第三方内容与来源说明](../THIRD_PARTY_NOTICES.md)",
            "- [维护工具与索引生成说明](../tools/README.md)",
            "",
        )
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        rendered = render_index()
        if args.check:
            current = INDEX_PATH.read_text(encoding="utf-8") if INDEX_PATH.is_file() else ""
            if current != rendered:
                print("INDEX CHECK FAILED: 题库/README.md is out of date", file=sys.stderr)
                return 1
            print("INDEX PASS: 题库/README.md is current")
            return 0
        INDEX_PATH.write_text(rendered, encoding="utf-8", newline="\n")
        print("Generated 题库/README.md")
        return 0
    except (QuestionError, OSError) as exc:
        print(f"INDEX FAILED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
