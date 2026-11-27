---
name: pembuatan-gambar
description: Membuat secara programatis, memeriksa, menyimpan, dan mengintegrasikan gambar aktual Bank Soal SD kelas 1–6 berdasarkan kompetensi, rancangan indikator, spesifikasi visual, sepuluh kriteria kualitas gambar, standar antiduplikasi, keputusan Romo, dan mekanisme persetujuan yang telah ditetapkan dalam dokumen induk resmi dan AGENTS.md.
---

# Skill Pembuatan Gambar Bank Soal SD

## 1. Tujuan dan cakupan

Gunakan skill ini untuk seluruh pekerjaan yang berkaitan dengan kebutuhan, spesifikasi, pembuatan secara programatis, pemeriksaan, penyimpanan, integrasi, dan tindakan korektif terhadap gambar Bank Soal SD kelas 1–6.

Gambar merupakan bagian substansi soal apabila diperlukan untuk pengukuran kompetensi, stimulus atau pembelajaran, bukan sekadar hiasan.

Utamakan ketepatan pendidikan, matematis dan konseptual daripada keindahan visual.

Gunakan metode programatis dalam pembuatan gambar Bank Soal SD sesuai keputusan Romo.

Skill ini berlaku untuk seluruh mata pelajaran, fase, kelas, indikator, serta empat jenis soal: Diagnostik, Penguatan, Pengayaan, dan Cek Ulang.

Penerapan skill tidak memberikan kewenangan untuk memulai produksi sebelum tahapan migrasi dan seluruh prasyarat produksi dipenuhi.

## 2. Sumber acuan dan hierarki

Gunakan sumber resmi yang telah disetujui, dengan hierarki:

1. Keputusan Romo yang telah disetujui.
2. Dokumen induk final V5-salinan 62 (setelah penetapan eksplisit) yang ditetapkan sebagai acuan bersama.
3. Rancangan indikator yang telah disetujui.
4. AGENTS.md dan SKILL.md yang relevan.
5. Instruksi penugasan Codex.

Dokumen induk aktif pada saat pelaksanaan adalah `ringkasan_bank_soal_sd_v5-salinan 62.md` di root repositori. Rujukan V4-51 di bagian lain dibaca sebagai riwayat jika telah digantikan oleh V5.

Gunakan khususnya:

- Bab 19.1 tentang identitas dan ketertelusuran soal.
- Bab 19.2 tentang 14 atribut dan pengisian bersyarat.
- Bab 19.3 tentang 18 kriteria kualitas soal.
- Bab 19.4 tentang tahapan penyusunan dan persetujuan.
- Bab 19.5 tentang JSON, HTML dan pengelolaan berkas gambar.
- Bab 19.6 tentang pembuatan dan verifikasi gambar.
- Bab 19.8 tentang standar antiduplikasi.
- Bab 20 tentang kolaborasi, perangkat produksi, verifikasi dan persetujuan.

Gunakan AGENTS.md dan skill penyusunan-soal yang telah ditetapkan.

Terapkan lima ketentuan keputusan khusus Romo mengenai perangkat pembuatan gambar:

1. AI Image Generation dikeluarkan dari daftar kandidat perangkat pembuatan gambar.
2. Pembuatan gambar menggunakan metode programatis.
3. Python Pillow, SVG programatis, Matplotlib, serta Blender dan Python API merupakan kandidat yang akan dievaluasi pada Tahap 3.
4. AI Image Generation tidak digunakan sebagai metode alternatif ketika terdapat kesulitan teknis.
5. Keputusan terbaru tersebut membatasi ketentuan terdahulu mengenai alat generasi gambar; gunakan dokumen induk V5 aktif dan jangan menghidupkan kembali ketentuan historis yang telah digantikan.

Keputusan tersebut berlaku sesuai hierarki kewenangan yang telah ditetapkan.

Jangan menggunakan ringkasan percakapan sebagai pengganti sumber resmi.

Apabila terdapat konflik, ketidakjelasan atau keputusan yang belum ditetapkan, hentikan pekerjaan yang terdampak dan laporkan kepada ChatGPT dan Romo.

Jangan menyelesaikan konflik keputusan pendidikan secara sepihak.

