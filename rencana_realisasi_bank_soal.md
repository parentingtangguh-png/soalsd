# Rencana Realisasi Bank Soal SD

## Status dokumen

- **Fungsi:** panduan kerja hidup menuju produksi Bank Soal SD.
- **Acuan utama:** [dokumen induk V5-salinan 61](<ringkasan_bank_soal_sd_v5-salinan 61.md>), AGENTS.md, dan keputusan Romo yang telah disetujui.
- **Tanggal pembaruan terakhir:** 27 November 2026.
- **Status keseluruhan:** Tahap Migrasi 2, Tahap 3, dan Tahap 4 telah final di `main`; Gerbang 4 disetujui dan sedang difinalkan melalui PR #14; analisis 10 indikator akan dimulai sebagai 10 penugasan terpisah; produksi soal belum dimulai.
- **Aturan pembaruan:** status hanya boleh berubah berdasarkan pekerjaan dan pemeriksaan aktual, bukan berdasarkan rencana, keberadaan kode, atau asumsi.

## Keputusan ruang lingkup

Kesenjangan cakupan CP tetap dicatat sebagai isu terbuka pada Komponen 1 dan tidak ditutup secara sepihak.

Konsekuensinya:

- Tidak ada penambahan atau perubahan TP, KM, maupun indikator tanpa persetujuan tersendiri.
- Produksi, setelah seluruh prasyarat terpenuhi, hanya mencakup indikator yang sudah final.
- Bank Soal tidak boleh dinyatakan telah mencakup seluruh CP Matematika Fase A.
- Komponen 7 tetap terbuka. Prototipe JSON/HTML boleh dibuat sesuai ketentuan, tetapi tidak boleh menetapkan penyimpanan permanen hasil belajar anak.

## Urutan gerbang realisasi

Urutan wajib:

**Ruang lingkup disahkan → repositori siap → perangkat tersedia → lingkungan lulus uji → persiapan disetujui → analisis indikator pertama → persetujuan rancangan → produksi bertahap → verifikasi 40 soal → persetujuan Romo → merge ke `main` → status Final.**

Tahap berikutnya tidak boleh dimulai sebelum gerbang sebelumnya memenuhi kriteria dan memperoleh persetujuan yang dipersyaratkan.

---

## Gerbang 0 — Ruang lingkup

### Tujuan

Menetapkan batas produksi tanpa menutup kesenjangan CP secara sepihak.

### Kriteria lulus

- Kesenjangan CP tercatat sebagai isu Komponen 1.
- Tidak ada perubahan TP, KM, atau indikator tanpa keputusan tersendiri.
- Lingkup indikator yang boleh diproduksi dapat ditelusuri ke dokumen induk aktif.

### Status aktual

**Disetujui secara kebijakan.** Romo memilih opsi bahwa kesenjangan tetap dicatat sebagai isu Komponen 1 dan tidak ditutup sepihak.

### Batas

Persetujuan ruang lingkup ini bukan persetujuan untuk langsung membuat soal. Gerbang 1–4 tetap wajib dilalui.

---

## Gerbang 1 — Repositori siap

### Tujuan

Memastikan sumber berkas, cabang, dan riwayat perubahan dapat dipertanggungjawabkan.

### Pekerjaan

- Memastikan repositori yang digunakan adalah `parentingtangguh-png/soalsd`.
- Memastikan cabang utama adalah `main`.
- Membuat atau menggunakan cabang kerja terpisah untuk setiap penugasan yang mengubah repositori.
- Memeriksa working tree dan commit dasar.
- Memastikan dokumen induk aktif adalah `ringkasan_bank_soal_sd_v5-salinan 61.md`.
- Menetapkan lokasi register progres, persetujuan, versi, dan bukti pemeriksaan.
- Memastikan tidak ada sumber aktif lain yang bertentangan dengan dokumen induk.

### Bukti yang harus tersedia

- Identitas repositori dan remote.
- Nama cabang utama dan cabang kerja.
- Identitas commit dasar.
- Hasil pemeriksaan working tree.
- Daftar berkas acuan aktif.

### Kriteria lulus

Repositori, cabang, commit dasar, working tree, dan sumber acuan telah diperiksa secara aktual dan dicatat.

### Status aktual

**Lulus dan final pada `main`.** `main` memuat AGENTS.md terbaru, dokumen induk V5 aktif, lima skill, struktur direktori, register, dan catatan persetujuan melalui PR #7 (merge `14e156a`) serta PR #8 (merge `69d3418`).

