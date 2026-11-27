# AGENTS.md — Instruksi Permanen Bank Soal SD

## 1. Identitas dan tujuan proyek

Proyek Bank Soal SD mengembangkan bank soal kelas 1–6 berdasarkan kurikulum nasional Indonesia dan seluruh keputusan pendidikan yang telah disetujui Romo.

- Repositori: `parentingtangguh-png/soalsd`
- Visibilitas: Private
- Cabang utama: `main`
- Environment Codex: `soalsd`
- Bahasa konten pendidikan: Bahasa Indonesia
- Dokumen induk resmi pada saat penetapan instruksi ini: `docs/ringkasan_bank_soal_sd_v4-51.md`

Setelah keputusan Romo pada 26 November 2026, dokumen induk aktif/final yang berlaku adalah `ringkasan_bank_soal_sd_v5-salinan 61.md`; V4-51 dan versi sebelumnya menjadi arsip sejarah.

Gunakan dokumen induk terbaru yang telah disetujui, diverifikasi, dan ditetapkan sebagai acuan bersama.

Jangan memilih versi dokumen hanya berdasarkan nama atau nomor versi terbesar.

Dokumen historis bukan acuan utama apabila telah digantikan oleh versi yang disetujui.

## 2. Hierarki acuan

Ikuti urutan kewenangan berikut, dari tertinggi:

1. Keputusan Romo yang telah disetujui.
2. Dokumen induk final V5-salinan 61 yang telah ditetapkan Romo sebagai acuan bersama.
3. Rancangan indikator yang telah disetujui.
4. AGENTS.md dan SKILL.md.
5. Instruksi tugas Codex.

Instruksi pada tingkat lebih rendah tidak boleh bertentangan dengan tingkat lebih tinggi.

Apabila ditemukan konflik, ketidakjelasan, atau keputusan yang belum ditetapkan, hentikan bagian pekerjaan yang terdampak dan laporkan sumber, lokasi, serta substansi permasalahan.

Jangan menyelesaikan konflik keputusan pendidikan secara sepihak.

## 3. Pembagian peran dan kewenangan

Romo merupakan pemegang kewenangan penetapan kebijakan pendidikan dan persetujuan akhir.

ChatGPT bertanggung jawab atas analisis kompetensi, rancangan pendidikan, penyusunan instruksi Codex, pemeriksaan substansi, dan penyampaian usulan keputusan kepada Romo.

Codex bertanggung jawab melaksanakan pekerjaan teknis dalam lingkup penugasan yang telah ditetapkan, termasuk penyusunan draf soal, gambar, JSON, HTML, pemeriksaan, penyimpanan berkas, dan pembaruan register.

GitHub merupakan pusat pengelolaan berkas, koordinasi, dan riwayat perubahan.

Codex boleh menentukan rincian implementasi teknis yang tidak mengubah substansi pendidikan atau standar yang disetujui.

Codex tidak berwenang:

- Mengubah rumusan dan identitas kompetensi final.
- Menetapkan batas kompetensi yang belum disetujui.
- Mengubah standar penilaian, laporan, percabangan atau ketuntasan.
- Menyetujui hasil pekerjaannya sendiri.
- Menganggap pemeriksaan otomatis sebagai pengganti persetujuan Romo.
- Melanjutkan tahap yang memerlukan persetujuan tanpa bukti persetujuan.

Delegasi pekerjaan tidak mendelegasikan kewenangan pengambilan keputusan.

## 4. Pemeriksaan wajib sebelum bekerja

Sebelum melaksanakan penugasan:

1. Pastikan repositori dan cabang yang digunakan benar.
2. Periksa kondisi aktual cabang dasar dan working tree.
3. Temukan dan baca dokumen induk resmi.
4. Periksa seluruh bagian dokumen induk yang relevan dengan pekerjaan.
5. Periksa instruksi permanen dan skill terkait.
6. Periksa identitas, lingkup, dan batas penugasan.
7. Periksa rancangan serta bukti persetujuan tahap sebelumnya apabila dipersyaratkan.
8. Periksa register, berkas aktual, dan status pekerjaan apabila tersedia dan relevan.
9. Periksa ketersediaan perangkat, data, akses, dan prasyarat pemeriksaan.

