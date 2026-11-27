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
| 4 | Verifikasi lingkungan produksi | Final | PR #12; merge `1560fbdf17df82d942c1bf974a4e8d890427e639`; `docs/verifikasi_tahap4.md` | Final untuk lingkungan teknis sintetis; pemeriksaan pedagogis/substansi berlaku pada indikator produksi |
| 5 | Analisis 10 indikator | Disetujui, menunggu finalisasi | PR #14; `docs/pengajuan_MIG-G4-PERSIAPAN-10-INDIKATOR.md` | Setelah finalisasi, mulai 10 penugasan analisis terpisah |

## Register indikator dan soal

Belum ada soal produksi. Draf, data uji, dan ilustrasi tidak dihitung sebagai soal final.

| ID indikator | Tahap aktif | JSON | HTML | Gambar | Status soal | Status verifikasi | Persetujuan |
|---|---|---|---|---|---|---|---|
| `IND-MTK-A-K1-B.1-KM01-I01` | Menunggu persetujuan | Belum ada | Belum ada | Belum ada | Belum dimulai | Belum diuji | Disetujui melalui PR #14 |
| `IND-MTK-A-K1-B.1-KM02-I01` | Menunggu persetujuan | Belum ada | Belum ada | Belum ada | Belum dimulai | Belum diuji | PR pengajuan 10 indikator |
| `IND-MTK-A-K1-B.1-KM03-I01` | Menunggu persetujuan | Belum ada | Belum ada | Belum ada | Belum dimulai | Belum diuji | PR pengajuan 10 indikator |
| `IND-MTK-A-K1-B.3-KM01-I01` | Menunggu persetujuan | Belum ada | Belum ada | Belum ada | Belum dimulai | Belum diuji | PR pengajuan 10 indikator |
| `IND-MTK-A-K1-B.3-KM02-I01` | Menunggu persetujuan | Belum ada | Belum ada | Belum ada | Belum dimulai | Belum diuji | PR pengajuan 10 indikator |
| `IND-MTK-A-K1-B.3-KM03-I01` | Menunggu persetujuan | Belum ada | Belum ada | Belum ada | Belum dimulai | Belum diuji | PR pengajuan 10 indikator |
| `IND-MTK-A-K1-B.3-KM04-I01` | Menunggu persetujuan | Belum ada | Belum ada | Belum ada | Belum dimulai | Belum diuji | PR pengajuan 10 indikator |
| `IND-MTK-A-K1-B.2-KM01-I01` | Menunggu persetujuan | Belum ada | Belum ada | Belum ada | Belum dimulai | Belum diuji | PR pengajuan 10 indikator |
| `IND-MTK-A-K1-B.2-KM02-I01` | Menunggu persetujuan | Belum ada | Belum ada | Belum ada | Belum dimulai | Belum diuji | PR pengajuan 10 indikator |
| `IND-MTK-A-K1-B.2-KM03-I01` | Menunggu persetujuan | Belum ada | Belum ada | Belum ada | Belum dimulai | Belum diuji | PR pengajuan 10 indikator |

## Aturan pencatatan

- Catat versi konten, gambar, metode, koleksi pembanding, commit, dan pull request jika tersedia.
- Simpan bukti antiduplikasi terpisah dari 14 atribut soal.
- Jika isi atau fungsi berubah setelah pemeriksaan, ulangi pemeriksaan yang terdampak.
- Jangan menghitung satu entitas yang sama berulang karena tersedia di beberapa cabang atau format.
- Jangan menandai persetujuan tanpa bukti keputusan Romo.
