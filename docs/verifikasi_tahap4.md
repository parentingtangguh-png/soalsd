# Verifikasi Tahap Migrasi 4 — Lingkungan Produksi

Status: **Final untuk lingkungan verifikasi sintetis**.

Lingkup pemeriksaan ini hanya menggunakan data sintetis. Tidak ada soal produksi, data pribadi anak, atau hasil belajar nyata.

## Hasil aktual

| Tingkat pemeriksaan | Hasil | Bukti / catatan |
|---|---|---|
| Struktural | Lulus | `scripts/stage4_verify.py`: JSON lengkap 40 soal, empat kelompok × 10, tepat 14 atribut, stimulus, register, dan indeks antiduplikasi. |
| Fungsional HTML | Lulus pada browser desktop | Mode Pemeriksaan menampilkan hierarki dan stimulus; Mode Pengerjaan menerima A/B/C dan ceklis orang tua; laporan 10/10; percabangan Diagnostik 0% → Penguatan dan 100% → Pengayaan; Cek Ulang 100% → Tuntas dan 0% → Belum Tuntas. |
| Stimulus/gambar | Lulus teknis dan tampilan desktop | SVG aktual dibuat dan tampil sebagai stimulus pada Mode Pemeriksaan. HTML menyematkan gambar tanpa dependensi eksternal. |
| Antiduplikasi teknis | Lulus teknis | Dua belas kelompok kasus DUP-01–DUP-12 dijalankan; sinyal ID ganda, konten identik, kandidat kemiripan, visual, variasi, revisi, dan koleksi cabang terdeteksi sesuai fixture. |
| Antiduplikasi pedagogis | Belum diuji pada fixture sintetis | Pemeriksaan manusia wajib dilakukan ketika indikator produksi diajukan; status ini tidak mengurangi kewajiban tersebut. |
| Substansi pendidikan | Belum diuji pada fixture sintetis | Fixture tidak mewakili indikator produksi; pemeriksaan substansi dilakukan pada Gerbang 5 dan produksi indikator. |
| Browser tablet/ponsel | Lulus | Uji responsif aktual pada override 390×844 (ponsel) dan 768×1024 (tablet): hierarki, stimulus, pilihan jawaban, dan Mode Pengerjaan tampil; tidak ada horizontal overflow. |
| Console browser | Lulus | Tidak ada error atau warning console pada sesi uji. |

## Perintah pemeriksaan

```text
python scripts/stage4_verify.py <direktori-output>
python scripts/test_runner.py
python -m compileall -q scripts tests
```

Hasil `stage4_verify.py` mencatat seluruh pemeriksaan teknis dan artefak sementara di luar koleksi soal aktif. Artefak sintetis tidak dihitung sebagai soal final.

## Batas dan tindakan berikutnya

- Tahap 4 berstatus Final hanya untuk lingkungan teknis sintetis setelah PR #12 masuk `main`; status ini bukan finalisasi soal produksi.
- Tidak ada produksi soal yang dimulai.
- Tidak ada keputusan baru tentang CP, TP, KM, indikator, kategori, metode, atau penyimpanan hasil belajar.
- Tindakan berikutnya adalah membuka Gerbang 4, yaitu pengajuan persiapan produksi; keterbatasan pemeriksaan pedagogis/empiris tetap terbuka untuk tahap indikator produksi.

