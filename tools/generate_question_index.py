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
        "本题库首先服务于学生掌握解题方法、减少常见失分并通过课程考试。"
        "兴趣拓展是辅助目标，不能替代基础题型和考试题训练。",
        "",
        "教材配套 PPT 适合课前预习和课后复习；课堂交互课件将通过稳定题目 ID "
        "引用本题库，每次集中讲解少量程序、关联知识点和对应题型。",
        "",
        "## 使用原则",
        "",
        "- 先独立作答，再展开“参考答案与解析”。",
        "- 同一知识点的不同代码、陷阱和输入作为变式保留。",
        "- 题库不标注试卷年度、考试性质或试卷版本。",
        "- 参考程序以 MinGW-w64 GCC 为验证边界。",
        "",
        "## 最短使用路径",
        "",
        "```powershell",
        "# 检查全部题目、答案和参考程序",
        "conda run -n base python tools/validate_questions.py",
        "",
        "# 检查一道题",
        "conda run -n base python tools/validate_questions.py --id QB-PG-001",
        "",
        "# 检查本索引是否最新",
        "conda run -n base python tools/generate_question_index.py --check",
        "```",
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
            "## 维护约定",
            "",
            "- 每道题独立保存为 Markdown，文件头是唯一元数据来源。",
            "- 参考答案与解析必须与题目保存在同一文件并默认折叠。",
            "- 编程题和程序填空题的完整参考程序必须通过 MinGW GCC 编译。",
            "- 本页由 `tools/generate_question_index.py` 生成，不手工维护题目清单。",
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