Jangan hanya menggunakan ringkasan percakapan sebagai pengganti sumber resmi.

Jangan menganggap isi percakapan ChatGPT otomatis tersedia bagi Codex.

Laporkan prasyarat yang tidak terpenuhi dan hentikan bagian pekerjaan yang tidak dapat dilanjutkan secara sah.

## 5. Tahapan migrasi

Ikuti lima tahap migrasi berdasarkan Bab 20.8:

1. Inisialisasi repositori.
2. Penyiapan instruksi permanen, lima skill, struktur direktori, register dan standar pencatatan persetujuan.
3. Pembangunan delapan perangkat produksi.
4. Verifikasi lingkungan produksi.
5. Penyusunan Bank Soal berdasarkan enam tahap penyusunan setiap indikator.

Jangan memulai tahap migrasi berikutnya sebelum tahap sebelumnya memenuhi persyaratan dan memperoleh persetujuan Romo.

Penyusunan soal tidak boleh dimulai sebelum perangkat produksi tersedia, terverifikasi, dan persiapan produksi disetujui.

Bedakan tahap migrasi dengan enam tahap penyusunan soal dalam satu indikator.

## 6. Standar pendidikan yang wajib dipertahankan

Seluruh keputusan final dalam dokumen induk wajib dipertahankan, termasuk:

- Hierarki CP, ATP, TP, KM, indikator, soal, penilaian dan laporan.
- Identitas dan ketertelusuran kompetensi.
- Empat jenis soal dengan masing-masing 10 butir untuk setiap indikator.
- Kompetensi yang sama pada keempat jenis soal.
- Kompleksitas relatif seragam dalam masing-masing kelompok.
- Cek Ulang lebih kompleks daripada Diagnostik.
- Pengayaan tidak wajib lebih kompleks daripada Penguatan.
- Penjelasan konsep dan penerapan nyata pada setiap soal Penguatan dan Pengayaan.
- Panduan orang tua pada setiap soal tanpa meminta perlengkapan tambahan.
- Penilaian otomatis atau penilaian orang tua melalui ceklis.
- Pembobotan kriteria rubrik yang sama dan perhitungan proporsional.
- Bobot setiap soal yang sama dalam kelompok.
- Kewajiban menjawab seluruh 10 soal sebelum kelompok selesai.
- Percabangan Diagnostik 100% menuju Pengayaan dan di bawah 100% menuju Penguatan.
- Cek Ulang 100% berarti Tuntas dan di bawah 100% berarti Belum Tuntas.
- Laporan konkret pada setiap kelompok soal yang diselesaikan.
- Tidak ada pengulangan soal yang diwajibkan setelah Cek Ulang.

Gunakan ketentuan lengkap dalam dokumen induk. Ringkasan ini tidak menggantikan ketentuan tersebut.

Komponen 1 dan Komponen 7 yang masih terbuka tidak boleh diselesaikan secara sepihak.

## 7. Identitas dan struktur data soal

Gunakan standar identitas soal Bab 19.1:

`SOAL-{kode_mapel}-{fase}-K{kelas}-{kode_tp}-KM{nomor_km}-I{nomor_indikator}-{kode_jenis_soal}-{nomor_soal}`

Kode jenis soal:

- DIA: Diagnostik.
- PGT: Penguatan.
- PYN: Pengayaan.
- CU: Cek Ulang.

Nomor soal dimulai dari 01 sampai 10 pada setiap jenis dalam setiap indikator.

Pertahankan identitas soal ketika melakukan revisi terhadap entitas soal yang sama.

Setiap soal menggunakan tepat 14 atribut berdasarkan Bab 19.2:

1. id_soal
2. id_indikator
3. jenis_soal
4. pertanyaan
5. pilihan
6. kunci_jawaban
7. panduan_orang_tua
8. penjelasan_konsep
9. penerapan_nyata
10. butuh_gambar
11. image_description
12. image_spec
13. metode_penilaian
14. rubrik_penilaian

Seluruh atribut harus tersedia dan diisi berdasarkan aturan wajib serta aturan bersyarat dalam dokumen induk.

Gunakan null sesuai kondisi yang ditetapkan, bukan untuk menyembunyikan ketidaklengkapan.

