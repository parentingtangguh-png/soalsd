# Bukti Antiduplikasi

Direktori ini menyimpan bukti pemeriksaan antiduplikasi secara terpisah dari JSON konten soal.

Struktur per indikator yang akan digunakan setelah perangkat tersedia:

```text
docs/antiduplikasi/
├── konfigurasi.json
└── MTK/A/K1/<ID-indikator>/
    ├── sidik_soal.jsonl
    ├── temuan.jsonl
    ├── hasil_verifikasi.json
    └── laporan_verifikasi.md
```

Bukti harus terikat pada versi konten, gambar, metode pemeriksaan, dan koleksi pembanding yang aktual. Algoritma, ambang teknis, dan indeks belum ditetapkan pada tahap ini.
