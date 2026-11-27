# Struktur Direktori Bank Soal SD

Struktur ini mengikuti Bab 20.2 dan memisahkan konten soal, perangkat, bukti pemeriksaan, register, dan dokumen keputusan.

```text
soalsd/
├── AGENTS.md
├── .agents/skills/
├── .github/
├── ringkasan_bank_soal_sd_v5-salinan 62.md (calon acuan aktif setelah penetapan)
├── ringkasan_bank_soal_sd_v5-salinan 61.md (dipertahankan; arsip setelah penetapan 62)
├── docs/
│   ├── register_bank_soal.md
│   ├── catatan_persetujuan.md
│   ├── struktur_direktori.md
│   └── antiduplikasi/
├── schemas/
├── templates/
├── scripts/
├── tests/
└── bank_soal/
    └── MTK/
        └── A/
            ├── K1/
            └── K2/
```

## Batas penyimpanan

- JSON soal adalah sumber data tunggal konten soal.
- HTML dihasilkan dari JSON dan gambar terkait.
- Bukti antiduplikasi, register, persetujuan, versi, dan status disimpan terpisah dari 14 atribut soal.
- Tidak ada penyimpanan permanen hasil belajar anak pada tahap ini.
- Data uji teknis tidak masuk koleksi soal aktif dan tidak dihitung sebagai soal final.