## 3. Prasyarat penggunaan skill

Sebelum melaksanakan pekerjaan:

1. Periksa kondisi aktual repositori, remote main, cabang dasar, cabang kerja dan working tree.
2. Temukan dan baca secara eksplisit dokumen induk resmi, AGENTS.md dan SKILL.md yang relevan.
3. Periksa identitas serta lingkup penugasan.
4. Periksa indikator induk yang telah ditetapkan.
5. Periksa rancangan indikator dan persetujuan tahap sebelumnya apabila dipersyaratkan.
6. Periksa pertanyaan, bentuk respons, jawaban atau rubrik, kebutuhan stimulus dan batas kompetensi.
7. Periksa ketersediaan perangkat pembuatan gambar programatis dan perangkat pemeriksaan yang relevan.
8. Periksa register, versi gambar, berkas soal dan bukti pemeriksaan sebelumnya apabila tersedia.
9. Periksa ketersediaan koleksi pembanding aktif untuk pemeriksaan antiduplikasi yang relevan.

Jangan menganggap perangkat produksi telah tersedia atau terverifikasi hanya karena namanya tercantum dalam dokumen induk atau daftar kandidat teknologi.

Gunakan perangkat pembuatan gambar produksi yang telah ditetapkan dan diverifikasi pada tahapan migrasi terkait.

Penyusunan dan pembuatan gambar produksi mengikuti tahapan migrasi dan persetujuan yang telah ditetapkan.

Laporkan prasyarat yang belum terpenuhi dan hentikan pekerjaan yang tidak dapat dilanjutkan secara sah.

## 4. Identifikasi penugasan dan kompetensi

Pastikan setiap pekerjaan gambar terkait dengan identitas soal dan indikator yang sah.

Periksa:

- Mata pelajaran, fase dan kelas.
- CP, TP, KM dan indikator induk.
- ID indikator dan ID soal.
- Jenis serta nomor soal.
- Tahap penyusunan yang sedang dilaksanakan.
- Kemampuan utama yang diukur.
- Bukti penguasaan yang diharapkan.
- Batas materi dan kompetensi.
- Pertanyaan, bentuk respons serta metode penilaian.
- Rancangan visual yang telah disetujui apabila dipersyaratkan.

Gunakan identitas soal sesuai Bab 19.1.

Jangan mengubah identitas indikator, substansi kompetensi atau rancangan pendidikan melalui pembuatan gambar.

Pekerjaan produksi tetap dibatasi satu indikator dan satu tahap penyusunan dalam setiap penugasan sesuai AGENTS.md.

## 5. Penentuan kebutuhan gambar

Tentukan kebutuhan gambar berdasarkan fungsi visual dalam pengukuran kompetensi, stimulus atau pembelajaran.

Gunakan atribut `butuh_gambar` dengan nilai boolean.

Jika `butuh_gambar = true`:

- `image_description` wajib terisi.
- `image_spec` wajib terisi dengan nilai `2D` atau `3D`.
- Gambar aktual wajib tersedia sebelum soal bergambar difinalisasi.
- Gambar aktual wajib diperiksa sesuai ketentuan dokumen induk.

Jika `butuh_gambar = false`:

- `image_description` bernilai `null`.
- `image_spec` bernilai `null`.
- Status gambar pada register adalah Tidak diperlukan.

Jangan menggunakan `null` untuk menyembunyikan gambar yang belum dibuat atau spesifikasi yang belum lengkap.

Jangan menambahkan gambar semata-mata untuk memenuhi jumlah gambar tertentu atau memperindah tampilan.

Kebutuhan gambar ditentukan berdasarkan kompetensi, bentuk tugas, rancangan dan kebutuhan pembelajaran, bukan kemudahan teknis pembuatannya.

Jangan mengubah kebutuhan gambar yang telah disetujui secara substantif tanpa mekanisme persetujuan yang berlaku.

Pertahankan tepat 14 atribut soal. Jangan menambahkan atribut status gambar, versi, hash atau hasil pemeriksaan ke dalam struktur data soal.

## 6. Penyusunan deskripsi dan spesifikasi gambar