### Tindakan berikutnya

Pembangunan perangkat Tahap Migrasi 3 sedang berjalan pada branch terpisah; selesaikan verifikasi dan ajukan persetujuan sebelum Tahap 4.

---

## Gerbang 2 — Perangkat tersedia

### Tujuan

Menyediakan delapan perangkat produksi yang dapat digunakan dan diuji. Tahap ini menjadi pekerjaan berikutnya setelah Tahap 2 final.

### Perangkat wajib

1. Ekstraktor kompetensi.
2. Generator identitas soal.
3. Validator JSON.
4. Perangkat pembuatan gambar.
5. Generator HTML.
6. Perangkat pengujian.
7. Pengelola register.
8. Detektor antiduplikasi soal.

### Urutan pembangunan yang disarankan

1. Ekstraktor kompetensi.
2. Generator identitas.
3. Validator JSON.
4. Pengelola register.
5. Perangkat pembuatan gambar.
6. Generator HTML.
7. Perangkat pengujian.
8. Detektor antiduplikasi.

Urutan ini dapat disesuaikan secara teknis jika ketergantungan dan dampaknya dicatat tanpa mengubah standar pendidikan.

### Syarat setiap perangkat

- Fungsi dan batas kewenangan terdokumentasi.
- Berkas implementasi tersedia.
- Data uji teknis tersedia.
- Hasil pengujian dicatat.
- Versi perangkat dapat ditelusuri.
- Kegagalan dan keterbatasan tidak disembunyikan.

### Kriteria lulus

Delapan perangkat tersedia, dapat dijalankan, dan hasil pengujian awalnya terdokumentasi. Keberadaan kode saja tidak cukup untuk menyatakan lulus.

### Status aktual

**Final.** Romo menyetujui PR #9 berdasarkan commit yang diperiksa `81acc59`; PR #9 masuk `main` melalui merge `5d01801`, dan statusnya difinalkan melalui PR #10 (merge `9e5973b`). Delapan perangkat, fixture sintetis, suite unit, dan uji CLI tersedia; suite teknis lulus 7 uji. Verifikasi integrasi, browser, visual aktual, dan dua belas kelompok uji antiduplikasi menjadi pekerjaan Tahap 4.

### Tindakan berikutnya

Siapkan pengajuan dan verifikasi lingkungan Tahap Migrasi 4 dengan data uji sintetis. Produksi soal tetap belum boleh dimulai sebelum lingkungan lulus uji dan persiapan produksi disetujui.

---

## Gerbang 3 — Lingkungan lulus uji

### Tujuan

Memastikan seluruh perangkat terintegrasi dan dapat digunakan untuk produksi secara aman.

### Data uji

- Hanya menggunakan data sintetis.
- Tidak menggunakan data pribadi anak nyata.
- Tidak memasukkan data uji ke koleksi soal final.
- Tidak menghitung data uji sebagai progres produksi.

### Pemeriksaan wajib

- Struktur JSON dan tepat 14 atribut soal.
- Generator identitas dan ketepatan format ID.
- Aturan atribut bersyarat.
- Pembuatan serta pemeriksaan gambar aktual.
- Generator HTML mandiri.
- Mode Pemeriksaan Bank Soal.
- Mode Pengerjaan Soal Interaktif.
- Penilaian otomatis dan ceklis orang tua.
- Nilai, ketuntasan, percabangan, dan laporan.
- Pengelolaan register.
- Integrasi antarperangkat.
- Dua belas kelompok pengujian antiduplikasi.

### Status pemeriksaan

Setiap pemeriksaan harus diberi salah satu status berikut:

- **Lulus** — benar-benar diperiksa dan berhasil.
- **Gagal** — ditemukan kekurangan.
- **Belum diuji** — belum diperiksa.
- **Tidak berlaku** — tidak relevan dengan lingkup pemeriksaan.

### Kriteria lulus

Seluruh pemeriksaan wajib selesai, tidak ada kegagalan yang belum ditangani, dan bukti pengujian dapat ditelusuri.

### Status aktual

**Final di `main`.** Pemeriksaan sintetis struktural, integrasi perangkat, HTML offline, stimulus SVG, hierarki, register, dan dua belas kelompok kasus antiduplikasi teknis telah dijalankan. Browser desktop, ponsel, dan tablet lulus untuk Mode Pemeriksaan, Mode Pengerjaan, respons otomatis, ceklis orang tua, laporan, percabangan, dan ketuntasan. Pemeriksaan pedagogis dan empiris belum dilakukan pada fixture sintetis dan tetap wajib pada indikator produksi.

