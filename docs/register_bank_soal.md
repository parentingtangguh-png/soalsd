# Register Bank Soal SD

Register ini mencatat kondisi aktual berkas, status pemeriksaan, bukti, persetujuan, dan progres. Register tidak mengubah substansi CP, ATP, TP, KM, indikator, atau 14 atribut soal.

## Status pengembangan

Gunakan hanya status berikut:

1. Belum dimulai
2. Draf
3. Dalam verifikasi
4. Menunggu persetujuan
5. Disetujui, menunggu finalisasi
6. Final

Status **Final** hanya digunakan setelah hasil disetujui, disimpan, diverifikasi, dan masuk `main`.

## Status migrasi

| Tahap | Lingkup | Status | Bukti | Kendala / tindakan berikutnya |
|---:|---|---|---|---|
| 1 | Inisialisasi repositori | Lulus pada checkout kerja | Checkout branch kerja dari `parentingtangguh-png/soalsd`, commit dasar `13dbb56172cc965c37f250cd67856bdf628d716c` | V5 aktif disiapkan pada branch kerja; belum masuk `main` |
| 2 | AGENTS.md, lima skill, struktur, register, persetujuan | Final | Branch `setup/tahap-2-persiapan`, commit diperiksa `1811052`, persetujuan dicatat pada `1c28b3e`, merge commit `14e156a`, PR `#7` | Tahap 3 dapat diajukan/dimulai sesuai persetujuan; belum dimulai |
| 3 | Delapan perangkat produksi | Final | Branch `build/tahap-3-perangkat`, commit diperiksa `81acc59`, persetujuan dicatat pada branch, merge commit `5d01801`, PR `#9`; `tests/test_devices.py` lulus; uji CLI lulus | Tahap 4 dapat disiapkan; belum dimulai |
| 4 | Verifikasi lingkungan produksi | Menunggu persetujuan | Branch `verify/tahap-4-lingkungan`; `docs/pengajuan_MIG-T4-VERIFIKASI.md`; PR #12; report sintetis dan bukti browser desktop | Uji tablet/ponsel, pemeriksaan pedagogis, dan substansi sintetis masih terbuka |
| 5 | Analisis indikator pertama | Belum dimulai | Belum tersedia | Menunggu Tahap 4 lulus dan persiapan produksi disetujui |

## Register indikator dan soal

Belum ada soal produksi. Draf, data uji, dan ilustrasi tidak dihitung sebagai soal final.

| ID indikator | Tahap aktif | JSON | HTML | Gambar | Status soal | Status verifikasi | Persetujuan |
|---|---|---|---|---|---|---|---|
| `IND-MTK-A-K1-B.1-KM01-I01` | Belum dimulai | Belum ada | Belum ada | Belum ada | Belum dimulai | Belum diuji | Belum ada |

## Aturan pencatatan

- Catat versi konten, gambar, metode, koleksi pembanding, commit, dan pull request jika tersedia.
- Simpan bukti antiduplikasi terpisah dari 14 atribut soal.
- Jika isi atau fungsi berubah setelah pemeriksaan, ulangi pemeriksaan yang terdampak.
- Jangan menghitung satu entitas yang sama berulang karena tersedia di beberapa cabang atau format.
- Jangan menandai persetujuan tanpa bukti keputusan Romo.
