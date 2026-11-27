# Verifikasi Produksi Diagnostik — MTK-A-K1-B.1-KM01-I01

## Identitas

- **ID indikator:** `IND-MTK-A-K1-B.1-KM01-I01`
- **Tahap:** Tahap 2 penyusunan 10 Diagnostik
- **Status hasil:** Draf — dalam verifikasi
- **Cabang:** `production/mtk-a-k1-b1-km01-diagnostik`
- **Acuan:** dokumen induk V5-salinan 61, analisis indikator final, AGENTS.md
- **Lingkup:** 10 soal Diagnostik saja; Penguatan, Pengayaan, dan Cek Ulang belum dibuat

## Berkas aktual

- JSON: `bank_soal/MTK/A/K1/MTK-A-K1-B.1-KM01-I01.json`
- HTML mandiri: `bank_soal/MTK/A/K1/MTK-A-K1-B.1-KM01-I01.html`
- Stimulus SVG: 10 berkas pada `bank_soal/MTK/A/K1/images/`
- Setiap soal memakai ID `...-DIA-01` sampai `...-DIA-10`
- Setiap soal memuat tepat 14 atribut soal sesuai standar
- Stimulus dibuat aktual dan dikaitkan satu per satu dengan ID soal

## Hasil pemeriksaan aktual

| Pemeriksaan | Status | Bukti atau batas |
|---|---|---|
| Validasi struktur JSON | **Lulus** | `scripts/json_validator.py`: valid true, errors kosong |
| Ketepatan jumlah soal | **Lulus** | Tepat 10 soal Diagnostik |
| Ketertelusuran indikator | **Lulus** | Setiap soal mengarah ke indikator dan hierarki CP–ATP–TP–KM yang sama |
| Ketepatan format ID | **Lulus** | Nomor DIA-01 sampai DIA-10 |
| Kelengkapan 14 atribut | **Lulus** | Seluruh objek soal memiliki 14 atribut |
| Stimulus aktual dan keterkaitan file | **Lulus teknis** | 10 SVG tersedia dan tampil pada HTML lokal |
| HTML mandiri lokal | **Lulus teknis** | HTML dibuka melalui file URL tanpa internet |
| Mode Pemeriksaan | **Lulus render desktop** | Hierarki, pertanyaan, stimulus, metode, dan rubrik tampil |
| Mode Pengerjaan | **Lulus render desktop** | Jenis Diagnostik, pertanyaan, stimulus, ceklis rubrik, navigasi, dan laporan tampil |
| Antiduplikasi lokal | **Lulus teknis terbatas** | Tidak ada ID conflict, exact duplicate, atau similarity candidate pada koleksi lokal satu indikator |
| Antiduplikasi global | **Belum diuji** | Koleksi pembanding global dan cabang aktif harus diperiksa sebelum finalisasi |
| Sepuluh kriteria kualitas gambar | **Belum diuji lengkap** | Tampilan telah diamati, tetapi audit visual formal belum selesai |
| Delapan belas kriteria kualitas soal | **Belum diuji lengkap** | Pemeriksaan substansi dan pedagogis formal masih terbuka |
| Respons, penyimpanan, nilai, dan laporan | **Belum diuji lengkap** | Render kontrol sudah terlihat; alur lengkap belum dinyatakan lulus |
| Uji tablet dan ponsel untuk artefak ini | **Belum diuji** | Uji Tahap 4 pada fixture sintetis tidak menggantikan uji artefak produksi |
| Uji empiris pada anak | **Belum diuji** | Tidak menggunakan data pribadi anak nyata |

## Batas keputusan

- Hasil ini **belum Final** dan belum dihitung sebagai soal final.
- Tidak ada persetujuan untuk membuat Penguatan, Pengayaan, atau Cek Ulang.
- Tidak ada perubahan CP, ATP, TP, KM, indikator, kategori, atau Komponen 1 dan Komponen 7.
- PR ini harus diperiksa sebelum penggabungan ke `main`.

## Tindakan berikutnya

1. Pemeriksaan substansi, visual formal, fungsional lengkap, dan antiduplikasi global.
2. Ajukan hasil ini kepada Romo untuk keputusan.
3. Jika disetujui dan seluruh pemeriksaan lulus, finalisasi melalui merge.
4. Baru setelah itu ajukan tahap berikutnya untuk indikator dan tahap yang diizinkan.