Susun `image_description` agar kebutuhan visual dapat dipahami, dibuat dan diperiksa terhadap kompetensi, pertanyaan serta jawaban atau rubrik.

Deskripsi memuat unsur yang relevan dengan tugas, antara lain:

- Objek atau representasi visual yang diperlukan.
- Jumlah objek apabila relevan.
- Bentuk dan sifat objek apabila relevan.
- Warna apabila relevan.
- Ukuran dan perbandingan ukuran apabila relevan.
- Posisi, arah, susunan dan hubungan spasial apabila relevan.
- Data, tanda atau informasi visual yang diperlukan.
- Hubungan visual dengan tugas dan bukti penguasaan.

Tidak semua unsur harus ditambahkan apabila tidak diperlukan oleh kompetensi.

Gunakan `image_spec` hanya dengan nilai `2D` atau `3D` sesuai kebutuhan representasi.

Bedakan spesifikasi visual dari format penyimpanan berkas.

SVG dan PNG merupakan contoh format berkas, bukan nilai pengganti `image_spec`.

Representasi bangun ruang atau hubungan spasial dapat disajikan dalam gambar pada layar selama spesifikasi dan substansi visualnya terpenuhi.

Periksa deskripsi dan spesifikasi sebelum membuat gambar aktual.

Jangan menambahkan informasi yang mengubah pertanyaan, menggeser kompetensi, menambah kompleksitas yang tidak disetujui atau membocorkan jawaban pada tahap penilaian.

Apabila rancangan visual belum cukup jelas untuk dibuat dan diperiksa, laporkan kekurangan dan selesaikan sesuai kewenangan yang berlaku.

## 7. Pemilihan metode dan perangkat pembuatan gambar

Gunakan metode programatis dalam pembuatan gambar Bank Soal SD.

Pilih metode berdasarkan karakteristik visual, kompetensi, spesifikasi dan kebutuhan ketepatan substansi.

Pertahankan ketentuan Bab 20.4 yang tidak bertentangan dengan keputusan terbaru Romo, termasuk penggunaan:

- SVG untuk bangun datar, kumpulan benda, garis bilangan, denah dan pola apabila sesuai.
- PNG untuk ilustrasi raster apabila sesuai.
- Visualisasi 3D untuk bangun ruang dan hubungan spasial apabila sesuai.

Pemilihan dan penetapan perangkat lunak, pustaka, serta teknologi pembuatan gambar dilakukan pada Tahap 3 — Pembangunan Perangkat Produksi.

Evaluasi empat kandidat berikut sesuai kebutuhan:

1. Python Pillow untuk pembuatan dan pengolahan gambar raster 2D.
2. SVG programatis untuk visual vektor, geometri dan representasi matematis yang presisi.
3. Matplotlib untuk grafik, diagram dan visualisasi data.
4. Blender beserta Python API untuk visualisasi 3D, bangun ruang dan hubungan spasial.

Keempat kandidat tersebut merupakan usulan teknologi yang akan dievaluasi, bukan penetapan penggunaan wajib atau bukti bahwa perangkat telah tersedia.

Pemilihan perangkat mempertimbangkan:

- Ketepatan substansi.
- Kemampuan otomatisasi.
- Konsistensi hasil.
- Keterulangan proses pembuatan.
- Kebutuhan sumber daya.
- Ketersediaan dalam environment Codex.
- Integrasi dengan GitHub dan HTML mandiri.
- Kemudahan pemeriksaan serta tindakan korektif.

Jangan memilih metode hanya berdasarkan keindahan atau kecepatan pembuatan apabila mengurangi ketepatan pendidikan.

Periksa kemampuan metode menghasilkan jumlah, bentuk, posisi, ukuran, hubungan dan sifat matematis yang dipersyaratkan.

Jangan menganggap gambar benar hanya karena dihasilkan oleh perangkat programatis.

Jangan menggunakan AI Image Generation untuk menghasilkan gambar Bank Soal SD, termasuk sebagai metode alternatif ketika terdapat kesulitan pembuatan gambar.

Apabila gambar sulit dibuat secara programatis, laporkan kendala teknis dan ajukan penyelesaian sesuai kewenangan yang berlaku tanpa mengubah kompetensi atau rancangan pendidikan secara sepihak.