### Tindakan berikutnya

Romo telah menyetujui pengajuan Tahap 4 dan PR #12 telah masuk `main`. Siapkan Gerbang 4 dan tunggu persetujuan sebelum analisis indikator atau produksi soal dimulai.

---

## Gerbang 4 — Persiapan produksi disetujui

### Tujuan

Mendapatkan persetujuan formal untuk membuka produksi indikator.

### Isi pengajuan persetujuan

- ID tugas.
- Lingkup indikator.
- Tahap pekerjaan yang diminta.
- Versi dokumen induk.
- Versi perangkat.
- Identitas commit yang diperiksa.
- Hasil Gerbang 1–3.
- Status Komponen 1 dan Komponen 7.
- Keputusan Romo.
- Tindakan berikutnya.

### Kriteria lulus

Romo menyetujui persiapan produksi berdasarkan bukti aktual Gerbang 1–3.

### Status aktual

**Disetujui, menunggu finalisasi.** Pengajuan `MIG-G4-PERSIAPAN-10-INDIKATOR` disetujui Romo; setelah PR #14 masuk `main`, analisis 10 indikator dimulai sebagai 10 penugasan terpisah. Belum ada permintaan untuk membuat soal produksi.

### Batas

Persetujuan ini membuka pekerjaan produksi, tetapi belum menyetujui isi soal tertentu.

---

## Gerbang 5 — Analisis indikator pertama

### Indikator awal

`IND-MTK-A-K1-B.1-KM01-I01` — Membilang benda satu per satu dalam suatu kumpulan.

### Tujuan

Menyusun dan memeriksa rancangan empat jenis soal sebelum membuat butir soal.

### Isi rancangan

- Kemampuan utama dan pendukung.
- Bukti penguasaan.
- Kategori kecakapan berpikir.
- Batas cakupan.
- Stimulus.
- Bentuk respons.
- Metode penilaian.
- Rubrik.
- Rancangan Diagnostik, Penguatan, Pengayaan, dan Cek Ulang.
- Variasi yang sah.
- Strategi antiduplikasi.
- Kebutuhan gambar dan spesifikasinya.
- Rancangan nilai dan laporan.

### Kriteria lulus

- Indikator dan kategori telah disetujui.
- Bukti penguasaan dan batas cakupan jelas.
- Metode, respons, rubrik, stimulus, dan gambar layak.
- Tidak ada batas numerik atau keputusan khusus yang ditetapkan sepihak.
- Rancangan empat jenis soal telah diperiksa dan disetujui.

### Status aktual

**Belum dimulai.**

### Batas

Gerbang ini hanya menghasilkan analisis dan rancangan. Belum boleh menghasilkan 40 soal.

---

## Gerbang 6 — Produksi bertahap per indikator

### Prinsip

- Satu penugasan hanya mencakup satu indikator dan satu tahap.
- Setiap kelompok berisi tepat 10 soal.
- Setiap tahap memerlukan pemeriksaan dan persetujuan sebelum tahap berikutnya.
- Draf tidak dihitung sebagai soal final.
- JSON tetap menjadi sumber data tunggal.
- HTML dihasilkan dari JSON dan gambar terkait.

### Enam tahap

1. Analisis dan rancangan empat jenis soal.
2. Penyusunan 10 Diagnostik.
3. Penyusunan 10 Penguatan.
4. Penyusunan 10 Pengayaan.
5. Penyusunan 10 Cek Ulang.
6. Verifikasi akhir seluruh 40 soal.

### Pemeriksaan setiap kelompok

- 14 atribut tersedia dan sesuai aturan bersyarat.
- Kompetensi dan kategori tetap sama.
- Kompleksitas kelompok relatif seragam.
- Cek Ulang lebih kompleks daripada Diagnostik.
- Penjelasan konsep dan penerapan nyata tersedia pada Penguatan dan Pengayaan.
- Panduan orang tua tersedia.
- Stimulus dan gambar sesuai kebutuhan.
- Metode, kunci, atau rubrik sesuai bukti penguasaan.
- 18 kriteria kualitas soal diperiksa.
- Antiduplikasi diperiksa pada titik yang relevan.

### Status aktual

**Belum dimulai.** Gerbang ini baru dibuka setelah Gerbang 4 dan Gerbang 5 lulus.

---

## Gerbang 7 — Finalisasi indikator

### Kriteria final

Satu indikator hanya boleh berstatus **Final** jika:

