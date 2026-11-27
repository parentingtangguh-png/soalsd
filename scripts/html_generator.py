"""Generate an offline HTML viewer and runner from one JSON source."""

from __future__ import annotations

import argparse
import base64
import json
from pathlib import Path
from typing import Any


def _data_uri(path: Path) -> str:
    mime = "image/svg+xml" if path.suffix.casefold() == ".svg" else "image/png"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def generate_html(data: dict[str, Any], image_dir: str | Path | None = None) -> str:
    images: dict[str, str] = {}
    if image_dir:
        root = Path(image_dir)
        for item in data.get("soal", []):
            if item.get("butuh_gambar"):
                for suffix in (".svg", ".png"):
                    candidate = root / f"{item['id_soal']}{suffix}"
                    if candidate.exists():
                        images[item["id_soal"]] = _data_uri(candidate)
                        break
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    image_payload = json.dumps(images, ensure_ascii=False)
    return f'''<!doctype html>
<html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Bank Soal SD — {data.get("id_indikator", "tanpa indikator")}</title>
<style>body{{font-family:system-ui,sans-serif;max-width:960px;margin:auto;padding:1rem;color:#172033}}button,select{{padding:.55rem;margin:.2rem}}.card{{border:1px solid #cbd5e1;border-radius:10px;padding:1rem;margin:.8rem 0}}.muted{{color:#64748b}}.hidden{{display:none}}.choice{{display:block;padding:.4rem}}figure.stimulus{{margin:1rem 0;padding:.75rem;border:2px solid #94a3b8;border-radius:8px;background:#f8fafc}}figure.stimulus figcaption{{font-weight:700;margin-bottom:.5rem}}figure.stimulus img{{display:block;max-width:100%;height:auto}}</style></head>
<body><header><h1>Bank Soal SD</h1><p id="indicator" class="muted"></p><button id="inspectBtn">Mode Pemeriksaan</button><button id="workBtn">Mode Pengerjaan</button></header>
<main id="app"></main>
<script>const DATA={payload}; const IMAGES={image_payload};
const app=document.getElementById('app'); const indicator=document.getElementById('indicator'); let mode='inspect'; let kind='DIA'; let index=0; const answers={{}};
 const labels={{DIA:'Diagnostik',PGT:'Penguatan',PYN:'Pengayaan',CU:'Cek Ulang'}};
 function hierarchy(){{const h=DATA.hierarki||{{}}; return '<section class="card"><h2>Hierarki CP–ATP–TP–KM–Indikator</h2>'+['CP','ATP','TP','KM','Indikator'].map(k=>'<p><b>'+k+':</b> '+esc(h[k]||DATA.id_indikator||'Belum tersedia')+'</p>').join('')+'</section>';}}
function esc(v){{return String(v??'').replace(/[&<>"']/g,m=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[m]));}}
function currentQuestions(){{return (DATA.soal||[]).filter(q=>q.jenis_soal===kind);}}
 function renderInspect(){{indicator.textContent='Indikator: '+(DATA.id_indikator||''); app.innerHTML='<h2>Mode Pemeriksaan</h2>'+hierarchy()+((DATA.soal||[]).map(q=>'<section class="card"><h3>'+esc(q.id_soal)+' — '+esc(labels[q.jenis_soal])+'</h3><dl>'+Object.entries(q).map(([k,v])=>'<dt><b>'+esc(k)+'</b></dt><dd>'+esc(typeof v==='object'?JSON.stringify(v):v)+'</dd>').join('')+'</dl>'+(IMAGES[q.id_soal]?'<figure class="stimulus"><figcaption>Stimulus</figcaption><img alt="Stimulus soal" src="'+IMAGES[q.id_soal]+'"></figure>':'')+'</section>').join('')||'<p>Belum ada soal.</p>');}}
function renderWork(){{const qs=currentQuestions(); const q=qs[index]; indicator.textContent='Indikator: '+(DATA.id_indikator||''); if(!q){{app.innerHTML='<p>Kelompok '+esc(kind)+' belum tersedia.</p>';return;}} let input=''; if(q.metode_penilaian==='OTOMATIS') input=Object.entries(q.pilihan||{{}}).map(([k,v])=>'<label class="choice"><input type="radio" name="answer" value="'+k+'" '+(answers[q.id_soal]===k?'checked':'')+'> '+k+'. '+esc(v)+'</label>').join(''); else input=Array.isArray(q.rubrik_penilaian)?q.rubrik_penilaian.map((v,i)=>'<label class="choice"><input type="checkbox" data-rubrik="'+i+'" '+((answers[q.id_soal]||[]).includes(i)?'checked':'')+'> '+esc(typeof v==='object'?v.kriteria:v)+'</label>').join(''):'<p>Rubrik belum tersedia.</p>'; app.innerHTML='<label>Jenis: <select id="kind">'+Object.entries(labels).map(([k,v])=>'<option value="'+k+'" '+(k===kind?'selected':'')+'>'+v+'</option>').join('')+'</select></label><section class="card"><h2>'+esc(q.id_soal)+'</h2><p>'+esc(q.pertanyaan)+'</p>'+(IMAGES[q.id_soal]?'<figure class="stimulus"><figcaption>Stimulus</figcaption><img alt="Stimulus soal" src="'+IMAGES[q.id_soal]+'"></figure>':'')+'<div>'+input+'</div><p class="muted">Soal '+(index+1)+' dari '+qs.length+'</p><button id="save">Simpan respons</button><button id="next">Berikutnya</button><button id="report">Nilai kelompok</button><div id="result"></div></section>'; document.getElementById('kind').onchange=e=>{{kind=e.target.value;index=0;renderWork();}}; document.getElementById('save').onclick=()=>save(q); document.getElementById('next').onclick=()=>{{save(q);index=Math.min(index+1,qs.length-1);renderWork();}}; document.getElementById('report').onclick=()=>report(qs);}}
function save(q){{if(q.metode_penilaian==='OTOMATIS'){{const el=document.querySelector('input[name=answer]:checked'); if(el)answers[q.id_soal]=el.value;}}else answers[q.id_soal]=[...document.querySelectorAll('input[data-rubrik]:checked')].map(x=>Number(x.dataset.rubrik));}}
function score(q){{const a=answers[q.id_soal]; if(a===undefined)return null; if(q.metode_penilaian==='OTOMATIS')return a===q.kunci_jawaban?100:0; return Math.round((a.length/(q.rubrik_penilaian||[]).length)*10000)/100;}}
function report(qs){{const scores=qs.map(score); const complete=scores.every(v=>v!==null); const avg=complete?scores.reduce((a,b)=>a+b,0)/scores.length:null; let next=''; if(kind==='DIA'&&avg!==null)next=avg===100?'PYN':'PGT'; else if((kind==='PGT'||kind==='PYN')&&complete)next='CU'; const status=kind==='CU'&&avg!==null?(avg===100?'Tuntas':'Belum Tuntas'):''; document.getElementById('result').innerHTML='<div class="card"><b>Laporan</b><p>Terjawab: '+scores.filter(v=>v!==null).length+'/'+scores.length+'</p><p>Nilai: '+(avg===null?'belum lengkap':avg.toFixed(2)+'%')+'</p><p>'+esc(status|| (next?'Kelompok berikutnya: '+labels[next]:'Lengkapi seluruh soal untuk laporan'))+'</p></div>';}}
document.getElementById('inspectBtn').onclick=()=>{{mode='inspect';renderInspect();}}; document.getElementById('workBtn').onclick=()=>{{mode='work';renderWork();}}; renderInspect();</script></body></html>'''


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("--image-dir")
    args = parser.parse_args()
    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    Path(args.output).write_text(generate_html(data, args.image_dir), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

