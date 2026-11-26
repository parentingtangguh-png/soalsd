---
name: generator-html
description: Menghasilkan dan memeriksa HTML mandiri Bank Soal SD dari JSON sumber, gambar terkait, dan metadata indikator, dengan Mode Pemeriksaan Bank Soal serta Mode Pengerjaan Soal Interaktif.
---

# Skill Generator HTML Bank Soal SD

## Tujuan

Gunakan skill ini untuk menghasilkan HTML mandiri dari JSON sumber soal dan gambar terkait. HTML adalah hasil produksi, bukan sumber soal terpisah dan bukan tempat mengubah substansi pendidikan.

## Prasyarat

Sebelum bekerja:

1. Periksa repositori, cabang kerja, working tree, dokumen induk aktif, AGENTS.md, dan status perangkat.
2. Pastikan indikator, tahap penyusunan, JSON, gambar, metode, kunci/rubrik, dan versi acuan telah ditetapkan dalam lingkup tugas.
3. Jangan melanjutkan jika JSON belum valid, gambar wajib belum tersedia, atau rancangan belum disetujui.
4. Jangan menetapkan desain penyimpanan permanen hasil belajar anak; Komponen 7 tetap terbuka.

## Sumber data dan batas perubahan

- JSON merupakan sumber data tunggal dengan tepat 14 atribut soal.
- HTML harus menggunakan data, gambar, jawaban, rubrik, dan versi yang sama.
- Metadata indikator boleh digunakan untuk pemeriksaan dan tampilan yang ditetapkan, tetapi tidak menambah atribut soal ke-15.
- Jangan mengubah pertanyaan, pilihan, kunci, panduan, penjelasan, penerapan, metode, rubrik, atau kebutuhan gambar melalui template HTML.
- Status produksi, persetujuan, versi, dan antiduplikasi disimpan di register atau bukti pemeriksaan terpisah.

## Dua mode wajib

### Mode Pemeriksaan Bank Soal

Tampilkan secara terbaca:

- identitas indikator dan hierarki CP–ATP–TP–KM–indikator;
- ID soal dan jenis soal;
- seluruh atribut soal yang relevan;
- pilihan dan kunci sesuai kewenangan pemeriksaan;
- rubrik jika metode ORANG_TUA;
- deskripsi dan spesifikasi gambar;
- hasil atau tautan bukti pemeriksaan jika disediakan oleh data turunan.

Mode ini tidak boleh menyamarkan atribut yang belum lengkap.

### Mode Pengerjaan Soal Interaktif

Ikuti seluruh fungsi wajib Bab 19.5, termasuk:

- menampilkan soal sesuai urutan dan jenis;
- menerima respons anak;
- mendukung pilihan A/B/C atau instrumen ceklis sesuai metode;
- menahan hasil kelompok sampai seluruh 10 soal dijawab atau dikonfirmasi sesuai aturan;
- menghitung nilai proporsional dan informasi pemenuhan utuh;
- menerapkan percabangan Diagnostik 100% ke Pengayaan dan selain itu ke Penguatan;
- menerapkan Cek Ulang 100% = Tuntas dan di bawah 100% = Belum Tuntas;
- menghasilkan laporan konkret untuk kelompok yang selesai;
- tidak mengarahkan ke kelompok yang belum tersedia;
- menyediakan panduan orang tua tanpa meminta perlengkapan tambahan.

Jangan membuat kelompok adaptif baru, ambang baru, pengulangan wajib, atau nilai tambahan.

## Gambar dan offline

- Jika `butuh_gambar` bernilai `true`, tampilkan gambar aktual yang sesuai dengan ID soal dan versi data.
- Jika `butuh_gambar` bernilai `false`, jangan menampilkan placeholder gambar seolah-olah gambar tersedia.
- HTML harus dibuka langsung tanpa internet dan tetap membawa gambar yang diperlukan.
- Periksa tampilan pada komputer, tablet, dan ponsel menggunakan perangkat pengujian yang tersedia.
- Perubahan generator yang memengaruhi HTML lama memerlukan pemeriksaan dampak terhadap seluruh hasil terdampak.

## Verifikasi

Laksanakan pemeriksaan struktural, fungsional, substansi, dan visual yang relevan. Gunakan status Lulus, Gagal, Belum diuji, atau Tidak berlaku secara tepat. Jangan menyatakan fungsi lulus hanya berdasarkan pembacaan kode.

Koordinasikan pemeriksaan dengan skill verifikasi-bank-soal dan pencatatan dengan skill pembaruan-register. Antiduplikasi dilakukan melalui perangkat dan bukti terpisah sesuai Bab 19.8.

## Titik berhenti

Hentikan pekerjaan jika sumber JSON, gambar, metode, rubrik, atau versi tidak konsisten; fungsi wajib belum dapat diuji; HTML mengubah substansi; atau persetujuan tahap sebelumnya belum tersedia.
