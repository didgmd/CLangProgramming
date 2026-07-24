#!/usr/bin/env python3
"""Shared parser for source-header metadata in the routine library."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ROUTINES_ROOT = ROOT / "例程"
REQUIRED_HEADER_FIELDS = (
    "例程 ID",
    "标题",
    "教材位置",
    "知识点",
    "来源",
    "编译模式",
    "旧语法",
    "交互方式",
    "兼容性",
)
VALID_BUILD_MODES = {"c11-strict", "gnu99-textbook"}
VALID_INTERACTIONS = {"deterministic", "manual"}
ID_PATTERN = re.compile(r"^(?:EX-C\d{2}-\d{3}|PJ-[A-Z0-9]+-\d{2})$")
HEADER_LINE = re.compile(r"^\s*\*\s*([^：]+)：(.*)$")


class MetadataError(RuntimeError):
    """Raised when routine metadata is missing or inconsistent."""


@dataclass
class Routine:
    routine_id: str
    title: str
    textbook_ref: str
    concepts: tuple[str, ...]
    origins: str
    build_mode: str
    legacy_features: tuple[str, ...]
    interaction: str
    compatibility: str
    sources: list[Path] = field(default_factory=list)

    def metadata_key(self) -> tuple[object, ...]:
        return (
            self.title,
            self.textbook_ref,
            self.concepts,
            self.origins,
            self.build_mode,
            self.legacy_features,
            self.interaction,
            self.compatibility,
        )


def read_utf8_lf(path: Path) -> str:
    data = path.read_bytes()
    if data.startswith(b"\xef\xbb\xbf"):
        raise MetadataError(f"UTF-8 BOM is not allowed: {path.relative_to(ROOT)}")
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise MetadataError(f"Non-UTF-8 source: {path.relative_to(ROOT)}") from exc
    if "\ufffd" in text:
        raise MetadataError(f"Replacement character found: {path.relative_to(ROOT)}")
    if "\r" in text:
        raise MetadataError(f"Non-LF line ending found: {path.relative_to(ROOT)}")
    return text


def parse_source(path: Path) -> tuple[Routine, str]:
    text = read_utf8_lf(path)
    header_end = text.find("*/")
    if header_end < 0:
        raise MetadataError(f"Missing metadata header: {path.relative_to(ROOT)}")
    fields: dict[str, str] = {}
    for line in text[:header_end].splitlines():
        match = HEADER_LINE.match(line)
        if match:
            fields[match.group(1).strip()] = match.group(2).strip()
    missing = [name for name in REQUIRED_HEADER_FIELDS if not fields.get(name)]
    if missing:
        raise MetadataError(
            f"Incomplete metadata header in {path.relative_to(ROOT)}: {', '.join(missing)}"
        )
    routine_id = fields["例程 ID"]
    if not ID_PATTERN.fullmatch(routine_id):
        raise MetadataError(f"Invalid routine ID in {path.relative_to(ROOT)}: {routine_id}")
    build_mode = fields["编译模式"]
    if build_mode not in VALID_BUILD_MODES:
        raise MetadataError(f"Invalid build mode for {routine_id}: {build_mode}")
    interaction = fields["交互方式"]
    if interaction not in VALID_INTERACTIONS:
        raise MetadataError(f"Invalid interaction mode for {routine_id}: {interaction}")
    concepts = tuple(part for part in fields["知识点"].split("、") if part)
    legacy = () if fields["旧语法"] == "无" else tuple(
        part for part in fields["旧语法"].split("、") if part
    )
    return (
        Routine(
            routine_id=routine_id,
            title=fields["标题"],
            textbook_ref=fields["教材位置"],
            concepts=concepts,
            origins=fields["来源"],
            build_mode=build_mode,
            legacy_features=legacy,
            interaction=interaction,
            compatibility=fields["兼容性"],
        ),
        text,
    )


def scan_routines() -> tuple[dict[str, Routine], dict[Path, str]]:
    if not ROUTINES_ROOT.is_dir():
        raise MetadataError("Missing routine root: 例程/")
    routines: dict[str, Routine] = {}
    texts: dict[Path, str] = {}
    for path in sorted(ROUTINES_ROOT.rglob("*.c")):
        parsed, text = parse_source(path)
        texts[path] = text
        existing = routines.get(parsed.routine_id)
        if existing is None:
            routines[parsed.routine_id] = parsed
            existing = parsed
        elif existing.metadata_key() != parsed.metadata_key():
            raise MetadataError(
                f"Inconsistent metadata across sources for {parsed.routine_id}: "
                f"{path.relative_to(ROOT)}"
            )
        existing.sources.append(path)
    return dict(sorted(routines.items())), texts