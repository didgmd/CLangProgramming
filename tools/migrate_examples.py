#!/usr/bin/env python3
"""Build the canonical routine library from the two read-only semester trees.

This is a reproducible, one-way migration tool. It never changes or deletes the
two source semester directories. It only regenerates 例程/ and the routine
migration manifest.
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

sys.dont_write_bytecode = True

from source_fixes import apply_source_fixes


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOTS = (ROOT / "2023-2024-1", ROOT / "2024-2025-1")
ROUTINES_ROOT = ROOT / "例程"
MIGRATION_ROOT = ROOT / "migration"

CHAPTER_DIRS = {
    1: "01-programming-and-c",
    2: "02-algorithms",
    3: "03-sequential-programming",
    4: "04-selection",
    5: "05-loops",
    6: "06-arrays-and-strings",
    7: "07-functions",
    8: "08-pointers",
    9: "09-user-defined-types",
    10: "10-files",
}

CHAPTER_TITLES = {
    1: "程序设计和 C 语言",
    2: "算法——程序的灵魂",
    3: "顺序程序设计",
    4: "选择结构程序设计",
    5: "循环结构程序设计",
    6: "利用数组处理批量数据",
    7: "用函数实现模块化程序设计",
    8: "善于利用指针",
    9: "用户自己建立数据类型",
    10: "对文件的输入输出",
}

CHAPTER_CONCEPTS = {
    1: ["程序结构", "编译与运行", "基本输出"],
    2: ["算法", "流程控制", "问题求解"],
    3: ["数据类型", "运算符", "输入输出"],
    4: ["if", "switch", "条件表达式"],
    5: ["while", "do-while", "for", "break", "continue"],
    6: ["一维数组", "二维数组", "字符数组", "字符串"],
    7: ["函数", "参数", "递归", "变量作用域"],
    8: ["指针", "数组与指针", "字符串指针", "动态内存"],
    9: ["结构体", "枚举", "链表", "自定义数据类型"],
    10: ["文件", "顺序读写", "随机读写", "错误检测"],
}

NEW_CHAPTER_DIRS = {
    "20240920": 1,
    "20240924": 2,
    "20240927_1008": 3,
    "20241011_1015": 4,
    "20241018_1022": 5,
    "20241025_1029": 6,
    "20241105_1108": 7,
    "20241112_1115": 8,
    "20241119_1122": 9,
    "20241129": 10,
}

OLD_CHAPTER_DIRS = {
    "01_HelloC": 1,
    "02_Algorithm": 2,
    "03_Sequential": 3,
    "04_Selection": 4,
    "06_Loop": 5,
    "08_Array": 6,
    "10_Function": 7,
    "11_Pointer": 8,
    "13_Structure": 9,
    "15_File": 10,
}

LAB5_CHAPTERS = {
    "01": 8,
    "02": 8,
    "03": 8,
    "04": 7,
    "05": 9,
    "06": 9,
    "07": 9,
    "08": 8,
    "09": 8,
    "10": 7,
    "11": 7,
}

PROJECT_SPECS = {
    "calculator": {
        "title": "计算器渐进项目",
        "prefix": "CALC",
        "paths": [
            "2023-2024-1/01_HelloC/1_4_1_Calculator.c",
            "2023-2024-1/01_HelloC/1_4_2_CalculatorFunction.c",
            "2023-2024-1/01_HelloC/1_5_2_CalcFuncForLoop.c",
            "2023-2024-1/01_HelloC/1_5_4_CalcFuncWhileLoop.c",
            "2023-2024-1/01_HelloC/1_5_5_CalcWhileLoop.c",
        ],
    },
    "data-management": {
        "title": "数据管理案例",
        "prefix": "DATA",
        "paths": [
            "2023-2024-1/05_Lab1/05_ToDoList.c",
            "2023-2024-1/05_Lab1/06_StudentManagement.c",
            "2023-2024-1/05_Lab1/07_BookManagement.c",
            "2023-2024-1/14_Lab5/12.c",
        ],
    },
    "snake": {
        "title": "贪吃蛇渐进项目",
        "prefix": "SNAKE",
        "paths": [
            f"2023-2024-1/07_Lab2/Snake_Step{i}.c" for i in range(1, 5)
        ],
    },
    "game-2048": {
        "title": "2048 渐进项目",
        "prefix": "2048",
        "paths": [
            f"2023-2024-1/09_Lab3/2048_Step{i}.c" for i in range(1, 7)
        ],
    },
    "maze": {
        "title": "迷宫渐进项目",
        "prefix": "MAZE",
        "paths": [
            f"2023-2024-1/12_Lab4/Maze{i:02d}.c" for i in range(1, 6)
        ],
    },
}

FIXTURE_SPECS = {
    (1, "1.1"): ("", "This is a C program.\n"),
    (
        2,
        "2.1_2.6",
    ): (
        "",
        "p is 1, i is 2\np is 2, i is 3\np is 6, i is 4\np is 24, i is 5\n",
    ),
    (3, "3.1"): ("", "f=64.000000\nc=17.777779\n"),
    (4, "4.1"): ("1 -3 2\n", "real roots:\nx1=   2.00\nx2=   1.00\n"),
    (5, "5.1"): ("", "sum=5050\n"),
    (6, "6.1"): ("", "9 8 7 6 5 4 3 2 1 0 \n"),
    (
        7,
        "7.1",
    ): (
        "",
        "******************\nHow do you do!\n******************\n",
    ),
    (
        8,
        "8.1",
    ): (
        "",
        "a=100,b=10\n*pointer_1=100,*pointer_2=10\n",
    ),
    (
        9,
        "9.1",
    ): (
        "",
        "NO.:10101\nname:Li Lin\nsex:M\naddress:123 Beijing Road\n",
    ),
}


@dataclass(frozen=True)
class SourceInfo:
    path: Path
    rel: str
    academic_year: str
    encoding: str
    sha256: str
    text: str


@dataclass(frozen=True)
class ConceptCandidate:
    source: SourceInfo
    chapter: int
    ref: str
    is_new: bool
    title_hint: str


def relpath(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def decode_source(path: Path) -> tuple[str, str]:
    data = path.read_bytes()
    try:
        return data.decode("utf-8-sig"), "utf-8"
    except UnicodeDecodeError:
        return data.decode("gb18030"), "gb18030"


def read_sources() -> list[SourceInfo]:
    result = []
    for source_root in SOURCE_ROOTS:
        for path in sorted(source_root.rglob("*.c")):
            text, encoding = decode_source(path)
            result.append(
                SourceInfo(
                    path=path,
                    rel=relpath(path),
                    academic_year=source_root.name,
                    encoding=encoding,
                    sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                    text=text,
                )
            )
    return result


def ascii_slug(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", value).strip("_").lower()
    return slug or "example"


def question_bank_reason(source: SourceInfo) -> str | None:
    rel = source.rel
    name = source.path.name
    if "/Examples/" in rel:
        return "以题目描述为入口的算法解答，等待题库板块接收"
    if "/16_Assessment/" in rel:
        return "评分或学生作答样例，等待题库板块接收"
    if re.search(r"错误|正确|反例|wrong|correct|error", name, re.IGNORECASE):
        return "正确/错误对照或反例，等待题库调试题接收"
    if rel.endswith("20241112_1115/8.9.2.c"):
        return "未初始化指针反例，等待题库调试题接收"
    if rel.endswith("03_Sequential/06_Expression.c"):
        return "包含未定义求值顺序，适合作为代码诊断题"
    return None


def discard_reason(source: SourceInfo) -> str | None:
    if source.rel.endswith("06_Loop/03_ex5_03_WhileDoWhile.c"):
        return (
            "文件仅含整段注释、没有可构建程序；while 与 do-while 已由 "
            "5.2、5.3 系列权威例程覆盖"
        )
    return None


def project_lookup() -> dict[str, tuple[str, int, dict[str, object]]]:
    lookup = {}
    for project_name, spec in PROJECT_SPECS.items():
        for step, path in enumerate(spec["paths"], start=1):
            lookup[path] = (project_name, step, spec)
    return lookup


def candidate_chapter(source: SourceInfo) -> int | None:
    parent = source.path.parent.name
    if parent in NEW_CHAPTER_DIRS:
        return NEW_CHAPTER_DIRS[parent]
    if parent in OLD_CHAPTER_DIRS:
        return OLD_CHAPTER_DIRS[parent]
    if parent == "14_Lab5":
        return LAB5_CHAPTERS.get(source.path.stem)
    if parent == "05_Lab1" and source.path.stem in {"01_Pointer", "02_Malloc"}:
        return 8
    if parent == "05_Lab1" and source.path.stem in {"03_Structure"}:
        return 9
    if parent == "05_Lab1" and source.path.stem in {"04_PointerAnalysis"}:
        return 8
    return None


def normal_number(value: str) -> str:
    return str(int(value))


def derive_reference(source: SourceInfo, chapter: int) -> str:
    stem = source.path.stem
    parent = source.path.parent.name

    if parent in NEW_CHAPTER_DIRS:
        if re.fullmatch(r"\d+(?:\.\d+)+(?:[._]file\d+)?", stem, re.IGNORECASE):
            return re.sub(r"[._]file\d+$", "", stem, flags=re.IGNORECASE)
        if re.fullmatch(r"\d+(?:\.\d+)*_\d+(?:\.\d+)*", stem):
            return stem
        return f"custom-{ascii_slug(stem)}"

    if parent == "14_Lab5":
        return f"lab5.{normal_number(stem)}"

    if parent == "05_Lab1":
        return f"lab1-{ascii_slug(stem)}"

    if parent == "01_HelloC":
        match = re.match(r"(\d+)_(\d+)(?:_(\d+))?", stem)
        if match:
            parts = [normal_number(part) for part in match.groups() if part]
            return ".".join(parts)

    match = re.search(
        r"ex_?(\d+)_(\d+)(?:_(\d+))?(?:_file\d+)?",
        stem,
        re.IGNORECASE,
    )
    if match:
        parts = [normal_number(part) for part in match.groups() if part]
        reference = ".".join(parts)
        if "课上" in stem:
            reference += "-class"
        return reference

    return f"custom-{ascii_slug(stem)}"


def title_for(candidate: ConceptCandidate) -> str:
    custom = {
        "custom-floatdouble": "浮点类型与精度",
        "custom-decocthex": "十进制、八进制与十六进制",
        "custom-integer": "整型数据",
        "custom-complement": "整数补码表示",
        "custom-selfoperation": "自增与自减运算",
        "custom-expression": "表达式求值",
        "custom-switch": "switch 语句",
        "custom-alignment": "结构体内存对齐",
        "custom-pointer": "二维数组指针",
        "custom-in-class": "课堂指针演示",
    }
    if candidate.ref in custom:
        return custom[candidate.ref]
    if candidate.ref.startswith("lab"):
        return f"实验演示 {candidate.ref}"
    return f"教材例程 {candidate.ref}"


def sort_reference(ref: str) -> tuple[object, ...]:
    pieces = re.split(r"([0-9]+)", ref)
    return tuple(int(piece) if piece.isdigit() else piece for piece in pieces)


def normalize_and_fix(text: str, source_rel: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n").lstrip("\ufeff")
    text = re.sub(r"\bextern\s+A\s*;", "extern int A;", text)
    text = text.replace('printf("%\\n");', 'printf("%%\\n");')

    if "strcpy(" in text and "#include <string.h>" not in text and "#include<string.h>" not in text:
        include = "#include <string.h>\n"
        stdio = re.search(r"#include\s*[<\"]stdio\.h[>\"]\s*\n", text)
        if stdio:
            text = text[: stdio.end()] + include + text[stdio.end() :]
        else:
            text = include + text

    if re.search(r"\b(?:printf|scanf|gets|fopen|fread|fwrite)\s*\(", text) and not re.search(r"#include\s*[<\"]stdio\.h[>\"]", text):
        text = "#include <stdio.h>\n" + text

    if source_rel.endswith("14_Lab5/08.c"):
        text = text.replace("int* ptr = matrix;", "int* ptr = &matrix[0][0];")

    if re.search(r"\bvoid\s+main\s*\(\s*\)", text):
        text = re.sub(r"\bvoid\s+main\s*\(\s*\)", "int main(void)", text, count=1)
        closing = text.rfind("}")
        if closing >= 0:
            text = text[:closing].rstrip() + "\n    return 0;\n" + text[closing:]

    return apply_source_fixes(text, source_rel)


def synthesize_pointer_sort_variant(source: SourceInfo) -> str:
    main_path = ROOT / "2024-2025-1/20241112_1115/8.10.1.c"
    main_text, _ = decode_source(main_path)
    split = re.split(r"\nvoid\s+sort\s*\(", main_text, maxsplit=1)
    if len(split) != 2:
        raise RuntimeError("Cannot identify the 8.10.1 main/function boundary")
    return split[0].rstrip() + "\n\n" + source.text.lstrip()


def legacy_features(texts: Iterable[str]) -> list[str]:
    joined = "\n".join(texts)
    features = []
    patterns = (
        ("gets", r"\bgets\s*\("),
        ("scanf", r"\bscanf\s*\("),
        ("scanf_s", r"\bscanf_s\s*\("),
        ("conio", r"#\s*include\s*[<\"]conio\.h[>\"]"),
        ("getch", r"\b_?getch\s*\("),
        ("system-pause", r"system\s*\(\s*\"pause\""),
        ("msvc-warning-pragma", r"#\s*pragma\s+warning"),
        ("msvc-crt-compat", r"_CRT_SECURE_NO_WARNINGS"),
        ("malloc-h", r"#\s*include\s*[<\"]malloc\.h[>\"]"),
    )
    for name, pattern in patterns:
        if re.search(pattern, joined):
            features.append(name)
    return features


def compatibility_note(features: list[str], profile: str) -> str:
    if "gets" in features:
        return (
            "教材/考试兼容例程：保留 gets() 以识别教材旧写法。"
            "仅允许受控短输入；该接口已从 C11 移除，不应用于生产程序。"
        )
    if profile == "windows":
        return "Windows 专属例程：依赖 conio.h 或即时按键接口。"
    if profile == "textbook":
        return "教材兼容配置：保留与教材或旧版编译器相关的写法。"
    return "可移植例程：按 C11 子集验证。"


def platform_metadata(features: list[str], profile: str) -> tuple[list[str], str]:
    if profile == "windows":
        return ["windows"], "platform_limited"
    if "gets" in features:
        return ["windows-mingw", "linux-gnu99"], "platform_limited"
    return ["windows", "linux", "macos"], "manual_interaction"

def source_header(
    example_id: str,
    title: str,
    textbook_ref: str,
    concepts: list[str],
    origins: list[str],
    build_mode: str,
    features: list[str],
    interaction: str,
    compatibility: str,
) -> str:
    origin_text = ", ".join(origins)
    concept_text = "、".join(concepts)
    legacy_text = "、".join(feature for feature in features if feature != "scanf") or "无"
    return (
        "/*\n"
        f" * 例程 ID：{example_id}\n"
        f" * 标题：{title}\n"
        f" * 教材位置：{textbook_ref}\n"
        f" * 知识点：{concept_text}\n"
        f" * 来源：{origin_text}\n"
        f" * 编译模式：{build_mode}\n"
        f" * 旧语法：{legacy_text}\n"
        f" * 交互方式：{interaction}\n"
        f" * 兼容性：{compatibility}\n"
        " */\n"
    )

def reset_generated_outputs() -> None:
    for target in (ROUTINES_ROOT, MIGRATION_ROOT):
        resolved = target.resolve()
        if resolved.parent != ROOT.resolve():
            raise RuntimeError(f"Refusing to reset unsafe path: {resolved}")
        if target.exists():
            shutil.rmtree(target)
    (ROUTINES_ROOT / "chapters").mkdir(parents=True)
    (ROUTINES_ROOT / "projects").mkdir(parents=True)
    MIGRATION_ROOT.mkdir(parents=True)


def run_command(command: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=cwd,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def audit_original_sources(sources: list[SourceInfo]) -> dict[str, dict[str, str]]:
    """Audit original syntax without creating link artifacts in the repository."""
    gcc = shutil.which("gcc")
    if not gcc:
        return {
            source.rel: {
                "syntax_status": "not_run_no_gcc",
                "single_file_link_status": "not_run_no_gcc",
            }
            for source in sources
        }

    result = {}
    for source in sources:
        syntax = run_command(
            [
                gcc,
                "-std=c11",
                "-Wall",
                "-Wextra",
                "-Wpedantic",
                "-fsyntax-only",
                str(source.path),
            ]
        )
        if syntax.returncode:
            syntax_status = "error"
        elif syntax.stderr.strip():
            syntax_status = "warning"
        else:
            syntax_status = "ok"
        result[source.rel] = {
            "syntax_status": syntax_status,
            "single_file_link_status": (
                "covered_by_routine_validator"
                if re.search(r"\bmain\s*\(", source.text)
                else "not_attempted_no_main"
            ),
        }
    return result

def syntax_diagnostics(paths: list[Path]) -> tuple[str, str]:
    gcc = shutil.which("gcc")
    if not gcc:
        return "not_run_no_gcc", ""
    combined = []
    for path in paths:
        check = run_command(
            [
                gcc,
                "-std=c11",
                "-Wall",
                "-Wextra",
                "-Wpedantic",
                "-fsyntax-only",
                str(path),
            ]
        )
        combined.append(check.stderr.strip())
        if check.returncode:
            raise RuntimeError(f"Generated source has a syntax error: {relpath(path)}\n{check.stderr}")
    diagnostics = "\n".join(part for part in combined if part)
    return ("warning" if diagnostics else "ok"), diagnostics


def add_migration_entry(
    migration: dict[str, dict[str, object]],
    source: SourceInfo,
    audit: dict[str, dict[str, str]],
    *,
    action: str,
    reason: str,
    final_id: str | None,
    destination: str | None,
    textbook_refs: list[str],
    concepts: list[str],
    near_duplicate_group: str | None,
    question_like: bool,
) -> None:
    if source.rel in migration:
        raise RuntimeError(f"Duplicate migration decision for {source.rel}")
    migration[source.rel] = {
        "source_path": source.rel,
        "academic_year": source.academic_year,
        "original_encoding": source.encoding,
        "sha256": source.sha256,
        "has_main": bool(re.search(r"\bmain\s*\(", source.text)),
        **audit[source.rel],
        "textbook_refs": textbook_refs,
        "knowledge_points": concepts,
        "question_like": question_like,
        "near_duplicate_group": near_duplicate_group,
        "action": action,
        "reason": reason,
        "final_id": final_id,
        "destination": destination,
    }


def build_examples() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    sources = read_sources()
    if len(sources) != 334:
        raise RuntimeError(f"Expected 334 original C files, found {len(sources)}")

    reset_generated_outputs()
    audits = audit_original_sources(sources)
    migration: dict[str, dict[str, object]] = {}
    examples: list[dict[str, object]] = []
    source_by_rel = {source.rel: source for source in sources}
    projects = project_lookup()
    candidates: list[ConceptCandidate] = []

    for source in sources:
        reason = question_bank_reason(source)
        if reason:
            add_migration_entry(
                migration,
                source,
                audits,
                action="question_bank_pending",
                reason=reason,
                final_id=None,
                destination=None,
                textbook_refs=[],
                concepts=["调试", "代码审查"] if "错误" in reason or "诊断" in reason else [],
                near_duplicate_group=None,
                question_like=True,
            )
            continue

        reason = discard_reason(source)
        if reason:
            add_migration_entry(
                migration,
                source,
                audits,
                action="discarded_after_review",
                reason=reason,
                final_id=None,
                destination=None,
                textbook_refs=["第 5 章 / 5.3"],
                concepts=CHAPTER_CONCEPTS[5],
                near_duplicate_group="C05:5.3",
                question_like=False,
            )
            continue

        if source.rel in projects:
            continue

        chapter = candidate_chapter(source)
        if chapter is None:
            add_migration_entry(
                migration,
                source,
                audits,
                action="discarded_after_review",
                reason="不属于已锁定的教材章节、项目链或题库候选范围",
                final_id=None,
                destination=None,
                textbook_refs=[],
                concepts=[],
                near_duplicate_group=None,
                question_like=False,
            )
            continue

        ref = derive_reference(source, chapter)
        candidates.append(
            ConceptCandidate(
                source=source,
                chapter=chapter,
                ref=ref,
                is_new=source.academic_year == "2024-2025-1",
                title_hint=source.path.stem,
            )
        )

    grouped: dict[tuple[int, str], list[ConceptCandidate]] = defaultdict(list)
    for candidate in candidates:
        grouped[(candidate.chapter, candidate.ref)].append(candidate)

    sequence_by_chapter = defaultdict(int)
    for (chapter, ref), group in sorted(
        grouped.items(), key=lambda item: (item[0][0], sort_reference(item[0][1]))
    ):
        newer = [candidate for candidate in group if candidate.is_new]
        selected = newer if newer else [candidate for candidate in group if not candidate.is_new]
        multi_file = ref in {"7.19", "7.20"}

        if not multi_file and len(selected) > 1:
            # Same-version collisions are distinct demonstrations, not implicit multi-file builds.
            for index, candidate in enumerate(selected[1:], start=2):
                candidates.append(
                    ConceptCandidate(
                        source=candidate.source,
                        chapter=chapter,
                        ref=f"{ref}-variant-{index}",
                        is_new=candidate.is_new,
                        title_hint=candidate.title_hint,
                    )
                )
            selected = selected[:1]

        sequence_by_chapter[chapter] += 1
        example_id = f"EX-C{chapter:02d}-{sequence_by_chapter[chapter]:03d}"
        exemplar = selected[0]
        title = title_for(exemplar)
        textbook_ref = f"第 {chapter} 章 / {ref}"
        origins = [candidate.source.rel for candidate in selected]

        if multi_file:
            target_dir = (
                ROUTINES_ROOT
                / "chapters"
                / CHAPTER_DIRS[chapter]
                / example_id.lower().replace("-", "_")
            )
            target_dir.mkdir(parents=True, exist_ok=True)
            target_paths = []
            for index, candidate in enumerate(
                sorted(selected, key=lambda item: item.source.path.name), start=1
            ):
                target = target_dir / f"source_{index:02d}.c"
                target_paths.append(target)
                body = normalize_and_fix(candidate.source.text, candidate.source.rel)
                target.write_text(body, encoding="utf-8", newline="\n")
        else:
            target_dir = ROUTINES_ROOT / "chapters" / CHAPTER_DIRS[chapter]
            target_dir.mkdir(parents=True, exist_ok=True)
            target = target_dir / (
                example_id.lower().replace("-", "_")
                + "_"
                + ascii_slug(exemplar.title_hint)
                + ".c"
            )
            body_text = (
                synthesize_pointer_sort_variant(exemplar.source)
                if exemplar.source.rel.endswith("20241112_1115/8.10.2.c")
                else exemplar.source.text
            )
            body = normalize_and_fix(body_text, exemplar.source.rel)
            target_paths = [target]
            target.write_text(body, encoding="utf-8", newline="\n")

        raw_texts = [path.read_text(encoding="utf-8") for path in target_paths]
        features = legacy_features(raw_texts)
        profile = "windows" if "conio" in features or "getch" in features else "portable"
        syntax_status, diagnostics = syntax_diagnostics(target_paths)
        if profile != "windows" and (features or syntax_status == "warning"):
            profile = "textbook"
        compatibility = compatibility_note(features, profile)
        build_mode = "c11-strict" if profile == "portable" else "gnu99-textbook"
        interaction = "deterministic" if (chapter, ref) in FIXTURE_SPECS else "manual"

        for path in target_paths:
            existing = path.read_text(encoding="utf-8")
            header = source_header(
                example_id,
                title,
                textbook_ref,
                CHAPTER_CONCEPTS[chapter],
                origins,
                build_mode,
                features,
                interaction,
                compatibility,
            )
            path.write_text(header + existing, encoding="utf-8", newline="\n")

        platforms, status = platform_metadata(features, profile)
        example = {
            "id": example_id,
            "title_zh": title,
            "kind": "comparison" if "variant" in ref else "concept",
            "chapter": chapter,
            "textbook_refs": [textbook_ref],
            "concepts": CHAPTER_CONCEPTS[chapter],
            "sources": [relpath(path) for path in target_paths],
            "build_profile": profile,
            "platforms": platforms,
            "legacy_features": features,
            "stdin_fixture": None,
            "expected_stdout": None,
            "status": status,
            "notes": compatibility,
            "compiler_diagnostics": syntax_status,
        }
        examples.append(example)

        destination = example["sources"][0] if len(example["sources"]) == 1 else str(
            Path(example["sources"][0]).parent.as_posix()
        )
        duplicate_group = f"C{chapter:02d}:{ref}"
        for candidate in group:
            is_selected = candidate in selected
            add_migration_entry(
                migration,
                candidate.source,
                audits,
                action="canonical_example" if is_selected else "merged_duplicate",
                reason=(
                    "选为章节权威例程"
                    if is_selected
                    else "与权威例程教材编号一致，已合并并保留来源记录"
                ),
                final_id=example_id,
                destination=destination,
                textbook_refs=[textbook_ref],
                concepts=CHAPTER_CONCEPTS[chapter],
                near_duplicate_group=duplicate_group,
                question_like=False,
            )

    for project_name, spec in PROJECT_SPECS.items():
        project_dir = ROUTINES_ROOT / "projects" / project_name
        project_dir.mkdir(parents=True, exist_ok=True)
        previous_id = None
        for step, source_rel in enumerate(spec["paths"], start=1):
            source = source_by_rel[source_rel]
            example_id = f"PJ-{spec['prefix']}-{step:02d}"
            title = f"{spec['title']}：步骤 {step}"
            target = project_dir / f"step_{step:02d}.c"
            body = normalize_and_fix(source.text, source.rel)
            features = legacy_features([body])
            profile = "windows" if "conio" in features or "getch" in features else "textbook"
            compatibility = compatibility_note(features, profile)
            platforms, status = platform_metadata(features, profile)
            header = source_header(
                example_id,
                title,
                "综合案例",
                ["综合应用", "渐进式开发"],
                [source.rel],
                "gnu99-textbook",
                features,
                "manual",
                compatibility,
            )
            target.write_text(header + body, encoding="utf-8", newline="\n")
            syntax_status, _ = syntax_diagnostics([target])
            example = {
                "id": example_id,
                "title_zh": title,
                "kind": "project_step",
                "chapter": None,
                "textbook_refs": ["综合案例"],
                "concepts": ["综合应用", "渐进式开发"],
                "sources": [relpath(target)],
                "build_profile": profile,
                "platforms": platforms,
                "legacy_features": features,
                "stdin_fixture": None,
                "expected_stdout": None,
                "status": status,
                "notes": (
                    compatibility
                    + (
                        f" 相较 {previous_id} 增加下一阶段功能。"
                        if previous_id
                        else " 项目起始步骤。"
                    )
                ),
                "compiler_diagnostics": syntax_status,
            }
            examples.append(example)
            add_migration_entry(
                migration,
                source,
                audits,
                action="canonical_project_step",
                reason=f"纳入 {spec['title']} 的第 {step} 步",
                final_id=example_id,
                destination=relpath(target),
                textbook_refs=["综合案例"],
                concepts=["综合应用", "渐进式开发"],
                near_duplicate_group=None,
                question_like=False,
            )
            previous_id = example_id

    missing = sorted(set(source_by_rel) - set(migration))
    extra = sorted(set(migration) - set(source_by_rel))
    if missing or extra:
        raise RuntimeError(f"Migration coverage mismatch; missing={missing}, extra={extra}")

    catalog = {
        "schema_version": 1,
        "title": "C 语言程序设计例程目录",
        "default_profile": "textbook",
        "source_count": len(sources),
        "example_count": len(examples),
        "examples": sorted(examples, key=lambda item: str(item["id"])),
    }
    migration_document = {
        "schema_version": 1,
        "source_roots": [root.name for root in SOURCE_ROOTS],
        "source_count": len(sources),
        "coverage_count": len(migration),
        "allowed_actions": [
            "canonical_example",
            "canonical_project_step",
            "merged_duplicate",
            "question_bank_pending",
            "discarded_after_review",
        ],
        "entries": [migration[key] for key in sorted(migration)],
    }
    return [catalog], [migration_document]


def main() -> int:
    catalogs, migrations = build_examples()
    (MIGRATION_ROOT / "examples-migration.json").write_text(
        json.dumps(migrations[0], ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(
        f"Generated {catalogs[0]['example_count']} routines and "
        f"{migrations[0]['coverage_count']} migration entries."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
