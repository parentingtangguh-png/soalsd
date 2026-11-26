"""Extract explicit indicator rows from a Markdown table or JSON manifest.

The extractor never invents missing competency fields. Rows without an explicit
indicator identifier are skipped and reported by the caller.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from device_common import load_json, write_json

ALIASES = {
    "id_indikator": {"id indikator", "indikator id", "kode indikator", "id"},
    "id_tp": {"id tp", "tp", "kode tp"},
    "id_km": {"id km", "km", "kode km"},
    "id_cp": {"id cp", "cp", "kode cp"},
    "elemen": {"elemen", "elemen cp"},
    "rumusan": {"indikator", "rumusan indikator", "rumusan"},
    "kategori": {"kategori", "kategori kecakapan berpikir"},
}


def _clean_heading(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().strip("|").casefold())


def _split_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _is_separator(line: str) -> bool:
    return all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in _split_row(line))


def extract_markdown(text: str) -> tuple[list[dict[str, Any]], list[str]]:
    records: list[dict[str, Any]] = []
    skipped: list[str] = []
    lines = text.splitlines()
    for index in range(len(lines) - 2):
        if "|" not in lines[index] or not _is_separator(lines[index + 1]):
            continue
        headings = [_clean_heading(x) for x in _split_row(lines[index])]
        mapping: dict[int, str] = {}
        for position, heading in enumerate(headings):
            for target, aliases in ALIASES.items():
                if heading in aliases:
                    mapping[position] = target
                    break
        if "id_indikator" not in mapping.values():
            continue
        cursor = index + 2
        while cursor < len(lines) and "|" in lines[cursor] and lines[cursor].strip():
            if _is_separator(lines[cursor]):
                cursor += 1
                continue
            cells = _split_row(lines[cursor])
            record = {
                target: cells[position] if position < len(cells) else ""
                for position, target in mapping.items()
            }
            if record.get("id_indikator"):
                records.append(record)
            else:
                skipped.append(f"baris {cursor + 1}: id_indikator kosong")
            cursor += 1
    return records, skipped


def extract_json(value: Any) -> list[dict[str, Any]]:
    if isinstance(value, dict) and isinstance(value.get("indicators"), list):
        return [item for item in value["indicators"] if isinstance(item, dict)]
    if isinstance(value, list):
        return [item for item in value if isinstance(item, dict)]
    raise ValueError("JSON harus berupa array atau objek dengan kunci indicators")


def extract(path: str | Path) -> dict[str, Any]:
    source = Path(path)
    if source.suffix.casefold() == ".json":
        records = extract_json(load_json(source))
        return {"source": str(source), "records": records, "skipped": []}
    records, skipped = extract_markdown(source.read_text(encoding="utf-8"))
    return {"source": str(source), "records": records, "skipped": skipped}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    args = parser.parse_args()
    write_json(args.output, extract(args.input))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

