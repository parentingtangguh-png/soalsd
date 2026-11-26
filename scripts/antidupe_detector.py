"""Create a reproducible duplicate/candidate index without pedagogical decisions."""

from __future__ import annotations

import argparse
import difflib
from pathlib import Path
from typing import Any

from device_common import load_json, normalize_text, sha256_file, sha256_text, write_json


def collect(root: str | Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in sorted(Path(root).rglob("*.json")):
        try:
            data = load_json(path)
        except Exception:
            continue
        for item in data.get("soal", []) if isinstance(data, dict) else []:
            if not isinstance(item, dict):
                continue
            content = " ".join(normalize_text(item.get(key)) for key in ("pertanyaan", "pilihan", "image_description"))
            structure = "|".join(str(item.get(key)) for key in ("jenis_soal", "metode_penilaian", "butuh_gambar"))
            records.append({
                "id_soal": item.get("id_soal"),
                "id_indikator": item.get("id_indikator"),
                "source": str(path),
                "content_hash": sha256_text(content),
                "structure_hash": sha256_text(structure),
                "question_text": normalize_text(item.get("pertanyaan")),
                "source_sha256": sha256_file(path),
            })
    return records


def detect(root: str | Path, threshold: float = 0.86) -> dict[str, Any]:
    records = collect(root)
    by_id: dict[str, list[str]] = {}
    by_content: dict[str, list[str]] = {}
    for record in records:
        by_id.setdefault(str(record["id_soal"]), []).append(record["source"])
        by_content.setdefault(record["content_hash"], []).append(record["id_soal"])
    conflicts = [{"id_soal": key, "sources": value} for key, value in by_id.items() if len(value) > 1]
    exact = [{"content_hash": key, "ids": value} for key, value in by_content.items() if len(value) > 1]
    candidates: list[dict[str, Any]] = []
    for left_index, left in enumerate(records):
        for right in records[left_index + 1:]:
            if left["content_hash"] == right["content_hash"]:
                continue
            ratio = difflib.SequenceMatcher(None, left["question_text"], right["question_text"]).ratio()
            if ratio >= threshold:
                candidates.append({"left": left["id_soal"], "right": right["id_soal"], "ratio": round(ratio, 4), "status": "Kandidat kemiripan; perlu verifikasi pedagogis"})
    return {"records": records, "id_conflicts": conflicts, "exact_duplicates": exact, "similarity_candidates": candidates, "threshold": threshold, "status": "Belum diuji pedagogis"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root")
    parser.add_argument("output")
    parser.add_argument("--threshold", type=float, default=0.86)
    args = parser.parse_args()
    write_json(args.output, detect(args.root, args.threshold))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

