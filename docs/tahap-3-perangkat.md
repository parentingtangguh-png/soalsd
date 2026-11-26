# Tahap Migrasi 3 — Perangkat Produksi

Status awal: **Draf / dalam verifikasi teknis**.

Dokumen ini mencatat perangkat yang dibuat pada Tahap 3. Ia tidak menetapkan keputusan pendidikan baru dan tidak mengubah 14 atribut soal.

| No. | Perangkat | Berkas | Fungsi yang tersedia | Status awal |
|---:|---|---|---|---|
| 1 | Ekstraktor kompetensi | `scripts/competency_extractor.py` | Membaca tabel Markdown atau manifest JSON dan mempertahankan field yang tertulis eksplisit. | Draf |
| 2 | Generator identitas | `scripts/question_id_generator.py` | Membuat ID soal sesuai format Bab 19.1 dan membatasi jenis/nomor soal. | Draf |
| 3 | Validator JSON | `scripts/json_validator.py` | Memeriksa tepat 14 atribut dan aturan bersyarat; dapat memeriksa parsial atau lengkap. | Draf |
| 4 | Perangkat pembuatan gambar | `scripts/image_generator.py` | Menghasilkan SVG deterministik untuk stimulus programatis yang didukung. | Draf |
| 5 | Generator HTML | `scripts/html_generator.py` | Menghasilkan HTML offline dengan Mode Pemeriksaan dan Mode Pengerjaan. | Draf |
| 6 | Perangkat pengujian | `scripts/test_runner.py` | Menjalankan suite uji teknis lokal. | Draf |
| 7 | Pengelola register | `scripts/register_manager.py` | Membaca berkas JSON aktual dan menghasilkan register mesin terpisah. | Draf |
| 8 | Detektor antiduplikasi | `scripts/antidupe_detector.py` | Membuat indeks ID/hash, duplikasi identik, dan kandidat kemiripan untuk verifikasi pedagogis. | Draf |

## Batas implementasi

- Data uji bersifat sintetis dan tidak dihitung sebagai soal final.
- Detektor tidak memutuskan kelulusan pedagogis secara otomatis.
- Generator HTML tidak menjadi sumber soal terpisah.
- Tidak ada database, akun, penyimpanan permanen hasil belajar, atau kredensial.
- Pemeriksaan browser, visual aktual, integrasi end-to-end, dan dua belas kelompok uji antiduplikasi masih menunggu Tahap 4.

## Pemeriksaan awal

Suite `tests/test_devices.py` memeriksa fungsi dasar ketujuh modul perangkat dan menggunakan fixture sintetis. Hasil pemeriksaan dicatat sebagai bukti Tahap 3; hasil ini belum menggantikan verifikasi lingkungan Tahap 4.

