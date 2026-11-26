"""Validate the fixed 14-attribute question structure and conditional rules."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from device_common import load_json

QUESTION_FIELDS = {
    "id_soal", "id_indikator", "jenis_soal", "pertanyaan", "pilihan",
    "kunci_jawaban", "panduan_orang_tua", "penjelasan_konsep", "penerapan_nyata",
    "butuh_gambar", "image_description", "image_spec", "metode_penilaian", "rubrik_penilaian",
}
KINDS = {"DIA", "PGT", "PYN", "CU"}
METHODS = {"OTOMATIS", "ORANG_TUA"}


def validate_data(data: Any, require_complete: bool = False) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["root harus berupa objek JSON"]
    indicator_id = data.get("id_indikator")
    questions = data.get("soal")
    if not isinstance(indicator_id, str) or not indicator_id.strip():
        errors.append("root.id_indikator wajib berupa teks tidak kosong")
    if not isinstance(questions, list):
        return errors + ["root.soal wajib berupa array"]
    seen: set[str] = set()
    counts = {kind: 0 for kind in KINDS}
    for index, item in enumerate(questions, start=1):
        prefix = f"soal[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix} harus berupa objek")
            continue
        keys = set(item)
        missing = QUESTION_FIELDS - keys
        extra = keys - QUESTION_FIELDS
        errors.extend(f"{prefix} atribut wajib hilang: {key}" for key in sorted(missing))
        errors.extend(f"{prefix} atribut tidak diizinkan: {key}" for key in sorted(extra))
        if missing:
            continue
        qid = item["id_soal"]
        if not isinstance(qid, str) or not qid.strip():
            errors.append(f"{prefix}.id_soal wajib teks")
        elif qid in seen:
            errors.append(f"{prefix}.id_soal duplikat: {qid}")
        seen.add(qid)
        if item["id_indikator"] != indicator_id:
            errors.append(f"{prefix}.id_indikator tidak sama dengan root")
        kind = item["jenis_soal"]
        if kind not in KINDS:
            errors.append(f"{prefix}.jenis_soal tidak valid")
        else:
            counts[kind] += 1
        if not isinstance(item["pertanyaan"], str) or not item["pertanyaan"].strip():
            errors.append(f"{prefix}.pertanyaan wajib teks tidak kosong")
        if not isinstance(item["panduan_orang_tua"], str) or not item["panduan_orang_tua"].strip():
            errors.append(f"{prefix}.panduan_orang_tua wajib teks tidak kosong")
        method = item["metode_penilaian"]
        if method not in METHODS:
            errors.append(f"{prefix}.metode_penilaian tidak valid")
        if method == "OTOMATIS":
            choices = item["pilihan"]
            if not isinstance(choices, dict) or set(choices) != {"A", "B", "C"}:
                errors.append(f"{prefix}.pilihan harus memuat tepat A, B, C")
            if item["kunci_jawaban"] not in {"A", "B", "C"}:
                errors.append(f"{prefix}.kunci_jawaban harus A, B, atau C")
            if item["rubrik_penilaian"] is not None:
                errors.append(f"{prefix}.rubrik_penilaian harus null untuk OTOMATIS")
        elif method == "ORANG_TUA":
            if item["pilihan"] is not None or item["kunci_jawaban"] is not None:
                errors.append(f"{prefix}.pilihan dan kunci_jawaban harus null untuk ORANG_TUA")
            if not item["rubrik_penilaian"]:
                errors.append(f"{prefix}.rubrik_penilaian wajib terisi untuk ORANG_TUA")
        if kind in {"DIA", "CU"}:
            if item["penjelasan_konsep"] is not None or item["penerapan_nyata"] is not None:
                errors.append(f"{prefix} penjelasan/penerapan harus null untuk {kind}")
        if kind in {"PGT", "PYN"}:
            if not isinstance(item["penjelasan_konsep"], str) or not item["penjelasan_konsep"].strip():
                errors.append(f"{prefix}.penjelasan_konsep wajib untuk {kind}")
            if not isinstance(item["penerapan_nyata"], str) or not item["penerapan_nyata"].strip():
                errors.append(f"{prefix}.penerapan_nyata wajib untuk {kind}")
        if not isinstance(item["butuh_gambar"], bool):
            errors.append(f"{prefix}.butuh_gambar harus boolean")
        elif item["butuh_gambar"]:
            if not isinstance(item["image_description"], str) or not item["image_description"].strip():
                errors.append(f"{prefix}.image_description wajib jika butuh_gambar=true")
            if item["image_spec"] not in {"2D", "3D"}:
                errors.append(f"{prefix}.image_spec harus 2D atau 3D")
        elif item["image_description"] is not None or item["image_spec"] is not None:
            errors.append(f"{prefix} image_description dan image_spec harus null jika tanpa gambar")
    if require_complete:
        if len(questions) != 40:
            errors.append(f"kelengkapan penuh memerlukan 40 soal, ditemukan {len(questions)}")
        for kind, count in counts.items():
            if count != 10:
                errors.append(f"jenis {kind} memerlukan 10 soal, ditemukan {count}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("--require-complete", action="store_true")
    args = parser.parse_args()
    errors = validate_data(load_json(args.input), args.require_complete)
    print(json.dumps({"valid": not errors, "errors": errors}, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())

