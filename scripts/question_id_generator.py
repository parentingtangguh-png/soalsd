"""Generate and validate the fixed Bank Soal question identity format."""

from __future__ import annotations

import argparse
import re

QUESTION_TYPES = {"DIA": "Diagnostik", "PGT": "Penguatan", "PYN": "Pengayaan", "CU": "Cek Ulang"}


def generate_id(
    kode_mapel: str,
    fase: str,
    kelas: int,
    kode_tp: str,
    nomor_km: int,
    nomor_indikator: int,
    kode_jenis: str,
    nomor_soal: int,
) -> str:
    if kode_jenis not in QUESTION_TYPES:
        raise ValueError("kode jenis harus DIA, PGT, PYN, atau CU")
    if not 1 <= kelas <= 6 or not 1 <= nomor_km <= 99 or not 1 <= nomor_indikator <= 99:
        raise ValueError("kelas, nomor KM, dan nomor indikator di luar rentang")
    if not 1 <= nomor_soal <= 10:
        raise ValueError("nomor soal harus 01 sampai 10")
    if not re.fullmatch(r"[A-Za-z0-9]+", kode_mapel) or not re.fullmatch(r"[A-Za-z0-9]+", fase):
        raise ValueError("kode mapel dan fase hanya boleh alfanumerik")
    if not re.fullmatch(r"[A-Za-z0-9.\-]+", kode_tp):
        raise ValueError("kode TP mengandung karakter yang tidak didukung")
    return (
        f"SOAL-{kode_mapel}-{fase}-K{kelas}-{kode_tp}-KM{nomor_km:02d}"
        f"-I{nomor_indikator:02d}-{kode_jenis}-{nomor_soal:02d}"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kode-mapel", required=True)
    parser.add_argument("--fase", required=True)
    parser.add_argument("--kelas", type=int, required=True)
    parser.add_argument("--kode-tp", required=True)
    parser.add_argument("--km", type=int, required=True)
    parser.add_argument("--indikator", type=int, required=True)
    parser.add_argument("--jenis", choices=sorted(QUESTION_TYPES), required=True)
    parser.add_argument("--nomor", type=int, required=True)
    args = parser.parse_args()
    print(generate_id(args.kode_mapel, args.fase, args.kelas, args.kode_tp, args.km, args.indikator, args.jenis, args.nomor))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

