"""Build a machine-readable register from actual JSON files on disk."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from device_common import load_json, sha256_file, write_json


def build_register(root: str | Path) -> dict[str, Any]:
    base = Path(root)
    records: list[dict[str, Any]] = []
    for path in sorted(base.rglob("*.json")):
        try:
            data = load_json(path)
        except Exception as exc:  # pragma: no cover - reported as register evidence
            records.append({"path": str(path), "status": "Gagal", "error": str(exc)})
            continue
        questions = data.get("soal", []) if isinstance(data, dict) else []
        records.append({
            "path": str(path),
            "id_indikator": data.get("id_indikator") if isinstance(data, dict) else None,
            "jumlah_soal": len(questions) if isinstance(questions, list) else 0,
            "status_pengembangan": "Draf",
            "status_verifikasi": "Belum diuji",
            "sha256": sha256_file(path),
        })
    return {"root": str(base), "records": records, "jumlah_berkas": len(records)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root")
    parser.add_argument("output")
    args = parser.parse_args()
    write_json(args.output, build_register(args.root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