Jangan menambahkan atribut status produksi, persetujuan, versi, atau antiduplikasi ke dalam 14 atribut soal.

Simpan informasi pengelolaan tersebut secara terpisah berdasarkan register dan standar pencatatan yang disetujui.

## 8. Prosedur penyusunan soal

Setiap penugasan produksi hanya mencakup satu indikator dan satu tahap penyusunan.

Ikuti urutan ATP, KM, dan indikator yang telah disetujui.

Enam tahap penyusunan:

1. Analisis dan rancangan empat jenis soal.
2. Penyusunan 10 Diagnostik.
3. Penyusunan 10 Penguatan.
4. Penyusunan 10 Pengayaan.
5. Penyusunan 10 Cek Ulang.
6. Verifikasi akhir seluruh 40 soal.

Pada tahap analisis dan rancangan, gunakan keputusan khusus indikator yang telah disetujui Romo sebagai dasar produksi.

Jangan menetapkan sendiri batas numerik, metode penilaian khusus, atau bentuk respons yang masih memerlukan keputusan.

Jangan menyusun kelompok soal sebelum rancangan dan tahap sebelumnya disetujui.

Setiap hasil kelompok soal wajib memenuhi 18 kriteria kualitas pada Bab 19.3.

**Gerbang ceklis wajib sebelum pengajuan:** sebelum hasil soal, gambar, JSON, HTML, kelompok soal, atau verifikasi diajukan untuk persetujuan, seluruh kriteria kualitas yang berlaku harus diperiksa dan berstatus **Lulus** pada ceklis terdokumentasi. Status **Belum diuji**, **Gagal**, atau **Tidak berlaku tanpa alasan yang sah** menghentikan pengajuan. Ceklis harus mencantumkan ID indikator, tahap, versi berkas, commit, pemeriksa, tanggal, bukti, dan temuan. Pemeriksaan otomatis tidak menggantikan pemeriksaan substansi, visual, fungsional, antiduplikasi, atau persetujuan Romo.

Siapkan berkas nyata, gambar aktual jika diperlukan, dan laporan pemeriksaan sebelum mengajukan persetujuan.

## 9. Pembuatan dan verifikasi gambar

Ikuti seluruh ketentuan Bab 19.6 dan bagian antiduplikasi visual yang relevan.

Apabila soal membutuhkan gambar:

1. Tentukan kebutuhan dan spesifikasi gambar sesuai soal.
2. Buat gambar aktual.
3. Periksa kesesuaian gambar terhadap kompetensi, pertanyaan, jawaban, dan spesifikasi.
4. Periksa ketepatan matematis dan konseptual.
5. Periksa seluruh sepuluh kriteria kualitas gambar.
6. Simpan gambar asli dan kaitkan dengan ID soal.
7. Periksa tampilan gambar pada kedua mode HTML.

Utamakan metode programatis jika sesuai dengan kebutuhan visual Matematika.

Pemilihan format gambar tidak menggantikan ketentuan image_spec 2D atau 3D.

Jangan menyatakan gambar terverifikasi hanya karena deskripsinya tersedia.

Jika gambar belum dapat dibuat atau diverifikasi, laporkan kendala dan pertahankan status soal belum final.

## 10. Pengelolaan JSON dan HTML

JSON merupakan sumber data tunggal soal.

Setiap indikator memiliki satu file JSON yang berkembang sesuai kelompok soal yang telah disetujui hingga mencapai 40 soal.

Setiap indikator memiliki satu file HTML mandiri yang dihasilkan dari JSON dan gambar terkait.

HTML wajib memiliki:

- Mode Pemeriksaan Bank Soal.
- Mode Pengerjaan Soal Interaktif.

Ikuti seluruh standar Bab 19.5, termasuk 14 fungsi wajib Mode Pengerjaan.

HTML harus dapat dibuka langsung tanpa internet, dapat dipindahkan tanpa kehilangan data atau gambar, serta dapat digunakan pada komputer, tablet, dan ponsel.

Draf parsial wajib menunjukkan status kelengkapan.

Jangan menjalankan percabangan menuju kelompok soal yang belum tersedia.

Gunakan data, soal, jawaban, rubrik dan gambar pada versi yang sama.

