---
name: verifikasi-bank-soal
description: Memeriksa struktur, fungsi, substansi, visual, ketertelusuran, kualitas, dan kelengkapan bukti Bank Soal SD pada tingkat butir, kelompok, indikator, dan finalisasi.
---

# Skill Verifikasi Bank Soal SD

## Tujuan

Gunakan skill ini untuk memeriksa hasil aktual Bank Soal SD dan menahan kelulusan jika bukti wajib belum lengkap. Skill ini tidak menggantikan verifikasi pedagogis ChatGPT atau persetujuan Romo.

## Prasyarat

1. Pastikan repositori, branch, working tree, dokumen induk aktif, AGENTS.md, dan rancangan indikator dapat ditelusuri.
2. Pastikan lingkup tugas hanya mencakup satu indikator dan satu tahap.
3. Pastikan berkas JSON, HTML, gambar, laporan, dan versi acuan tersedia.
4. Jika prasyarat atau keputusan pendidikan belum jelas, hentikan bagian terdampak dan laporkan sumber serta lokasi masalah.

## Tingkat pemeriksaan

Gunakan empat tingkat pemeriksaan:

1. **Struktural:** ID, relasi indikator, 14 atribut, aturan bersyarat, jumlah, nomor, JSON, dan berkas.
2. **Fungsional:** HTML dua mode, respons, penilaian, rubrik, percabangan, ketuntasan, dan laporan melalui pengujian aktual.
3. **Substansi dan visual:** keselarasan CP–ATP–TP–KM–indikator, bukti, kategori, batas, kompleksitas, stimulus, gambar, metode, dan variasi.
4. **Persetujuan akhir:** kelengkapan bukti, register, keputusan Romo, versi, commit, dan pull request.

## Pemeriksaan kualitas soal

Periksa 18 kriteria Bab 19.3 pada tingkat butir, kelompok 10 soal, dan keseluruhan 40 soal. Pastikan:

- keempat jenis soal mengukur kompetensi dan kategori yang sama;
- Penguatan dan Pengayaan memiliki penjelasan konsep serta penerapan nyata;
- Cek Ulang lebih kompleks daripada Diagnostik tanpa mengubah kompetensi;
- metode, pilihan/kunci atau rubrik benar-benar menghasilkan bukti;
- panduan orang tua dapat dilaksanakan tanpa perlengkapan tambahan;
- stimulus dan gambar konsisten dengan pertanyaan, jawaban, serta rubrik;
- status parsial tidak disamakan dengan Final.

## Antiduplikasi

Terapkan Bab 19.8 pada enam titik wajib:

1. Sebelum produksi.
2. Per butir.
3. Setelah kelompok 10 soal.
4. Setelah revisi.
5. Saat verifikasi 40 soal.
6. Sebelum finalisasi.

Gunakan koleksi pembanding global yang mencakup soal aktif pada `main`, cabang relevan, dan draf lokal yang diketahui. Bedakan benturan ID, duplikasi terbukti, kandidat kemiripan, dan variasi sah. Jangan memutuskan duplikasi hanya berdasarkan skor otomatis atau kemiripan struktur.

Sepuluh kriteria kelulusan antiduplikasi harus terpenuhi bersamaan. Jika koleksi, kandidat, bukti, versi, atau tindakan korektif belum lengkap, tahan kelulusan.

## Status pemeriksaan

Gunakan hanya:

- **Lulus:** benar-benar diperiksa dan berhasil.
- **Gagal:** ditemukan kekurangan.
- **Belum diuji:** belum diperiksa.
- **Tidak berlaku:** tidak relevan, dengan alasan.

Jangan menyebut rencana, keberadaan kode, atau deskripsi sebagai bukti Lulus.

## Bukti dan tindakan korektif

Catat minimal identitas kedua entitas pembanding jika relevan, versi konten, metode, kategori temuan, unsur sama, unsur berbeda, variasi, kesimpulan, dan alasan pedagogis. Simpan bukti terpisah dari 14 atribut soal.

Jika terjadi revisi yang memengaruhi soal, gambar, metode, rubrik, versi, atau koleksi pembanding, ulangi pemeriksaan yang terdampak. Jangan mengubah identitas kompetensi, kategori, batas, atau standar penilaian secara sepihak.

## Titik berhenti

Hentikan dan laporkan jika indikator ambigu, bukti tidak cukup, perangkat belum terverifikasi, HTML belum diuji, gambar belum diperiksa aktual, koleksi pembanding tidak lengkap, atau persetujuan tahap sebelumnya belum tersedia.
