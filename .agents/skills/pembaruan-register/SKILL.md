---
name: pembaruan-register
description: Mencatat status aktual, versi, lokasi berkas, pemeriksaan, bukti antiduplikasi, persetujuan, dan progres Bank Soal SD tanpa mengubah substansi pendidikan atau menghitung draf sebagai final.
---

# Skill Pembaruan Register Bank Soal SD

## Tujuan

Gunakan skill ini untuk menjaga register sebagai catatan kondisi aktual Bank Soal SD. Register bukan sumber keputusan pendidikan dan tidak boleh mengubah isi soal atau indikator.

## Prasyarat

1. Baca AGENTS.md dan dokumen induk aktif.
2. Periksa branch, working tree, commit, dan lingkup penugasan.
3. Gunakan bukti berkas dan hasil pemeriksaan aktual.
4. Jika informasi belum diperiksa, catat sebagai Belum diuji, bukan Lulus.

## Informasi yang dicatat

Register harus dapat menelusuri:

- ID indikator dan hierarki CP–ATP–TP–KM–indikator;
- jenis dan ID soal;
- lokasi JSON, HTML, dan gambar;
- versi konten dan gambar;
- status pengembangan;
- status pemeriksaan struktural, fungsional, substansi, visual, dan antiduplikasi;
- bukti dan laporan pemeriksaan;
- koleksi pembanding yang digunakan;
- versi metode atau perangkat pemeriksaan;
- persetujuan, commit, pull request, dan keputusan berikutnya;
- kendala serta titik berhenti.

## Status pengembangan

Gunakan enam status berikut secara tepat:

1. Belum dimulai.
2. Draf.
3. Dalam verifikasi.
4. Menunggu persetujuan.
5. Disetujui, menunggu finalisasi.
6. Final.

Status **Final** hanya boleh digunakan setelah hasil disetujui, disimpan, diverifikasi, dan masuk cabang utama. Rumusan indikator yang Final tidak berarti 40 soal dan verifikasinya sudah Final.

## Aturan pencatatan

- Catat satu perubahan sebagai satu riwayat yang dapat ditelusuri.
- Jangan menghapus catatan historis yang diperlukan untuk memahami perubahan.
- Jangan menghitung draf, usulan, data uji, atau pekerjaan yang belum difinalisasi sebagai soal final.
- Jangan menambahkan status, versi, persetujuan, atau antiduplikasi ke dalam 14 atribut soal.
- Jangan membuat keputusan pendidikan baru melalui register.
- Jangan menandai persetujuan tanpa bukti keputusan Romo.
- Jika isi atau fungsi berubah setelah pemeriksaan, tandai pemeriksaan terdampak untuk diulang.

## Format catatan pembaruan

Setiap pembaruan minimal mencantumkan:

- tanggal;
- ID tugas;
- indikator dan tahap;
- lingkup perubahan;
- berkas yang berubah;
- status sebelum dan sesudah;
- bukti pemeriksaan;
- versi atau commit;
- keputusan Romo jika diperlukan;
- kendala;
- tindakan berikutnya.

## Antiduplikasi

Catat bukti antiduplikasi secara terpisah dari konten soal. Hubungkan bukti dengan versi soal, gambar, metode pemeriksaan, dan koleksi pembanding. Catat enam titik pemeriksaan dan sepuluh kriteria kelulusan; jangan menganggap kelulusan antiduplikasi sebagai Final tanpa pemeriksaan kualitas dan persetujuan Romo.

## Titik berhenti

Hentikan pembaruan jika sumber berkas tidak jelas, versi tidak dapat ditentukan, bukti pemeriksaan tidak tersedia, persetujuan tidak dapat dibuktikan, atau perubahan akan mengubah substansi pendidikan di luar kewenangan teknis.