Jangan menjadikan HTML sebagai sumber soal terpisah atau mengubah substansi soal melalui HTML.

HTML mandiri merupakan prototipe, bukan penetapan desain sistem penyimpanan permanen hasil belajar.

## 11. Standar antiduplikasi

Seluruh ketentuan Bab 19.8.1–19.8.8 wajib diterapkan.

Antiduplikasi merupakan bagian permanen dari produksi Bank Soal, bukan pemeriksaan tambahan yang dapat dilewati.

Gunakan Detektor Antiduplikasi Soal dan pemeriksaan pedagogis sesuai tahap yang relevan.

Pemeriksaan mencakup identitas, konten, struktur, semantik, visual, dan ketentuan lain yang ditetapkan dalam dokumen induk.

Laksanakan pemeriksaan pada enam titik wajib:

1. Sebelum produksi.
2. Per butir soal.
3. Per kelompok soal.
4. Setelah revisi.
5. Saat verifikasi keseluruhan 40 soal.
6. Sebelum finalisasi.

Gunakan koleksi pembanding global yang lengkap, mencakup soal aktif pada main, cabang kerja relevan dan draf lokal yang diketahui, sesuai ketentuan Bab 19.8.

Jangan menghitung satu entitas yang sama berulang kali hanya karena terdapat di beberapa cabang.

Jangan memasukkan cabang historis, versi yang telah digantikan, atau data uji sebagai entitas soal aktif tambahan.

Bedakan duplikasi yang terbukti, kandidat kemiripan, dan variasi yang sah berdasarkan definisi dan kriteria yang disetujui.

Jangan menolak soal semata-mata berdasarkan kemiripan struktur atau skor otomatis.

Setiap temuan wajib ditangani sesuai Bab 19.8.6, disertai bukti dan alasan pedagogis.

Simpan bukti pemeriksaan secara terpisah dan dapat ditelusuri terhadap versi konten, gambar, metode, dan koleksi pembanding.

Lakukan pemeriksaan ulang apabila terjadi perubahan yang memengaruhi validitas hasil pemeriksaan sebelumnya.

Jangan memfinalisasi soal apabila:

- Koleksi pembanding belum lengkap.
- Terdapat benturan ID.
- Terdapat duplikasi yang terbukti.
- Kandidat kemiripan belum diselesaikan.
- Bukti pemeriksaan belum lengkap.
- Tindakan korektif belum diperiksa ulang.
- Salah satu dari sepuluh kriteria kelulusan pada Bab 19.8.8.3 belum terpenuhi.

Kelulusan antiduplikasi tidak menggantikan pemeriksaan kualitas lain atau persetujuan Romo.

Tidak ada skill keenam khusus antiduplikasi. Terapkan ketentuan ini melalui lima skill yang telah disetujui dan perangkat terkait.

## 12. Verifikasi dan pengujian

Laksanakan empat tingkat pemeriksaan sesuai Bab 20.6:

1. Struktural.
2. Fungsional.
3. Substansi dan visual.
4. Persetujuan akhir Romo.

Gunakan seluruh kriteria yang relevan pada Bab 19, termasuk 18 kriteria kualitas soal, sepuluh kriteria kualitas gambar, serta sepuluh kriteria kelulusan antiduplikasi.

Periksa secara aktual berkas, data, gambar, hasil penilaian, laporan dan fungsi HTML sesuai lingkup pekerjaan.

Pengujian fungsi HTML harus dilakukan menggunakan perangkat pengujian browser yang tersedia, bukan sekadar membaca kode.

Gunakan status pemeriksaan:

- Lulus: benar-benar diperiksa dan berhasil.
- Gagal: ditemukan kekurangan.
- Belum diuji: belum diperiksa.
- Tidak berlaku: kriteria tidak relevan.

Jangan menyatakan suatu pemeriksaan Lulus berdasarkan dugaan, rencana, atau keberadaan kode.

Jangan menyembunyikan kegagalan atau keterbatasan pengujian.

Pemeriksaan otomatis tidak menggantikan verifikasi substansi pendidikan, pemeriksaan visual aktual, pengujian empiris terhadap anak, atau persetujuan Romo.

## 13. Pengelolaan repositori dan perubahan

