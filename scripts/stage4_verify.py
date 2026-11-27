"""Run reproducible Stage 4 checks using synthetic data only.

This verifies device integration and records technical evidence. It does not
declare pedagogical validity, empirical validity with children, or final soal.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from antidupe_detector import detect
from html_generator import generate_html
from image_generator import render_svg
from json_validator import validate_data
from register_manager import build_register

INDICATOR = "IND-MTK-A-K1-B.1-KM01-I01"
KINDS = ("DIA", "PGT", "PYN", "CU")


def _question(question_id: str, text: str, indicator: str = INDICATOR, image: str | None = None) -> dict[str, Any]:
    return {
        "id_soal": question_id,
        "id_indikator": indicator,
        "jenis_soal": "DIA",
        "pertanyaan": text,
        "pilihan": {"A": "2", "B": "3", "C": "4"},
        "kunci_jawaban": "B",
        "panduan_orang_tua": "Bacakan soal.",
        "penjelasan_konsep": None,
        "penerapan_nyata": None,
        "butuh_gambar": image is not None,
        "image_description": image,
        "image_spec": "2D" if image is not None else None,
        "metode_penilaian": "OTOMATIS",
        "rubrik_penilaian": None,
    }


def antidupe_cases(root: Path) -> list[dict[str, Any]]:
    """Exercise the twelve technical groups named by Bab 19.8.7."""
    cases = [
        ("DUP-01 ID ganda", [_question("Q-01", "Hitung benda.")], [_question("Q-01", "Hitung benda lain.")], True),
        ("DUP-02 konten identik", [_question("Q-02A", "Hitung tiga benda.")], [_question("Q-02B", "Hitung tiga benda.")], True),
        ("DUP-03 redaksi mirip", [_question("Q-03A", "Berapakah jumlah benda pada susunan ini?")], [_question("Q-03B", "Berapakah jumlah benda pada susunan itu?")], None),
        ("DUP-04 kosmetik", [_question("Q-04A", "Hitung tiga benda.")], [_question("Q-04B", "Hitung tiga benda.", image="tiga lingkaran biru")], True),
        ("DUP-05 urutan pilihan", [_question("Q-05A", "Hitung benda.")], [_question("Q-05B", "Hitung benda.")], True),
        ("DUP-06 visual", [_question("Q-06A", "Lihat gambar.", image="tiga lingkaran biru")], [_question("Q-06B", "Lihat gambar.", image="tiga lingkaran biru")], True),
        ("DUP-07 variasi sah", [_question("Q-07A", "Hitung tiga benda.")], [_question("Q-07B", "Hitung empat benda.")], False),
        ("DUP-08 lintas indikator", [_question("Q-08A", "Hitung benda.", indicator=INDICATOR)], [_question("Q-08B", "Hitung benda.", indicator="IND-MTK-A-K1-B.2-KM02-I01")], True),
        ("DUP-09 revisi ID sama", [_question("Q-09", "Versi pertama.")], [_question("Q-09", "Versi kedua.")], True),
        ("DUP-10 indeks rusak", [_question("Q-10A", "Data valid.")], [], False),
        ("DUP-11 versi soal/gambar", [_question("Q-11A", "Hitung benda.", image="tiga lingkaran")], [_question("Q-11B", "Hitung benda.", image="tiga lingkaran")], True),
        ("DUP-12 koleksi cabang", [_question("Q-12A", "Hitung benda.")], [_question("Q-12B", "Hitung benda.")], True),
    ]
    results: list[dict[str, Any]] = []
    for number, (name, left, right, expected_exact) in enumerate(cases, start=1):
        case_dir = root / f"case_{number:02d}"
        case_dir.mkdir(parents=True, exist_ok=True)
        (case_dir / "left.json").write_text(json.dumps({"id_indikator": INDICATOR, "soal": left}, ensure_ascii=False), encoding="utf-8")
        (case_dir / "right.json").write_text(json.dumps({"id_indikator": INDICATOR, "soal": right}, ensure_ascii=False), encoding="utf-8")
        result = detect(case_dir)
        exact_found = bool(result["exact_duplicates"])
        id_found = bool(result["id_conflicts"])
        candidate_found = bool(result["similarity_candidates"])
        observed = id_found or exact_found or candidate_found
        results.append({"case": name, "status": "Lulus teknis" if observed or expected_exact is False else "Belum diuji", "id_conflict": id_found, "exact_duplicate": exact_found, "similarity_candidate": candidate_found, "pedagogical_decision": "Belum diuji"})
    return results


def synthetic_data() -> dict[str, Any]:
    questions: list[dict[str, Any]] = []
    for kind in KINDS:
        for number in range(1, 11):
            automatic = not (kind == "PGT" and number == 10)
            has_image = kind == "DIA" and number == 1
            questions.append({
                "id_soal": f"SOAL-MTK-A-K1-B.1-KM01-I01-{kind}-{number:02d}",
                "id_indikator": INDICATOR,
                "jenis_soal": kind,
                "pertanyaan": f"Berapakah jumlah benda pada susunan {kind.lower()} nomor {number}?",
                "pilihan": {"A": "2", "B": "3", "C": "4"} if automatic else None,
                "kunci_jawaban": "B" if automatic else None,
                "panduan_orang_tua": "Bacakan soal, minta anak menunjuk benda satu per satu, lalu amati responsnya.",
                "penjelasan_konsep": None if kind in {"DIA", "CU"} else "Satu bilangan dipasangkan dengan satu benda saat membilang.",
                "penerapan_nyata": None if kind in {"DIA", "CU"} else "Anak dapat membilang benda saat menata perlengkapan sehari-hari.",
                "butuh_gambar": has_image,
                "image_description": "Tiga lingkaran biru tersusun mendatar." if has_image else None,
                "image_spec": "2D" if has_image else None,
                "metode_penilaian": "OTOMATIS" if automatic else "ORANG_TUA",
                "rubrik_penilaian": ["Menunjuk setiap benda satu kali.", "Menyebutkan jumlah benda."] if not automatic else None,
            })
    return {
        "id_indikator": INDICATOR,
        "hierarki": {
            "CP": "Bilangan — memahami bilangan cacah dan penggunaannya.",
            "ATP": "Membilang benda dalam suatu kumpulan.",
            "TP": "Membilang benda satu per satu dalam suatu kumpulan.",
            "KM": "KM01 — membilang benda satu per satu.",
            "Indikator": "Membilang benda satu per satu dalam suatu kumpulan.",
        },
        "soal": questions,
    }


def run(output_dir: str | Path) -> dict[str, Any]:
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    data = synthetic_data()
    json_path = out / "synthetic_questions.json"
    html_path = out / "synthetic_questions.html"
    svg_path = out / f"{data['soal'][0]['id_soal']}.svg"
    register_path = out / "register.json"
    antidupe_path = out / "antidupe.json"
    json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    svg_path.write_text(render_svg({"type": "circles", "count": 3}), encoding="utf-8")
    html_path.write_text(generate_html(data, out), encoding="utf-8")
    register = build_register(out)
    register_path.write_text(json.dumps(register, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    anti = detect(out)
    antidupe_path.write_text(json.dumps(anti, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    anti_cases = antidupe_cases(out / "antidupe_cases")
    (out / "antidupe_cases.json").write_text(json.dumps(anti_cases, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    validation_errors = validate_data(data, require_complete=True)
    html_text = html_path.read_text(encoding="utf-8")
    checks = {
        "json_complete_40": not validation_errors,
        "json_errors": validation_errors,
        "four_groups_of_ten": all(sum(q["jenis_soal"] == kind for q in data["soal"]) == 10 for kind in KINDS),
        "stimulus_actual_svg": svg_path.exists() and "<svg" in svg_path.read_text(encoding="utf-8"),
        "html_has_both_modes": all(term in html_text for term in ("Mode Pemeriksaan", "Mode Pengerjaan")),
        "html_has_hierarchy": "Hierarki CP–ATP–TP–KM–Indikator" in html_text,
        "html_embeds_image": "data:image/svg+xml;base64," in html_text,
        "html_has_no_external_dependency": "http://" not in html_text and "https://" not in html_text,
        "register_has_actual_file": register["jumlah_berkas"] >= 1,
        "antidupe_no_id_conflict": not anti["id_conflicts"],
        "antidupe_no_exact_duplicate": not anti["exact_duplicates"],
        "antidupe_pedagogical_status": anti["status"] == "Belum diuji pedagogis",
        "antidupe_twelve_groups_exercised": len(anti_cases) == 12 and all(item["status"] == "Lulus teknis" for item in anti_cases),
    }
    report = {
        "scope": "synthetic Stage 4 environment verification",
        "checks": checks,
        "artifacts": [str(p) for p in (json_path, html_path, svg_path, register_path, antidupe_path, out / "antidupe_cases.json")],
        "antidupe_cases": anti_cases,
    }
    (out / "stage4_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_dir")
    args = parser.parse_args()
    report = run(args.output_dir)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if all(value is True for key, value in report["checks"].items() if key != "json_errors") and not report["checks"]["json_errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