- 40 soal tersedia dan lengkap.
- JSON lengkap dan valid.
- Gambar aktual telah dibuat dan diverifikasi jika diperlukan.
- HTML dihasilkan dari JSON.
- Kedua mode HTML telah diuji menggunakan perangkat pengujian browser.
- 18 kriteria kualitas soal terpenuhi.
- 10 kriteria kelulusan antiduplikasi terpenuhi secara bersamaan.
- Koleksi pembanding global lengkap.
- Seluruh kandidat kemiripan telah diselesaikan.
- Bukti pemeriksaan lengkap dan dapat ditelusuri.
- Register telah diperbarui.
- Hasil telah diverifikasi secara struktural, fungsional, substansial, dan visual.
- Romo telah memberikan persetujuan akhir.
- Perubahan telah masuk ke `main` melalui prosedur cabang dan pull request yang sah.

### Status aktual

**Belum dimulai.**

### Batas

Kelulusan antiduplikasi saja tidak menjadikan soal Final. Persetujuan Romo, pemeriksaan kualitas lain, dan penggabungan ke `main` tetap wajib.

---

## Aturan penghentian sementara

Pekerjaan harus dihentikan pada bagian yang terdampak apabila:

- repositori atau cabang tidak dapat diverifikasi;
- perangkat wajib belum tersedia;
- lingkungan belum lulus uji;
- kategori atau batas kompetensi belum jelas;
- diperlukan keputusan pendidikan baru;
- koleksi pembanding antiduplikasi belum lengkap;
- terdapat benturan ID;
- terdapat duplikasi yang terbukti;
- kandidat kemiripan belum diselesaikan;
- bukti pemeriksaan belum lengkap;
- isi atau fungsi berubah setelah pemeriksaan;
- persetujuan tahap sebelumnya belum tersedia.

## Aturan pembaruan dokumen ini

Setiap pembaruan wajib mencantumkan:

- tanggal pembaruan;
- gerbang yang terdampak;
- pekerjaan nyata yang dilakukan;
- berkas yang berubah;
- status pemeriksaan aktual;
- bukti atau lokasi laporan;
- identitas commit dan pull request jika tersedia;
- keputusan Romo jika diperlukan;
- kendala;
- tindakan berikutnya.

Status tidak boleh diubah menjadi **Lulus**, **Disetujui**, atau **Final** hanya karena pekerjaan direncanakan atau kode telah dibuat.

Jika perubahan memengaruhi soal, gambar, metode, rubrik, HTML, JSON, koleksi pembanding, atau validitas pemeriksaan, pemeriksaan yang terdampak harus diulang.

## Log pembaruan