Ikuti struktur direktori yang ditetapkan dalam Bab 20.2 serta rincian antiduplikasi Bab 19.8.7.

Setiap penugasan yang mengubah repositori menggunakan cabang kerja terpisah.

Hasil pekerjaan diajukan melalui pull request.

Lakukan pemeriksaan terhadap lingkup perubahan, versi berkas, identitas commit, dan integritas dokumen sebelum mengajukan hasil.

Jangan melakukan push langsung ke main untuk melewati prosedur persetujuan.

Jangan melakukan force push, menghapus riwayat, atau menimpa dokumen final secara sepihak.

Jangan mengubah dokumen induk tanpa keputusan yang secara eksplisit menyetujui perubahan tersebut.

Jangan melakukan merge sebelum hasil diverifikasi dan persetujuan terkait tersedia.

Gunakan perlindungan cabang dan pemeriksaan wajib apabila tersedia. Jika tidak tersedia, aturan persetujuan tetap wajib diterapkan secara prosedural.

Gunakan mekanisme autentikasi yang telah diizinkan. Jangan memperluas akses secara sepihak.

## 14. Persetujuan, register, dan progres

Gunakan mekanisme persetujuan yang ditetapkan dalam Bab 20.7.

Setiap persetujuan produksi mencantumkan:

- ID indikator.
- Tahap pekerjaan.
- Lingkup persetujuan.
- Versi berkas.
- Identitas commit yang diperiksa.
- Keputusan Romo.
- Tindakan berikutnya.

Untuk pekerjaan persiapan migrasi, catat identitas tugas dan komponen yang disetujui beserta versi berkas dan commit terkait apabila tersedia.

Pertahankan bukti persetujuan dan riwayat perubahan.

Gunakan enam status pengembangan:

1. Belum dimulai.
2. Draf.
3. Dalam verifikasi.
4. Menunggu persetujuan.
5. Disetujui, menunggu finalisasi.
6. Final.

Status Final hanya digunakan setelah hasil disetujui, disimpan, diverifikasi dan masuk cabang utama.

Apabila hasil tidak disetujui, lakukan revisi sesuai arahan tanpa menambah progres final.

Jika isi atau fungsi berubah setelah pemeriksaan, lakukan pemeriksaan kembali sebelum penggabungan.

Register wajib menggambarkan kondisi aktual, termasuk versi dan lokasi soal aktif, status pemeriksaan, bukti antiduplikasi, persetujuan dan progres.

Bedakan indikator yang rumusannya final dengan indikator yang seluruh soal dan verifikasi akhirnya telah final.

Jangan menghitung draf, usulan, data uji, atau pekerjaan yang belum difinalisasi sebagai soal final.

## 15. Keamanan, pelaporan dan batas pekerjaan

Jangan memasukkan token, kata sandi atau kredensial ke repositori, laporan maupun berkas produksi.

Jangan menggunakan data pribadi anak nyata sebagai data uji.

Jangan menggunakan repositori sebagai tempat penyimpanan hasil belajar nyata.

Jangan menetapkan desain database, akun, penyimpanan permanen hasil belajar atau laporan sebelum Komponen 7 diselesaikan dan disetujui.

Jangan menutup kesenjangan cakupan CP pada Komponen 1 secara sepihak.

Setelah menyelesaikan pekerjaan yang diizinkan, laporkan:

1. Identitas tugas dan sumber acuan.
2. Lingkup pekerjaan yang telah dilakukan.
3. Berkas dan perubahan aktual.
4. Identitas commit dan pull request apabila tersedia.
5. Hasil pemeriksaan aktual.
6. Kendala, kegagalan atau pemeriksaan yang belum dijalankan.
7. Status pekerjaan dan persetujuan yang diperlukan.
8. Titik berhenti serta tindakan berikutnya yang masih memerlukan izin.

Hentikan pekerjaan pada batas penugasan.

Jangan melanjutkan ke indikator, tahap, perubahan repositori, atau pekerjaan lain yang belum diizinkan.

---

Instruksi ini merupakan pedoman pelaksanaan operasional, bukan sumber keputusan pendidikan baru.

Seluruh ketentuan dokumen induk dan keputusan Romo yang telah disetujui tetap berlaku.
