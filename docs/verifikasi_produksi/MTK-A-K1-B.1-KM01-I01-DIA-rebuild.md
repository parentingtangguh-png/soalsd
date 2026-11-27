# Verifikasi Pengajuan Ulang — 10 Diagnostik

## Identitas

- **Indikator:** `IND-MTK-A-K1-B.1-KM01-I01`
- **Tahap:** Penyusunan 10 Diagnostik
- **Status:** Draf — diajukan ulang untuk pemeriksaan dan persetujuan
- **Branch:** `production/mtk-a-k1-b1-km01-diagnostik-rebuild`
- **Acuan:** dokumen induk V5-salinan 61, analisis indikator final, metode generate soal yang diperbaiki
- **Pengajuan sebelumnya:** PR #28; hasil ini dibangun ulang dan tidak menggunakan hasil soal lama sebagai dasar penerimaan

## Perubahan substantif

- Seluruh 10 pertanyaan ditulis ulang dari sudut pandang anak.
- Tidak ada ID, kode jenis soal, atau rujukan “susunan DIA nomor ...” pada teks anak.
- Setiap pertanyaan menyebut objek yang tampak dan tindakan yang harus dilakukan.
- Setiap soal memiliki stimulus SVG aktual yang disematkan ke HTML.
- HTML menampilkan label visual **Stimulus** bersama gambar.
- Setiap soal memiliki peta bukti melalui dua kriteria rubrik: pembilangan tepat satu kali dan jumlah akhir.
- Tidak ada penjelasan konsep atau penerapan nyata pada Diagnostik.
- JSON tetap menjadi sumber data tunggal.

## Ceklis sebelum pengajuan

| Pemeriksaan | Status internal | Bukti |
|---|---|---|
| 1. Selaras dengan indikator | **Lulus** | Seluruh soal meminta membilang setiap benda satu kali dan menyebutkan jumlah akhir |
| 2. Tidak melampaui kompetensi | **Lulus** | Tidak meminta operasi, perbandingan, pengurutan, atau strategi tambahan |
| 3. Bukti dapat diamati | **Lulus** | Pembilangan dan jumlah akhir dicatat melalui ceklis |
| 4. Tidak mencampurkan kompetensi lain | **Lulus** | Satu kemampuan utama dipertahankan |
| 5. Benar secara konsep | **Lulus** | Jumlah objek dan deskripsi stimulus konsisten |
| 6. Sesuai perkembangan anak | **Lulus internal** | Bahasa pendek dan tugas membilang langsung |
| 7. Bahasa jelas | **Lulus internal** | Ditelaah sebagai teks yang dibacakan orang tua |
| 8. Tidak ambigu | **Lulus internal** | Referen objek dan tindakan dinyatakan |
| 9. Pertanyaan–stimulus–jawaban konsisten | **Lulus** | 10 gambar aktual dikaitkan dengan 10 ID soal |
| 10. Sesuai fungsi Diagnostik | **Lulus** | Mengukur kemampuan awal, bukan mengajar atau menetapkan ketuntasan |
| 11. Kompleksitas relatif seragam | **Lulus internal** | Semua meminta pembilangan satu per satu; jumlah dan bentuk bervariasi |
| 12. Variasi bermakna | **Lulus internal** | Bentuk objek, jumlah, susunan, dan redaksi bervariasi |
| 13. Penjelasan/penerapan | **Lulus** | Kedua atribut bernilai null untuk Diagnostik |
| 14. Metode dan rubrik | **Lulus internal** | ORANG_TUA dengan dua kriteria objektif berbobot sama |
| 15. Panduan orang tua | **Lulus internal** | Tidak meminta perlengkapan tambahan atau bantuan substantif |
| 16. Informasi laporan | **Lulus teknis terbatas** | Respons tersimpan dan laporan menolak kelompok yang belum lengkap |
| 17. 14 atribut | **Lulus** | Validator JSON: valid true, errors kosong |
| 18. ID dan ketertelusuran | **Lulus** | ID unik DIA-01 sampai DIA-10 dan hierarki CP–ATP–TP–KM–Indikator tersedia |

## Bukti teknis aktual

- JSON: 10 soal.
- Stimulus SVG: 10 berkas.
- HTML: memuat 10 gambar SVG sebagai data URI.
- Validator JSON: **Lulus**.
- Antiduplikasi lokal: 10 record, 0 benturan ID, 0 duplikasi identik, 0 kandidat kemiripan.
- Browser aktual:
  - Mode Pemeriksaan menampilkan pertanyaan dan gambar stimulus.
  - Mode Pengerjaan menampilkan seluruh 10 soal untuk review pengajuan, masing-masing dengan pertanyaan, label Stimulus, gambar, dan rubrik.
- Mode Pengerjaan menyediakan opsi kembali ke tampilan satu per satu untuk uji interaksi.
  - Tombol Berikutnya berpindah dari soal 1 ke soal 2.
  - Setelah satu respons disimpan, laporan menampilkan `Terjawab: 1/10` dan menahan laporan lengkap sampai seluruh soal dijawab.

## Audit browser lanjutan

- HTML lokal dibuka langsung di Chrome.
- Mode Pemeriksaan menampilkan pertanyaan, label Stimulus, dan gambar aktual.
- Mode Pengerjaan menampilkan pertanyaan, label Stimulus, gambar, dua ceklis rubrik, navigasi, dan laporan.
- Setelah kembali ke tampilan satu per satu, respons pada soal pertama tersimpan; tombol Berikutnya berpindah ke soal kedua; laporan menampilkan `Terjawab: 1/10` dan `Nilai: belum lengkap`.
- Audit menemukan ambiguitas pada instruksi DIA-02 tentang urutan dua baris. Instruksi diperbaiki menjadi baris atas kiri-ke-kanan lalu baris bawah, dan JSON/HTML diperbarui serta divalidasi ulang.

## Batas

- “Lulus internal” bukan persetujuan akhir Romo.
- Antiduplikasi global tetap memperlakukan PR #28 sebagai revisi entitas yang sama, bukan koleksi soal aktif tambahan.
- Penguatan, Pengayaan, dan Cek Ulang belum dibuat.
- Hasil belum Final dan belum masuk `main`.

## Permintaan

Mohon pemeriksaan dan keputusan Romo atas hasil pengajuan ulang ini sebelum merge.
