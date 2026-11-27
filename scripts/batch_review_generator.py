"""Generate one offline audit page containing every question in a batch."""

from __future__ import annotations

import argparse
import base64
import html
import json
from pathlib import Path


def esc(value) -> str:
    return html.escape("" if value is None else str(value), quote=True)


def json_text(value) -> str:
    if value is None:
        return "null"
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False)
    return str(value)


def image_uri(path: Path) -> str:
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/svg+xml;base64,{data}"


def render_card(question: dict, image: str | None) -> str:
    fields = "".join(
        f"<dt>{esc(key)}</dt><dd>{esc(json_text(question.get(key)))}</dd>"
        for key in question
    )
    stimulus = ""
    if image:
        stimulus = f'<figure class="stimulus"><figcaption>Stimulus aktual</figcaption><img alt="Stimulus soal" src="{image}"></figure>'
    return (
        f'<article class="card" data-kind="{esc(question["jenis_soal"])}" '
        f'data-indicator="{esc(question["id_indikator"])}">'
        f'<h3>{esc(question["id_soal"])} — {esc(question["jenis_soal"])}</h3>'
        f'<p class="question">{esc(question["pertanyaan"])}</p>{stimulus}'
        f'<details><summary>14 atribut dan audit identitas</summary>'
        f'<dl><dt>kategori_kecakapan_berpikir</dt><dd class="derived">Ditampilkan dari hierarki indikator pada bagian kelompok.</dd>{fields}</dl>'
        f'</details></article>'
    )


def generate(root: Path) -> str:
    files = sorted(root.glob("MTK-A-K1-*.json"))
    groups = []
    total = 0
    image_root = root / "images"
    for path in files:
        data = json.loads(path.read_text(encoding="utf-8"))
        questions = data.get("soal", [])
        total += len(questions)
        cards = []
        for question in questions:
            image = None
            if question.get("butuh_gambar"):
                candidate = image_root / f'{question["id_soal"]}.svg'
                if candidate.exists():
                    image = image_uri(candidate)
            cards.append(render_card(question, image))
        hierarchy = data.get("hierarki", {})
        hierarchy_html = "".join(
            f"<p><b>{esc(key)}:</b> {esc(value)}</p>"
            for key, value in hierarchy.items()
        )
        groups.append(
            f'<section class="indicator" data-indicator="{esc(data["id_indikator"])}">'
            f'<h2>{esc(data["id_indikator"])}</h2><div class="hierarchy">{hierarchy_html}</div>'
            + "".join(cards)
            + "</section>"
        )
    return f'''<!doctype html>
<html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Pengajuan MTK Fase A — 10 indikator — 400 soal</title>
<style>
body{{font-family:system-ui,sans-serif;max-width:1180px;margin:auto;padding:1rem;color:#172033;background:#f8fafc}}
header,.indicator,.card{{background:white;border:1px solid #cbd5e1;border-radius:10px;padding:1rem;margin:.8rem 0}}
header{{position:sticky;top:0;z-index:2;box-shadow:0 2px 10px #0001}}h1{{margin:.1rem 0}}h2{{color:#0f3d68}}h3{{font-size:1rem;overflow-wrap:anywhere}}.muted{{color:#64748b}}
select,button{{padding:.55rem;margin:.2rem}}.question{{font-size:1.05rem}}.hierarchy{{background:#eff6ff;border-left:4px solid #2563eb;padding:.6rem;overflow-wrap:anywhere}}
details{{margin-top:.7rem}}dt{{margin-top:.35rem;font-weight:700}}dd{{margin-left:1rem;white-space:pre-wrap;overflow-wrap:anywhere}}.derived{{color:#7c3aed}}
figure.stimulus{{padding:.75rem;border:2px solid #94a3b8;border-radius:8px;background:#f8fafc}}figure.stimulus img{{display:block;max-width:100%;height:auto}}
.hidden{{display:none}}.count{{font-weight:700;color:#166534}}
</style></head><body>
<header><h1>Pengajuan Produksi MTK Fase A</h1><p>Batch audit: 10 indikator × 40 soal = <span class="count">{total} soal</span>.</p>
<p class="muted">Halaman ini adalah tampilan audit gabungan. JSON per indikator tetap menjadi sumber data soal.</p>
<label>Indikator: <select id="indicatorFilter"><option value="ALL">Semua indikator</option>{''.join(f'<option value="{esc(p.stem.replace("MTK-A-K1-", "IND-MTK-A-K1-"))}">{esc(p.stem)}</option>' for p in files)}</select></label>
<label>Jenis: <select id="kindFilter"><option value="ALL">Semua jenis</option><option value="DIA">Diagnostik</option><option value="PGT">Penguatan</option><option value="PYN">Pengayaan</option><option value="CU">Cek Ulang</option></select></label>
<button id="expand">Buka semua atribut</button><button id="collapse">Tutup semua atribut</button><span id="shown" class="muted"></span></header>
<main>{''.join(groups)}</main>
<script>
const indicator=document.getElementById('indicatorFilter'), kind=document.getElementById('kindFilter'), shown=document.getElementById('shown');
function filter(){{let n=0;const iv=indicator.value,kv=kind.value;document.querySelectorAll('.indicator').forEach(s=>{{const si=s.dataset.indicator;let visible=false;s.querySelectorAll('.card').forEach(c=>{{const ok=(iv==='ALL'||si===iv)&&(kv==='ALL'||c.dataset.kind===kv);c.classList.toggle('hidden',!ok);if(ok){{n++;visible=true;}}}});s.classList.toggle('hidden',!visible);}});shown.textContent=' Ditampilkan: '+n+' soal';}}
function setDetails(open){{document.querySelectorAll('details').forEach(d=>d.open=open);}}
indicator.onchange=filter;kind.onchange=filter;document.getElementById('expand').onclick=()=>setDetails(true);document.getElementById('collapse').onclick=()=>setDetails(false);filter();
</script></body></html>'''


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root")
    parser.add_argument("output")
    args = parser.parse_args()
    root = Path(args.root)
    Path(args.output).write_text(generate(root), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
