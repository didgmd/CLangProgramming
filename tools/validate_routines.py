#!/usr/bin/env python3
"""Validate routine metadata, repository boundaries, MinGW builds, and behavior."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True

from generate_routine_index import INDEX_PATH, render_index
from routine_common import MetadataError, ROOT, ROUTINES_ROOT, Routine, scan_routines


LOCAL_REFERENCE_NAMES = {
    "C程序设计 (第五版)_9787302481447.pdf",
    "C程序设计 (第五版) 学习辅导_9787302480877.pdf",
    "C语言程序设计 - 教学大纲.doc",
}
FEATURE_PATTERNS = {
    "gets": r"\bgets\s*\(",
    "scanf_s": r"\bscanf_s\s*\(",
    "conio": r"#\s*include\s*[<\"]conio\.h[>\"]",
    "getch": r"\b_?getch\s*\(",
    "system-pause": r"system\s*\(\s*\"pause\"",
    "msvc-warning-pragma": r"#\s*pragma\s+warning",
    "msvc-crt-compat": r"_CRT_SECURE_NO_WARNINGS",
    "malloc-h": r"#\s*include\s*[<\"]malloc\.h[>\"]",
}
BEHAVIOR_CASES = {
    "EX-C01-001": ("", "This is a C program.\n"),
    "EX-C02-003": ("", "p is 1, i is 2\np is 2, i is 3\np is 6, i is 4\np is 24, i is 5\n"),
    "EX-C03-001": ("", "f=64.000000\nc=17.777779\n"),
    "EX-C04-001": ("1 -3 2\n", "real roots:\nx1=   2.00\nx2=   1.00\n"),
    "EX-C05-001": ("", "sum=5050\n"),
    "EX-C06-001": ("", "9 8 7 6 5 4 3 2 1 0 \n"),
    "EX-C07-001": ("", "******************\nHow do you do!\n******************\n"),
    "EX-C08-001": ("", "a=100,b=10\n*pointer_1=100,*pointer_2=10\n"),
    "EX-C09-001": ("", "NO.:10101\nname:Li Lin\nsex:M\naddress:123 Beijing Road\n"),
}
MAIN_PATTERN = re.compile(r"\b(?:int|void)\s+main\s*\(")


class ValidationError(RuntimeError):
    """Raised when a repository invariant or build check fails."""


def run(
    command: list[str],
    *,
    cwd: Path | None = None,
    stdin: str | None = None,
    timeout: int = 30,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=cwd,
        input=stdin,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
        check=False,
    )


def detect_features(text: str) -> set[str]:
    return {name for name, pattern in FEATURE_PATTERNS.items() if re.search(pattern, text)}


def validate_layout() -> None:
    retired_build_file = "C" + "MakeLists.txt"
    forbidden = [
        ROOT / "examples",
        ROOT / retired_build_file,
        ROUTINES_ROOT / "catalog.json",
        ROUTINES_ROOT / "tests",
        ROUTINES_ROOT / retired_build_file,
    ]
    existing = [str(path.relative_to(ROOT)) for path in forbidden if path.exists()]
    existing.extend(str(path.relative_to(ROOT)) for path in ROOT.rglob(retired_build_file))
    if existing:
        raise ValidationError(
            "Removed build/catalog surfaces still exist: "
            + ", ".join(sorted(set(existing)))
        )

    process_dirs = [
        ROOT / "build-audit",
        ROOT / ".routine-validation-tmp",
        *ROOT.glob("build-validation-*"),
        *ROOT.rglob("__pycache__"),
    ]
    residue_dirs = [path for path in process_dirs if path.exists()]
    if residue_dirs:
        raise ValidationError(
            "Process directories remain: "
            + ", ".join(str(path.relative_to(ROOT)) for path in residue_dirs)
        )
    residue_files = []
    for suffix in ("*.exe", "*.o", "*.obj", "*.pyc"):
        residue_files.extend(
            path for path in ROOT.rglob(suffix) if ".git" not in path.parts
        )
    if residue_files:
        raise ValidationError(
            "Compiled artifacts remain in repository: "
            + ", ".join(str(path.relative_to(ROOT)) for path in residue_files[:20])
        )

def validate_reference_boundary() -> None:
    git = shutil.which("git")
    if not git:
        raise ValidationError("git is required for the local reference boundary check")
    tracked = run([git, "ls-files", "--", "*.pdf", "*.doc"], cwd=ROOT)
    if tracked.returncode != 0:
        raise ValidationError(
            f"Cannot inspect tracked reference files: {tracked.stderr.strip()}"
        )
    tracked_names = {
        Path(line).name for line in tracked.stdout.splitlines() if line.strip()
    }
    forbidden = tracked_names & LOCAL_REFERENCE_NAMES
    if forbidden:
        raise ValidationError(
            "Local reference file is tracked: " + ", ".join(sorted(forbidden))
        )
    for name in LOCAL_REFERENCE_NAMES:
        ignored = run([git, "check-ignore", "-q", "--", name], cwd=ROOT)
        if ignored.returncode != 0:
            raise ValidationError(
                f"Local reference file is not protected by .gitignore: {name}"
            )


def validate_index(routines: dict[str, Routine]) -> None:
    if not INDEX_PATH.is_file():
        raise ValidationError("Missing generated index: 例程/README.md")
    current = INDEX_PATH.read_text(encoding="utf-8")
    expected = render_index(routines)
    if current != expected:
        raise ValidationError(
            "例程/README.md is out of date; run tools/generate_routine_index.py"
        )


def validate_routine_structure(
    routines: dict[str, Routine], texts: dict[Path, str]
) -> None:
    if len(routines) != 195:
        raise ValidationError(f"Routine ID count is {len(routines)}, expected 195")
    strict_count = sum(item.build_mode == "c11-strict" for item in routines.values())
    textbook_count = sum(item.build_mode == "gnu99-textbook" for item in routines.values())
    if (strict_count, textbook_count) != (104, 91):
        raise ValidationError(
            f"Build mode counts are strict={strict_count}, textbook={textbook_count}; "
            "expected 104/91"
        )
    deterministic = {item.routine_id for item in routines.values() if item.interaction == "deterministic"}
    if deterministic != set(BEHAVIOR_CASES):
        raise ValidationError(
            f"Behavior case mismatch: declared={sorted(deterministic)}, "
            f"embedded={sorted(BEHAVIOR_CASES)}"
        )

    for routine in routines.values():
        combined = "\n".join(texts[path] for path in routine.sources)
        actual_features = detect_features(combined)
        declared_features = set(routine.legacy_features)
        if actual_features != declared_features:
            raise ValidationError(
                f"Legacy feature mismatch for {routine.routine_id}: "
                f"declared={sorted(declared_features)}, actual={sorted(actual_features)}"
            )
        main_count = sum(len(MAIN_PATTERN.findall(texts[path])) for path in routine.sources)
        if main_count != 1:
            raise ValidationError(
                f"{routine.routine_id} has {main_count} main() definitions; expected exactly one"
            )
        if "gets" in actual_features:
            if "C11" not in routine.compatibility or "生产程序" not in routine.compatibility:
                raise ValidationError(f"gets() risk boundary is incomplete for {routine.routine_id}")
            if routine.build_mode != "gnu99-textbook":
                raise ValidationError(f"gets() must use gnu99-textbook: {routine.routine_id}")
        if actual_features & {"conio", "getch"} and routine.build_mode != "gnu99-textbook":
            raise ValidationError(f"MinGW API routine has wrong mode: {routine.routine_id}")


def validate_retired_sources_absent() -> None:
    retired = [
        ROOT / "2023-2024-1",
        ROOT / "2024-2025-1",
        ROOT / "migration",
        ROOT / "tools" / "migrate_examples.py",
        ROOT / "tools" / "source_fixes.py",
    ]
    existing = [str(path.relative_to(ROOT)) for path in retired if path.exists()]
    if existing:
        raise ValidationError(
            "Retired migration sources remain: " + ", ".join(sorted(existing))
        )


def validate_mingw(gcc_argument: str) -> tuple[str, str]:
    gcc = shutil.which(gcc_argument) if Path(gcc_argument).name == gcc_argument else gcc_argument
    if not gcc or not Path(gcc).is_file():
        raise ValidationError(f"MinGW GCC is not available: {gcc_argument}")
    target = run([gcc, "-dumpmachine"])
    if target.returncode != 0 or "mingw" not in target.stdout.lower():
        raise ValidationError(f"Compiler is not MinGW-w64 GCC: {target.stdout.strip() or target.stderr.strip()}")
    version_result = run([gcc, "-dumpfullversion", "-dumpversion"])
    match = re.search(r"\d+(?:\.\d+)+", version_result.stdout)
    if not match:
        raise ValidationError("Cannot determine GCC version")
    version = match.group(0)
    version_tuple = tuple(int(part) for part in version.split("."))
    if version_tuple < (8, 1):
        raise ValidationError(f"GCC {version} is older than the 8.1 baseline")
    return str(Path(gcc).resolve()), version


def unexpected_warnings(stderr: str, features: set[str]) -> list[str]:
    unexpected = []
    for line in stderr.splitlines():
        lower = line.lower()
        if "warning:" not in lower:
            continue
        if "ignoring #pragma warning" in lower and "msvc-warning-pragma" in features:
            continue
        if "gets" in lower and "gets" in features and (
            "dangerous" in lower or "deprecated" in lower or "warning" in lower
        ):
            continue
        unexpected.append(line.strip())
    return unexpected


def remove_validation_temp(path: Path) -> None:
    expected_parent = ROOT.resolve()
    resolved = path.resolve()
    if resolved.parent != expected_parent or resolved.name != ".routine-validation-tmp":
        raise ValidationError(f"Refusing to clean unsafe temporary path: {resolved}")
    shell = shutil.which("pwsh") or shutil.which("powershell")
    if not shell:
        raise ValidationError(f"PowerShell is required to clean temporary path: {resolved}")
    escaped = str(resolved).replace("'", "''")
    cleanup = run(
        [
            shell,
            "-NoProfile",
            "-NonInteractive",
            "-Command",
            f"Remove-Item -LiteralPath '{escaped}' -Recurse -Force",
        ],
        timeout=30,
    )
    if cleanup.returncode != 0:
        raise ValidationError(
            f"Cannot clean temporary validation directory: {resolved}: "
            f"{cleanup.stderr.strip()}"
        )

def compile_and_test(
    routines: dict[str, Routine], gcc: str, selected_id: str | None
) -> tuple[int, int]:
    selected = [routines[selected_id]] if selected_id is not None else list(routines.values())
    failures: list[str] = []
    compiled = 0
    tested = 0
    temp_path = ROOT / ".routine-validation-tmp"
    if temp_path.exists():
        raise ValidationError(f"Previous validation residue remains: {temp_path}")
    temp_path.mkdir()
    try:
        bin_dir = temp_path / "bin"
        run_root = temp_path / "run"
        bin_dir.mkdir()
        run_root.mkdir()
        for position, routine in enumerate(selected, start=1):
            safe_name = re.sub(r"[^a-z0-9]+", "_", routine.routine_id.lower()).strip("_")
            executable = bin_dir / f"{safe_name}.exe"
            if routine.build_mode == "c11-strict":
                flags = ["-std=c11", "-Wall", "-Wextra", "-Wpedantic", "-Werror"]
            else:
                flags = ["-std=gnu99", "-Wall", "-Wextra"]
            command = [
                gcc,
                *flags,
                "-fdiagnostics-color=never",
                *(str(path) for path in routine.sources),
                "-lm",
                "-o",
                str(executable),
            ]
            completed = run(command, cwd=temp_path, timeout=30)
            if completed.returncode != 0:
                failures.append(
                    f"{routine.routine_id} compile failed:\n{completed.stderr.strip()}"
                )
                continue
            warnings = unexpected_warnings(completed.stderr, set(routine.legacy_features))
            if warnings:
                failures.append(
                    f"{routine.routine_id} has unexpected warnings:\n" + "\n".join(warnings)
                )
                continue
            compiled += 1
            behavior = BEHAVIOR_CASES.get(routine.routine_id)
            if behavior is not None:
                working_dir = run_root / safe_name
                working_dir.mkdir()
                executed = run(
                    [str(executable)], cwd=working_dir, stdin=behavior[0], timeout=8
                )
                actual = executed.stdout.replace("\r\n", "\n")
                if executed.returncode != 0:
                    failures.append(
                        f"{routine.routine_id} run failed: {executed.stderr.strip()}"
                    )
                elif actual != behavior[1]:
                    failures.append(
                        f"{routine.routine_id} output mismatch\n"
                        f"EXPECTED:\n{behavior[1]}ACTUAL:\n{actual}"
                    )
                else:
                    tested += 1
            if position % 25 == 0 or position == len(selected):
                print(
                    f"BUILD PROGRESS: {position}/{len(selected)}, "
                    f"compiled={compiled}, behaviors={tested}, failures={len(failures)}",
                    flush=True,
                )
    finally:
        remove_validation_temp(temp_path)
    if failures:
        preview = "\n\n".join(failures[:20])
        suffix = f"\n\n... {len(failures) - 20} more failures" if len(failures) > 20 else ""
        raise ValidationError(f"Build/behavior failures ({len(failures)}):\n{preview}{suffix}")
    return compiled, tested

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", dest="routine_id")
    parser.add_argument("--gcc", default="gcc")
    args = parser.parse_args()
    try:
        validate_layout()
        routines, texts = scan_routines()
        validate_routine_structure(routines, texts)
        validate_retired_sources_absent()
        validate_reference_boundary()
        validate_index(routines)
        if args.routine_id and args.routine_id not in routines:
            raise ValidationError(f"Unknown routine ID: {args.routine_id}")
        gcc, version = validate_mingw(args.gcc)
        compiled, tested = compile_and_test(routines, gcc, args.routine_id)
        scope = args.routine_id or "all"
        print(
            f"PASS: routines={len(routines)}, historical_sources=git-history, "
            f"compiler=MinGW GCC {version}, scope={scope}, compiled={compiled}, behaviors={tested}"
        )
        return 0
    except (ValidationError, MetadataError, subprocess.TimeoutExpired) as exc:
        print(f"VALIDATION FAILED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
