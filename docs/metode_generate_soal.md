# Metode Generate Soal yang Diperbaiki

## Prinsip utama

Konten pendidikan dibuat dan diperiksa terlebih dahulu. JSON, gambar, dan HTML hanya menjadi kemasan setelah konten lulus pemeriksaan user-facing.

Urutan wajib:

**kontrak indikator → draf yang dibaca anak → stimulus aktual → peta bukti → variasi bermakna → panduan orang tua dan rubrik → telaah lawan → kemasan teknis → ceklis lolos → pengajuan**

Tidak boleh membalik urutan ini dengan membuat JSON atau HTML lebih dahulu lalu menganggap soal layak karena validator teknis lulus.

## Tahap 1 — Kontrak indikator

Sebelum menulis soal, buat lembar kontrak untuk satu indikator yang memuat:

- ID indikator dan rumusan verbatim.
- CP, ATP, TP, dan KM yang menjadi jalur ketertelusuran.
- Kategori kecakapan berpikir.
- Kemampuan utama.
- Bukti esensial yang harus diperlihatkan anak.
- Batas kompetensi dan kemampuan yang tidak boleh ditambahkan.
- Jenis soal yang sedang dibuat.
- Bentuk respons dan metode penilaian.
- Kebutuhan stimulus.

Jika salah satu unsur belum jelas, produksi dihentikan.

## Tahap 2 — Draf dari sudut pandang anak

Tulis pertanyaan sebelum menulis JSON.

Draf harus diuji dengan pertanyaan berikut:

- Apakah anak memahami objek yang dirujuk?
- Apakah kata-katanya alami jika dibacakan orang tua?
- Apakah tugasnya dapat dikerjakan tanpa membaca ID, kode, atau metadata?
- Apakah hanya ada tuntutan utama yang sesuai indikator?
- Apakah pertanyaan meminta bukti yang benar-benar diperlukan?
- Apakah anak tahu apa yang harus dilakukan dan apa yang harus disampaikan?

Dilarang menggunakan rujukan seperti “soal nomor 1”, “susunan DIA”, “objek tersebut” tanpa referen yang terlihat. ID hanya untuk administrasi, bukan teks anak.

## Tahap 3 — Stimulus terlebih dahulu

Stimulus aktual harus tersedia sebelum butir dinyatakan selesai.

Periksa lima syarat:

1. Relevan dengan tugas.
2. Cukup tanpa perlengkapan tambahan.
3. Jelas bagi anak.
4. Netral dan tidak membocorkan jawaban atau strategi.
5. Akurat serta konsisten dengan pertanyaan, respons, dan rubrik.

Stimulus harus tampil pada butir yang sama dengan pertanyaan. `image_description` saja bukan stimulus. Jika gambar gagal tampil, soal gagal dan tidak boleh diajukan.

## Tahap 4 — Peta bukti

Untuk setiap soal, tulis hubungan berikut sebelum memasukkannya ke JSON:

| Unsur | Isi |
|---|---|
| Pertanyaan | Tugas yang dibaca anak |
| Stimulus | Gambar atau informasi yang benar-benar tampil |
| Respons | Tindakan, ucapan, pilihan, tulisan, atau susunan anak |
| Bukti | Kemampuan yang dapat diamati |
| Rubrik/kunci | Cara memeriksa bukti |
| Indikator | Alasan soal berada pada indikator tersebut |

Setiap kriteria rubrik harus memeriksa bukti yang berbeda dan tidak boleh menghitung kesalahan yang sama dua kali.

## Tahap 5 — Variasi sepuluh soal

Buat matriks variasi sebelum menulis sepuluh butir. Variasi harus bermakna pada data, stimulus, representasi, hubungan, konteks, atau respons.

Perubahan warna, nama, posisi, atau angka kecil saja tidak otomatis menjadi variasi substantif. Semua soal dalam satu kelompok tetap:

- mengukur kemampuan utama yang sama;
- berada pada kategori dan cakupan yang sama;
- memiliki kompleksitas relatif seragam;
- menuntut bukti esensial yang sama.

## Tahap 6 — Panduan dan penilaian

Panduan orang tua harus menjelaskan cara mendampingi tanpa:

- menyediakan perlengkapan tambahan;
- mengajarkan konsep atau strategi yang sedang diukur;
- mengarahkan jawaban;
- membetulkan respons sebelum dicatat.

Metode dan rubrik ditentukan berdasarkan bukti, bukan berdasarkan kemudahan teknis.

## Tahap 7 — Telaah lawan sebelum kemasan

Sebelum membuat JSON atau HTML, lakukan telaah dengan membaca soal seolah-olah menjadi anak dan orang tua:

- hapus atau sembunyikan seluruh metadata;
- baca pertanyaan bersama stimulus aktual;
- periksa gambar yang hilang, rusak, atau tidak terbaca;
- cari kata yang tidak alami atau ambigu;
- cari jalan pintas menuju jawaban;
- cocokkan respons dengan bukti;
- cocokkan rubrik dengan respons;
- pastikan soal tidak meminta kemampuan di luar indikator.

Satu temuan kritis menghentikan proses dan memicu penulisan ulang.

## Tahap 8 — Kemasan teknis

Setelah konten lulus telaah:

1. Tulis JSON dengan tepat 14 atribut.
2. Kaitkan stimulus aktual dengan ID soal.
3. Hasilkan HTML dari JSON dan gambar versi yang sama.
4. Buka HTML pada browser.
5. Periksa Mode Pemeriksaan dan Mode Pengerjaan.
6. Uji alur respons, penilaian, laporan, dan percabangan yang berlaku.

Validator JSON hanya memeriksa struktur; validator tidak membuktikan soal masuk akal atau stimulus terlihat.

## Tahap 9 — Ceklis dan pengajuan

Sebelum pengajuan, isi `docs/ceklist_lolos_soal.md` pada tingkat soal, kelompok, dan keseluruhan yang berlaku.

Pengajuan ditahan jika:

- ada kriteria Belum diuji atau Gagal;
- stimulus tidak terlihat;
- pertanyaan tidak alami atau ambigu;
- hubungan indikator–bukti–respons–rubrik tidak jelas;
- variasi belum bermakna;
- koleksi antiduplikasi belum lengkap;
- bukti pemeriksaan belum tersimpan.

## Koreksi terhadap metode sebelumnya

Metode sebelumnya terlalu cepat berpindah dari analisis ke JSON, gambar, dan HTML. Draf pertanyaan dibuat sebagai variasi template, lalu kelulusan teknis dipakai sebagai indikasi kesiapan. Metode itu tidak cukup dan tidak boleh digunakan lagi.

PR produksi yang dibuat dengan metode lama harus dibangun ulang, bukan hanya diperbaiki dengan mengganti beberapa kata.
