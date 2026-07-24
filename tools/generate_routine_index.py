#!/usr/bin/env python3
"""Generate the student-facing routine index from source headers."""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path

sys.dont_write_bytecode = True

from routine_common import MetadataError, ROUTINES_ROOT, Routine, scan_routines


INDEX_PATH = ROUTINES_ROOT / "README.md"
CHAPTER_TITLES = {
    "01-programming-and-c": "第 1 章 程序设计和 C 语言",
    "02-algorithms": "第 2 章 算法——程序的灵魂",
    "03-sequential-programming": "第 3 章 顺序程序设计",
    "04-selection": "第 4 章 选择结构程序设计",
    "05-loops": "第 5 章 循环结构程序设计",
    "06-arrays-and-strings": "第 6 章 利用数组处理批量数据",
    "07-functions": "第 7 章 用函数实现模块化程序设计",
    "08-pointers": "第 8 章 善于利用指针",
    "09-user-defined-types": "第 9 章 用户自己建立数据类型",
    "10-files": "第 10 章 对文件的输入输出",
}
PROJECT_TITLES = {
    "calculator": "计算器",
    "data-management": "数据管理",
    "snake": "贪吃蛇",
    "game-2048": "2048",
    "maze": "迷宫",
}


def escape_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def source_links(routine: Routine) -> str:
    links = []
    for source in routine.sources:
        relative = source.relative_to(ROUTINES_ROOT).as_posix()
        links.append(f"[`{source.name}`]({relative})")
    return "<br>".join(links)


def table(rows: list[Routine]) -> list[str]:
    lines = [
        "| ID | 标题 | 教材位置 | 知识点 | 编译模式 | 旧语法 | 源码 |",
        "|---|---|---|---|---|---|---|",
    ]
    for routine in rows:
        legacy = "、".join(routine.legacy_features) or "无"
        lines.append(
            "| "
            + " | ".join(
                (
                    routine.routine_id,
                    escape_cell(routine.title),
                    escape_cell(routine.textbook_ref),
                    escape_cell("、".join(routine.concepts)),
                    routine.build_mode,
                    escape_cell(legacy),
                    source_links(routine),
                )
            )
            + " |"
        )
    return lines


def render_index(routines: dict[str, Routine] | None = None) -> str:
    if routines is None:
        routines, _ = scan_routines()
    strict_count = sum(item.build_mode == "c11-strict" for item in routines.values())
    textbook_count = len(routines) - strict_count
    chapter_groups: dict[str, list[Routine]] = defaultdict(list)
    project_groups: dict[str, list[Routine]] = defaultdict(list)
    for routine in routines.values():
        relative = routine.sources[0].relative_to(ROUTINES_ROOT)
        if relative.parts[0] == "chapters":
            chapter_groups[relative.parts[1]].append(routine)
        elif relative.parts[0] == "projects":
            project_groups[relative.parts[1]].append(routine)
        else:
            raise MetadataError(f"Unexpected routine path: {relative}")

    lines = [
        "# C 语言例程库",
        "",
        "本目录以谭浩强《C程序设计（第五版）》第 1–10 章为主轴，"
        "仅支持 MinGW-w64 GCC。例程元数据以源码文件头为准。",
        "",
        f"当前共 {len(routines)} 个例程：{strict_count} 个 `c11-strict`，"
        f"{textbook_count} 个 `gnu99-textbook`。",
        "",
        "源码头中的 `来源` 字段保留历史 provenance；旧学期路径不再是工作区目录，需通过 Git 历史恢复原始文件。",
        "",
        "## 最短使用路径",
        "",
        "```powershell",
        "# 验证全部例程",
        "conda run -n base python tools/validate_routines.py",
        "",
        "# 验证单个例程（多文件例程会自动整体构建）",
        "conda run -n base python tools/validate_routines.py --id EX-C05-010",
        "",
        "# 检查本索引是否与源码头一致",
        "conda run -n base python tools/generate_routine_index.py --check",
        "```",
        "",
        "单文件例程也可在仓库根目录直接编译，例如：",
        "",
        "```powershell",
        "gcc -std=c11 -Wall -Wextra -Wpedantic -Werror \"例程/chapters/01-programming-and-c/ex_c01_001_1_1.c\" -o hello.exe",
        ".\\hello.exe",
        "Remove-Item -LiteralPath .\\hello.exe",
        "```",
        "",
        "`gets()`、`conio.h` 等教材旧接口的适用边界写在对应源码文件头。",
    ]
    for chapter_name in CHAPTER_TITLES:
        rows = sorted(chapter_groups.get(chapter_name, []), key=lambda item: item.routine_id)
        lines.extend(("", f"## {CHAPTER_TITLES[chapter_name]}", ""))
        lines.extend(table(rows))
    lines.extend(("", "## 渐进项目", ""))
    for project_name in PROJECT_TITLES:
        rows = sorted(project_groups.get(project_name, []), key=lambda item: item.routine_id)
        lines.extend((f"### {PROJECT_TITLES[project_name]}", ""))
        lines.extend(table(rows))
        lines.append("")
    lines.extend(
        (
            "## 维护约定",
            "",
            "- 不手工维护机器可读目录；索引由源码文件头生成。",
            "- 单个例程的所有源码必须使用同一个例程 ID，且只能有一个 `main()`。",
            "- 编译和运行产物只进入仓库根的隔离临时目录，命令结束时必须删除。",
            "- 本页由 `tools/generate_routine_index.py` 生成。",
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
                print("INDEX CHECK FAILED: 例程/README.md is out of date", file=sys.stderr)
                return 1
            print("INDEX PASS: 例程/README.md is current")
            return 0
        INDEX_PATH.write_text(rendered, encoding="utf-8", newline="\n")
        print("Generated 例程/README.md")
        return 0
    except (MetadataError, OSError) as exc:
        print(f"INDEX FAILED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