Rincian bahasa pemrograman, modul, algoritma, format berkas dan implementasi perangkat produksi diselesaikan pada Tahap 3.

Perangkat yang dipilih harus diuji dan diverifikasi pada Tahap 4 sebelum digunakan dalam produksi Bank Soal.

Jangan membangun perangkat produksi atau memperluas daftar teknologi yang disetujui di luar lingkup penugasan.

## 8. Prosedur pembuatan gambar aktual

Ikuti enam tahap Bab 19.6:

1. Menentukan kebutuhan gambar (`butuh_gambar`).
2. Menyusun `image_description` dan `image_spec`.
3. Memeriksa spesifikasi terhadap kompetensi, pertanyaan dan jawaban.
4. Membuat gambar aktual secara programatis.
5. Memeriksa gambar aktual secara visual dan matematis.
6. Menyimpan gambar, mengaitkan dengan ID soal, dan memasukkannya ke HTML.

Gunakan metode programatis dan perangkat yang telah ditetapkan serta diverifikasi.

Pastikan hasil pembuatan berupa gambar aktual yang dapat diperiksa, bukan sekadar deskripsi, prompt, placeholder atau tautan yang belum diverifikasi.

Periksa hasil terhadap stimulus, pertanyaan dan jawaban atau rubrik yang menggunakan gambar tersebut.

Jika gambar merupakan bagian penjelasan konsep atau penerapan nyata, pertahankan fungsi pembelajaran dan ketentuan jenis soal.

Jangan menggunakan gambar untuk mengubah metode penilaian atau memberikan petunjuk jawaban yang tidak sesuai pada tahap penilaian.

Jangan meminta orang tua menyiapkan benda, membeli perlengkapan, menggambar manual, mencetak materi atau mencari gambar tambahan.

Jika gambar aktual belum dapat dibuat, laporkan kendala dan jangan menyatakan soal bergambar siap difinalisasi.

Jangan mengatasi kendala tersebut dengan menggunakan metode pembuatan gambar yang telah ditolak atau mengubah rancangan pendidikan secara sepihak.

## 9. Sepuluh kriteria kualitas gambar

Gunakan seluruh sepuluh kriteria kualitas gambar Bab 19.6:

1. Sesuai kebutuhan kompetensi.
2. Sesuai `image_description`.
3. Sesuai spesifikasi 2D atau 3D.
4. Benar secara matematis dan konseptual.
5. Jumlah, bentuk, warna, ukuran, dan posisi tepat apabila relevan.
6. Jelas dan mudah diamati anak.
7. Tidak mengandung elemen visual yang membingungkan.
8. Konsisten dengan pertanyaan dan jawaban.
9. Tidak membocorkan jawaban pada tahap penilaian.
10. Tidak membutuhkan perlengkapan tambahan dari orang tua.

Periksa gambar aktual terhadap setiap kriteria yang berlaku.

Jika suatu kriteria tidak relevan, gunakan status Tidak berlaku dengan alasan yang sesuai.

Jangan menambah, mengurangi, atau mengganti sepuluh kriteria tersebut secara sepihak.

Utamakan ketepatan substansi daripada keindahan.

Gambar yang tidak sesuai dengan jumlah, bentuk, ukuran, warna, posisi, hubungan atau sifat yang relevan harus diperbaiki atau dibuat ulang.

Kelulusan kualitas gambar tidak menggantikan 18 kriteria kualitas soal, pemeriksaan antiduplikasi atau persetujuan Romo.

## 10. Penyimpanan gambar dan ketertelusuran identitas

Simpan gambar asli yang digunakan oleh soal pada struktur direktori Bank Soal yang ditetapkan.

Ikuti Bab 19.5 dan Bab 20.2.

Gunakan direktori `gambar/` dalam struktur kelas yang relevan, sesuai pengelolaan berkas yang disetujui.

Kaitkan gambar secara jelas dan dapat ditelusuri dengan ID soal yang sah.

Pastikan berkas yang diperiksa adalah berkas aktual yang digunakan dalam hasil produksi.

Pertahankan hubungan antara:

