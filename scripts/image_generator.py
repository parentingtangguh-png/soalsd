"""Create deterministic SVG teaching stimuli from a small JSON specification."""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path
from typing import Any


def _esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


def render_svg(spec: dict[str, Any]) -> str:
    kind = spec.get("type")
    if kind == "circles":
        count = int(spec.get("count", 0))
        if not 1 <= count <= 50:
            raise ValueError("count circles harus 1 sampai 50")
        cols = min(10, count)
        rows = (count + cols - 1) // cols
        parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {cols * 52} {rows * 52}" role="img">']
        for i in range(count):
            x, y = (i % cols) * 52 + 26, (i // cols) * 52 + 26
            parts.append(f'<circle cx="{x}" cy="{y}" r="18" fill="#4f46e5"/>')
        return "".join(parts) + "</svg>"
    if kind == "rectangles":
        count = int(spec.get("count", 0))
        if not 1 <= count <= 30:
            raise ValueError("count rectangles harus 1 sampai 30")
        parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {count * 42} 54" role="img">']
        for i in range(count):
            parts.append(f'<rect x="{i * 42 + 3}" y="5" width="36" height="44" rx="4" fill="#0f766e"/>')
        return "".join(parts) + "</svg>"
    if kind == "number_line":
        start, end = int(spec["start"]), int(spec["end"])
        if end <= start or end - start > 30:
            raise ValueError("rentang garis bilangan tidak valid")
        width = (end - start) * 44 + 40
        parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} 90" role="img">', f'<line x1="20" y1="45" x2="{width - 20}" y2="45" stroke="#111827" stroke-width="3"/>']
        points = {int(x) for x in spec.get("points", [])}
        for value in range(start, end + 1):
            x = 20 + (value - start) * 44
            parts.append(f'<line x1="{x}" y1="36" x2="{x}" y2="54" stroke="#111827" stroke-width="2"/>')
            parts.append(f'<text x="{x}" y="76" text-anchor="middle" font-size="14">{value}</text>')
            if value in points:
                parts.append(f'<circle cx="{x}" cy="45" r="8" fill="#dc2626"/>')
        return "".join(parts) + "</svg>"
    if kind == "grid":
        rows, cols = int(spec["rows"]), int(spec["cols"])
        if not 1 <= rows <= 12 or not 1 <= cols <= 12:
            raise ValueError("ukuran grid harus 1 sampai 12")
        parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {cols * 42} {rows * 42}" role="img">']
        for row in range(rows):
            for col in range(cols):
                parts.append(f'<rect x="{col * 42}" y="{row * 42}" width="42" height="42" fill="white" stroke="#374151"/>')
        return "".join(parts) + "</svg>"
    raise ValueError(f"tipe stimulus tidak didukung: {kind}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("spec")
    parser.add_argument("output")
    args = parser.parse_args()
    spec = json.loads(Path(args.spec).read_text(encoding="utf-8"))
    Path(args.output).write_text(render_svg(spec), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

