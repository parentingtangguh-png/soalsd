from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from antidupe_detector import detect
from competency_extractor import extract
from html_generator import generate_html
from question_id_generator import generate_id
from image_generator import render_svg
from json_validator import validate_data
from register_manager import build_register


FIXTURES = ROOT / "tests" / "fixtures"


class DeviceTests(unittest.TestCase):
    def test_competency_extractor_preserves_explicit_fields(self):
        result = extract(FIXTURES / "indicator_manifest.json")
        self.assertEqual(result["records"][0]["rumusan"], "Membilang benda satu per satu dalam suatu kumpulan.")
        self.assertEqual(result["records"][0]["kategori"], "I")

    def test_id_generator(self):
        self.assertEqual(
            generate_id("MTK", "A", 1, "B.1", 1, 1, "DIA", 1),
            "SOAL-MTK-A-K1-B.1-KM01-I01-DIA-01",
        )

    def test_json_validator_accepts_partial_valid_data(self):
        data = json.loads((FIXTURES / "questions.json").read_text(encoding="utf-8"))
        self.assertEqual(validate_data(data), [])
        self.assertTrue(validate_data(data, require_complete=True))

    def test_image_generator_is_actual_svg(self):
        svg = render_svg({"type": "circles", "count": 3})
        self.assertIn("<svg", svg)
        self.assertEqual(svg.count("<circle"), 3)

    def test_html_generator_contains_both_modes_and_data(self):
        data = json.loads((FIXTURES / "questions.json").read_text(encoding="utf-8"))
        html = generate_html(data)
        self.assertIn("Mode Pemeriksaan", html)
        self.assertIn("Mode Pengerjaan", html)
        self.assertIn("SOAL-MTK-A-K1-B.1-KM01-I01-DIA-01", html)

    def test_register_reads_actual_json(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "q.json"
            path.write_text((FIXTURES / "questions.json").read_text(encoding="utf-8"), encoding="utf-8")
            result = build_register(directory)
            self.assertEqual(result["jumlah_berkas"], 1)
            self.assertEqual(result["records"][0]["jumlah_soal"], 2)
            self.assertEqual(result["records"][0]["status_verifikasi"], "Belum diuji")

    def test_antidupe_index_has_separate_evidence_fields(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "q.json"
            path.write_text((FIXTURES / "questions.json").read_text(encoding="utf-8"), encoding="utf-8")
            result = detect(directory)
            self.assertEqual(len(result["records"]), 2)
            self.assertIn("content_hash", result["records"][0])
            self.assertEqual(result["status"], "Belum diuji pedagogis")


if __name__ == "__main__":
    unittest.main()

