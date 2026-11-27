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
| 5 | Gerbang 4 dan analisis 10 indikator | Final | PR #14 merge `e27168a91b52c778a65715ac41ce8adb760dbdf9`; PR #15–#24 telah merge | Analisis 10 indikator Final; lanjutkan pengajuan produksi per indikator; produksi soal belum dimulai |

## Register indikator dan soal

Belum ada soal produksi. Draf, data uji, dan ilustrasi tidak dihitung sebagai soal final.

| ID indikator | Tahap aktif | JSON | HTML | Gambar | Status soal | Status verifikasi | Persetujuan |
|---|---|---|---|---|---|---|---|
| `IND-MTK-A-K1-B.1-KM01-I01` | Tahap 1 — analisis (Final) | Belum ada | Belum ada | Belum ada | Belum dimulai | Final | PR #15 merged |
| `IND-MTK-A-K1-B.1-KM02-I01` | Tahap 1 — analisis (Final) | Belum ada | Belum ada | Belum ada | Belum dimulai | Final | PR #16 merged |
| `IND-MTK-A-K1-B.1-KM03-I01` | Tahap 1 — analisis (Final) | Belum ada | Belum ada | Belum ada | Belum dimulai | Final | PR #17 merged |
| `IND-MTK-A-K1-B.3-KM01-I01` | Tahap 1 — analisis (Final) | Belum ada | Belum ada | Belum ada | Belum dimulai | Final | PR #18 merged |
| `IND-MTK-A-K1-B.3-KM02-I01` | Tahap 1 — analisis (Final) | Belum ada | Belum ada | Belum ada | Belum dimulai | Final | PR #19 merged |
| `IND-MTK-A-K1-B.3-KM03-I01` | Tahap 1 — analisis (Final) | Belum ada | Belum ada | Belum ada | Belum dimulai | Final | PR #20 merged |
| `IND-MTK-A-K1-B.3-KM04-I01` | Tahap 1 — analisis (Final) | Belum ada | Belum ada | Belum ada | Belum dimulai | Final | PR #21 merged |
| `IND-MTK-A-K1-B.2-KM01-I01` | Tahap 1 — analisis (Final) | Belum ada | Belum ada | Belum ada | Belum dimulai | Final | PR #22 merged |
| `IND-MTK-A-K1-B.2-KM02-I01` | Tahap 1 — analisis (Final) | Belum ada | Belum ada | Belum ada | Belum dimulai | Final | PR #23 merged |
| `IND-MTK-A-K1-B.2-KM03-I01` | Tahap 1 — analisis (Final) | Belum ada | Belum ada | Belum ada | Belum dimulai | Final | PR #24 merged |

## Aturan pencatatan

- Catat versi konten, gambar, metode, koleksi pembanding, commit, dan pull request jika tersedia.
- Simpan bukti antiduplikasi terpisah dari 14 atribut soal.
- Jika isi atau fungsi berubah setelah pemeriksaan, ulangi pemeriksaan yang terdampak.
- Jangan menghitung satu entitas yang sama berulang karena tersedia di beberapa cabang atau format.
- Jangan menandai persetujuan tanpa bukti keputusan Romo.