- ID soal.
- ID indikator.
- Deskripsi dan spesifikasi gambar.
- Berkas gambar aktual.
- Versi soal dan gambar yang diperiksa.
- Lokasi berkas dan bukti pemeriksaan.
- HTML yang menggunakan gambar tersebut.

Jangan menetapkan atribut JSON soal tambahan untuk menyimpan status, versi, sidik digital atau hasil pemeriksaan gambar.

Gunakan register dan data pemeriksaan terpisah sesuai ketentuan yang berlaku.

Pertahankan ID soal apabila revisi masih dilakukan terhadap entitas dan slot hierarkis yang sama.

Jangan menghilangkan riwayat versi atau menimpa hasil final tanpa kewenangan dan persetujuan yang diperlukan.

## 11. Integrasi dengan JSON dan HTML

JSON tetap merupakan sumber data tunggal konten soal dengan tepat 14 atribut.

Gunakan gambar yang sesuai dengan data soal pada versi yang diperiksa.

Koordinasikan integrasi gambar dengan skill generator-html.

HTML wajib menyediakan:

1. Mode Pemeriksaan Bank Soal.
2. Mode Pengerjaan Soal Interaktif.

Pada Mode Pemeriksaan, tampilkan gambar aktual, deskripsi dan spesifikasi yang relevan sesuai Bab 19.5.

Pada Mode Pengerjaan, tampilkan gambar yang sesuai kebutuhan tugas dan pembelajaran tanpa membocorkan jawaban pada tahap penilaian.

Sematkan data dan gambar pada HTML sesuai ketentuan HTML mandiri.

Pastikan:

- Gambar tampil pada kedua mode.
- Gambar terkait dengan ID soal yang benar.
- Gambar tidak terpotong sehingga menghilangkan informasi penting.
- Proporsi gambar tidak berubah sehingga mengubah makna matematis atau konseptual.
- Gambar jelas pada komputer, tablet dan ponsel.
- Gambar tetap tersedia ketika HTML dibuka tanpa internet.
- Gambar tetap tersedia ketika HTML dipindahkan.
- JSON, gambar, pertanyaan, jawaban, rubrik dan HTML berasal dari versi yang konsisten.

Periksa hasil tampilan aktual menggunakan perangkat pengujian browser yang tersedia.

Jangan menyatakan fungsi tampilan lulus hanya berdasarkan kode, deskripsi atau keberadaan gambar asli.

Pertahankan berkas gambar asli secara terpisah.

Jangan menjadikan HTML sebagai sumber soal terpisah atau mengubah substansi pendidikan melalui proses integrasi gambar.

## 12. Pemeriksaan antiduplikasi visual

Terapkan seluruh ketentuan Bab 19.8.1–19.8.8 yang relevan dengan stimulus visual.

Gunakan Detektor Antiduplikasi Soal yang telah dibangun dan diverifikasi pada tahapan migrasi terkait.

Pemeriksaan visual mencakup:

1. Sidik digital berkas untuk menemukan gambar identik.
2. Kemiripan tampilan untuk menemukan gambar hampir sama meskipun format, ukuran atau tampilan berubah.
3. Analisis substansi visual terhadap informasi yang relevan dengan kompetensi.

Periksa gambar aktual.

`image_description` dan `image_spec` merupakan informasi pendukung, bukan pengganti pemeriksaan gambar.

Kesamaan gambar tidak otomatis merupakan duplikasi soal.

Perubahan warna, bentuk, posisi, ukuran, konteks atau tampilan yang hanya bersifat kosmetik tidak cukup untuk membedakan soal.

Gunakan tujuh kategori duplikasi DUP-01–DUP-07 dan enam kategori variasi VAR-01–VAR-06 sesuai rumusan dokumen induk.

Pastikan variasi yang dipertahankan memenuhi keenam kriteria penerimaan variasi Bab 19.8.2 secara bersama-sama.

Lakukan pemeriksaan visual pada titik pemeriksaan antiduplikasi yang relevan, dalam kerangka enam titik pemeriksaan wajib:

1. Sebelum produksi.
2. Saat penyusunan setiap butir.
3. Setelah kelompok 10 soal selesai.
4. Setelah revisi.
5. Saat verifikasi keseluruhan 40 soal.
6. Sebelum finalisasi.

