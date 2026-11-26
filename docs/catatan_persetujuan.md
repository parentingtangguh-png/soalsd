# Catatan Persetujuan Bank Soal SD

Catatan ini menyimpan keputusan, lingkup persetujuan, versi berkas, identitas commit, dan tindakan berikutnya. Catatan ini terpisah dari atribut soal.

## Format catatan

Setiap persetujuan produksi harus mencantumkan:

- ID indikator.
- Tahap pekerjaan.
- Lingkup persetujuan.
- Versi berkas.
- Identitas commit yang diperiksa.
- Keputusan Romo.
- Tindakan berikutnya.

## Keputusan yang telah diterima

| Tanggal | Lingkup | Keputusan | Status bukti formal |
|---|---|---|---|
| 27 November 2026 | Komponen 1 / cakupan CP | Kesenjangan tetap dicatat sebagai isu Komponen 1 dan tidak ditutup sepihak. | Keputusan percakapan; perlu dikaitkan dengan commit/register pada pengajuan resmi |
| 27 November 2026 | `MIG-T2-PERSIAPAN` / Tahap Migrasi 2 | Tahap 2 disetujui dan difinalkan dalam lingkup PR #7: AGENTS.md, dokumen induk V5, lima skill, struktur direktori, register, dan catatan persetujuan. | Disetujui Romo berdasarkan PR #7 dan commit yang diperiksa `1811052`; tercatat pada `1c28b3e` dan masuk `main` melalui merge commit `14e156a` |
| 27 November 2026 | `MIG-T3-PERANGKAT` / Tahap Migrasi 3 | Delapan perangkat produksi, fixture sintetis, suite teknis, dan uji CLI. | Disetujui Romo berdasarkan PR #9 dan commit yang diperiksa `81acc59`; masuk `main` melalui merge commit `5d01801` |

## Status persetujuan dan pekerjaan berikutnya

| ID tugas / indikator | Tahap | Lingkup | Status | Tindakan berikutnya |
|---|---|---|---|---|
| `MIG-T2-PERSIAPAN` | Tahap Migrasi 2 | AGENTS.md, lima skill, struktur, register, dan mekanisme persetujuan | Final | PR #7 telah masuk `main` melalui merge commit `14e156a`; Tahap 3 dapat disiapkan |
| `MIG-T3-PERANGKAT` | Tahap Migrasi 3 | Delapan perangkat produksi | Final | PR #9 masuk `main` melalui merge `5d01801`; siapkan Tahap 4 |
| `MIG-T4-VERIFIKASI` | Tahap Migrasi 4 | Verifikasi lingkungan produksi | Dalam verifikasi | Bukti sintetis dan browser desktop tersedia; uji lintas ukuran layar serta pemeriksaan pedagogis masih terbuka |
| `IND-MTK-A-K1-B.1-KM01-I01` | Tahap 1 penyusunan | Analisis dan rancangan empat jenis soal | Belum dimulai | Menunggu Tahap 4 dan persiapan produksi |