| Tanggal | Gerbang | Perubahan nyata | Bukti | Status |
|---|---|---|---|---|
| 27 November 2026 | Gerbang 0 | Ruang lingkup ditetapkan: kesenjangan CP tetap terbuka pada Komponen 1 dan tidak ditutup sepihak. | Keputusan Romo dalam percakapan; perlu dicatat pada register formal saat register tersedia. | Disetujui secara kebijakan |
| 27 November 2026 | Gerbang 1 | Checkout repositori remote dibuat di folder terpisah tanpa menimpa workspace lama. Remote, branch dasar, commit, dan working tree diverifikasi. | `soalsd-repo`, remote GitHub, branch `main`, commit `13dbb56172cc965c37f250cd67856bdf628d716c`. | Lulus pada checkout kerja |
| 27 November 2026 | Gerbang 1 | Cabang kerja dibuat dan acuan V5-salinan 61, AGENTS.md terbaru, serta panduan realisasi disiapkan pada cabang kerja. Dokumen V4 historis tidak dihapus. | Branch `setup/tahap-2-persiapan`; hash salinan diverifikasi sama dengan sumber lokal. | Dalam verifikasi sebelum persetujuan |
| 27 November 2026 | Gerbang 2 | Tiga skill tambahan dibuat, dua skill lama dibaca dan rujukan V5 diperbarui, struktur register/persetujuan/antiduplikasi disiapkan. | `.agents/skills/`; `docs/register_bank_soal.md`; `docs/catatan_persetujuan.md`; `docs/struktur_direktori.md`; `docs/antiduplikasi/`. | Dalam verifikasi |
| 27 November 2026 | Gerbang 2 | Artefak persiapan dicatat dalam commit draft. Validasi struktur kelima skill lulus. Pemeriksaan `git diff --check` menemukan tiga trailing whitespace pada rumusan V5 yang disalin verbatim; tidak diubah sepihak. | Commit `0816f76`; hasil validator skill-creator: kelima skill valid. | Dalam verifikasi; temuan format tercatat |
| 27 November 2026 | Gerbang 2 | Register dan panduan progres diperbarui untuk mencatat commit serta status verifikasi. | Commit `7eee7ad`. | Dalam verifikasi; menunggu persetujuan Tahap 2 |
| 27 November 2026 | Gerbang 2 | Pengajuan formal Tahap Migrasi 2 dibuat, status register diubah menjadi Menunggu persetujuan, dan pull request dibuka. | `docs/pengajuan_MIG-T2-PERSIAPAN.md`; PR `#7`; commit pengajuan `25b95d1`. | Menunggu persetujuan Romo |
| 27 November 2026 | Gerbang 2 | Persetujuan Romo diterima dan PR #7 difinalkan ke `main` berdasarkan commit `1811052`. | Catatan persetujuan `1c28b3e`; PR `#7`; merge commit `14e156a`. | Final |
| 27 November 2026 | Tahap 3 / Gerbang 2 | Persetujuan Romo diterima dan Tahap 3 difinalkan ke `main`. Suite teknis lulus 7 uji; belum ada perubahan soal atau produksi. | Catatan persetujuan; PR `#9`; merge commit `5d01801`; finalisasi PR `#10` merge `9e5973b`. | Final |
| 27 November 2026 | Tahap 4 / Gerbang 3 | Verifikasi sintetis struktural dan fungsional dijalankan; browser desktop menampilkan stimulus/hierarki dan menguji alur penilaian; dua belas kelompok kasus antiduplikasi teknis dijalankan. | `docs/verifikasi_tahap4.md`; `scripts/stage4_verify.py`; artefak uji lokal; bukti sesi browser; PR #12 (ready for review), head awal `2c221aaa80e88dd83d6ed6dae95429acaec4d7c3`. | Dalam verifikasi; uji tablet/ponsel dan pemeriksaan pedagogis masih terbuka |
| 27 November 2026 | Tahap 4 / Gerbang 3 | Atas keputusan Romo, uji tablet/ponsel tetap dicatat Belum diuji dan hasil Tahap 4 dilanjutkan sebagai pengajuan formal. | `docs/pengajuan_MIG-T4-VERIFIKASI.md`; PR #12; keputusan Romo dalam percakapan. | Menunggu persetujuan |
| 27 November 2026 | Tahap 4 / Gerbang 3 | Uji responsif aktual dijalankan pada viewport ponsel dan tablet. Hierarki, stimulus, pilihan jawaban, dan Mode Pengerjaan tampil tanpa horizontal overflow; console bersih. | Browser Chrome; override 390×844 dan 768×1024; bukti sesi browser; PR #12. | Menunggu persetujuan; pemeriksaan pedagogis/substansi/empiris masih terbuka |
| 27 November 2026 | Tahap 4 / Gerbang 3 | Romo menyetujui pengajuan Tahap 4 untuk difinalkan; lingkungan teknis sintetis akan berstatus Final setelah PR #12 masuk `main`. | Keputusan Romo; `docs/pengajuan_MIG-T4-VERIFIKASI.md`; PR #12. | Disetujui, menunggu finalisasi |
| 27 November 2026 | Tahap 4 / Gerbang 3 | PR #12 berhasil di-merge; lingkungan verifikasi teknis sintetis difinalkan di `main`. | PR #12; merge `1560fbdf17df82d942c1bf974a4e8d890427e639`. | Final |
| 27 November 2026 | Gerbang 4 | Pengajuan persiapan produksi untuk memulai analisis 10 indikator disetujui; setiap indikator tetap memiliki penugasan dan status terpisah; produksi soal belum diminta. | `docs/pengajuan_MIG-G4-PERSIAPAN-10-INDIKATOR.md`; PR #14; keputusan Romo. | Disetujui, menunggu finalisasi |

## Rujukan dokumen induk

- Bab 19.1–19.2: identitas dan atribut soal.
- Bab 19.3: kriteria kualitas soal.
- Bab 19.4: enam tahap penyusunan dan persetujuan soal.
- Bab 19.5: JSON dan HTML.
- Bab 19.6: gambar.
- Bab 19.8: antiduplikasi.
- Bab 20.4: delapan perangkat produksi.
- Bab 20.6: empat tingkat pemeriksaan.
- Bab 20.7: persetujuan dan register.
- Bab 20.8: lima tahap migrasi.