Gunakan koleksi pembanding global seluruh soal aktif, bukan hanya gambar dalam satu indikator.

Cakup soal aktif pada main, cabang kerja relevan dan draf aktif yang diketahui, tanpa menghitung satu entitas secara berulang.

Jangan memasukkan cabang historis, versi tergantikan dan data uji sebagai entitas soal aktif tambahan.

Gunakan hasil programatis untuk mendukung pemeriksaan pedagogis.

Jangan menggunakan satu ambang persentase kemiripan sebagai keputusan mutlak duplikasi.

Jika gambar sama atau hampir sama, periksa tugas, tuntutan respons, kompetensi, data visual dan kebermaknaan perbedaan.

Tangani temuan berdasarkan empat kategori kesimpulan Bab 19.8.4 dan ketentuan korektif Bab 19.8.6.

Jika koleksi aktif belum lengkap, kandidat belum diselesaikan, bukti belum cukup atau perangkat gagal, jangan menyatakan antiduplikasi lulus.

Tidak ada skill tambahan khusus antiduplikasi. Koordinasikan pemeriksaan melalui lima skill dan perangkat yang telah ditetapkan.

## 13. Verifikasi, bukti pemeriksaan dan tindakan korektif

Periksa gambar aktual secara visual, matematis dan konseptual.

Gunakan sepuluh kriteria kualitas gambar, pemeriksaan integrasi HTML dan standar antiduplikasi yang berlaku.

Gunakan empat tingkat pemeriksaan kolaborasi Bab 20.6:

1. Struktural.
2. Fungsional.
3. Substansi dan visual.
4. Persetujuan akhir Romo.

Gunakan empat status pemeriksaan:

- Lulus: benar-benar diperiksa dan berhasil.
- Gagal: ditemukan kekurangan.
- Belum diuji: belum diperiksa.
- Tidak berlaku: kriteria tidak relevan.

Jangan memberikan status Lulus berdasarkan rencana, dugaan, deskripsi atau keberadaan kode.

Jika ditemukan ketidaksesuaian, lakukan koreksi yang diizinkan berupa perbaikan atau pembuatan ulang gambar secara programatis.

Pertahankan kompetensi, indikator, jenis soal, kompleksitas, bentuk respons, jawaban atau rubrik, dan rancangan yang disetujui.

Perubahan yang memengaruhi substansi soal harus dikoordinasikan dengan skill penyusunan-soal dan mengikuti batas kewenangan berdasarkan status persetujuan soal.

Pertahankan gambar atau soal final sesuai prioritas pemeliharaan Bab 19.8.6.

Jangan mengubah gambar final secara substantif tanpa persetujuan Romo.

Periksa ulang hasil koreksi terhadap spesifikasi, kriteria kualitas, pertanyaan, jawaban, HTML dan ketentuan antiduplikasi yang relevan.

Lakukan pemeriksaan ulang terhadap koleksi aktif global jika revisi memengaruhi validitas pemeriksaan antiduplikasi sebelumnya.

Simpan bukti antiduplikasi terpisah sesuai Bab 19.8.4 dan Bab 19.8.7.

Pertahankan sembilan informasi minimum bukti pemeriksaan kandidat beserta metadata teknis, versi dan riwayat penyelesaian yang dipersyaratkan.

Jangan menambahkan informasi pemeriksaan tersebut ke dalam 14 atribut soal.

Jika perangkat gagal, gambar tidak dapat diperiksa, hasil pemeriksaan belum lengkap atau terdapat ketidakpastian pedagogis yang belum terselesaikan, laporkan kendala dan tahan kelulusan.

Pemeriksaan otomatis tidak menggantikan pemeriksaan visual aktual, pemeriksaan substansi pendidikan atau persetujuan akhir Romo.

## 14. Koordinasi antarskill, register dan persetujuan

Koordinasikan pembuatan gambar dengan empat skill lainnya.

Skill penyusunan-soal:

- Menyediakan identitas soal, rancangan, kompetensi, kebutuhan visual, pertanyaan dan jawaban atau rubrik.
- Menjaga kesesuaian antara gambar dan substansi soal.
- Menangani perubahan soal yang diperlukan sesuai kewenangan.

Skill generator-html:

- Mengintegrasikan gambar aktual yang sesuai dengan JSON.
- Menjaga tampilan kedua mode dan fungsi HTML mandiri.
- Memeriksa dampak perubahan gambar terhadap HTML.

Skill verifikasi-bank-soal:

- Memeriksa kualitas gambar aktual dan kesesuaian dengan soal.
- Memeriksa kelengkapan integrasi, bukti antiduplikasi dan syarat kelulusan.
- Menahan pengajuan final apabila pemeriksaan wajib belum lengkap.

Skill pembaruan-register:

- Mencatat lokasi dan versi gambar aktif.
- Mencatat status gambar, hasil pemeriksaan, bukti, persetujuan dan progres.
- Tidak menghitung draf atau gambar yang belum diperiksa sebagai hasil final.

Gunakan empat status gambar pada register sesuai Bab 19.6:

1. Tidak diperlukan: soal tidak membutuhkan gambar.
2. Spesifikasi selesai: deskripsi dan spesifikasi tersedia, gambar belum dibuat.
3. Gambar tersedia: gambar dibuat, belum diverifikasi.
4. Gambar terverifikasi: gambar aktual memenuhi kriteria dan tampilan terkait telah diperiksa.

Status gambar bukan atribut tambahan soal.

Bedakan status gambar, status pemeriksaan antiduplikasi dan status pengembangan soal.

Gambar terverifikasi tidak otomatis menjadikan soal Final.

Gunakan persetujuan per tahap penyusunan sesuai Bab 19.4 dan Bab 20.7.

Jangan menambah tahap persetujuan tersendiri yang tidak ditetapkan.

Jangan memfinalisasi soal bergambar sebelum gambar aktual tersedia dan terverifikasi serta seluruh syarat finalisasi soal terpenuhi.

## 15. Hasil wajib, keamanan dan titik berhenti

Pada akhir penugasan, laporkan:

1. Identitas tugas, indikator, soal dan sumber acuan.
2. Lingkup pembuatan atau pemeriksaan gambar.
3. Kebutuhan gambar, deskripsi dan spesifikasi.
4. Metode programatis dan perangkat pembuatan yang digunakan.
5. Berkas gambar aktual dan kaitannya dengan ID soal.
6. Hasil sepuluh kriteria kualitas gambar.
7. Hasil pemeriksaan tampilan pada kedua mode HTML sesuai lingkup penugasan.
8. Hasil pemeriksaan antiduplikasi visual dan bukti yang relevan.
9. Tindakan korektif dan pemeriksaan ulang apabila diperlukan.
10. Status gambar dan status pekerjaan aktual.
11. Kendala, pemeriksaan yang belum dijalankan dan persetujuan yang diperlukan.
12. Titik berhenti serta tindakan berikutnya yang masih memerlukan izin.

Jangan menyatakan gambar terverifikasi atau soal Final jika persyaratan wajib belum terpenuhi.

Status Final soal hanya digunakan setelah disetujui, disimpan, diverifikasi dan masuk cabang utama sesuai mekanisme yang berwenang.

Jangan menyertakan kredensial, token, kata sandi atau data pribadi anak nyata dalam berkas, gambar, pengujian maupun laporan.

Jangan menggunakan repositori untuk menyimpan hasil belajar nyata.

Pertahankan status terbuka Komponen 1 dan Komponen 7.

Jangan menetapkan desain teknis penyimpanan permanen hasil belajar, akun atau database melalui skill ini.

Jangan mengubah dokumen induk, AGENTS.md, skill lain, soal final atau rancangan yang disetujui tanpa kewenangan.

Jangan melakukan push langsung ke main, force push, menghapus riwayat atau melakukan merge tanpa persetujuan yang sesuai.

Hentikan pekerjaan setelah lingkup penugasan selesai.

Jangan melanjutkan indikator, tahap penyusunan, pembahasan, tahapan migrasi atau perubahan repositori yang belum diizinkan.

Skill ini merupakan pedoman operasional pelaksanaan keputusan yang telah disetujui, bukan sumber keputusan pendidikan baru.
