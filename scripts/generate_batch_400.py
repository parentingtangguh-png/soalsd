"""Generate the approved 10-indicator MTK Fase A batch: 400 questions."""

from __future__ import annotations

import json
import re
from pathlib import Path
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "bank_soal" / "MTK" / "A" / "K1"
IMG = OUT / "images"

CP = "CP-MTK-A-1.1 — Bilangan cacah sampai 100; nilai tempat; perbandingan dan pengurutan; komposisi/dekomposisi; penjumlahan dan pengurangan sampai 20; setengah dan seperempat."

INDICATORS = [
    {
        "id": "IND-MTK-A-K1-B.1-KM01-I01", "tp": "B.1 — Membilang, subitasi, dan membandingkan jumlah benda.",
        "km": "KM-MTK-A-K1-B.1-01 — Menentukan banyak benda dalam suatu kumpulan dengan membilang satu per satu secara tepat.",
        "atp": "Kelas 1, ATP 1", "cat": "I",
        "text": "Menentukan banyak benda dalam satu kumpulan yang ditampilkan melalui gambar dengan membilang setiap benda tepat satu kali dan menyebutkan jumlah akhirnya secara benar.",
        "kind": "count",
    },
    {
        "id": "IND-MTK-A-K1-B.1-KM02-I01", "tp": "B.1 — Membilang, subitasi, dan membandingkan jumlah benda.",
        "km": "KM-MTK-A-K1-B.1-02 — Menentukan banyak benda dalam kumpulan kecil secara langsung tanpa menghitung satu per satu (subitasi).",
        "atp": "Kelas 1, ATP 1", "cat": "I",
        "text": "Menentukan banyak benda dalam satu kumpulan kecil yang ditampilkan melalui gambar secara langsung tanpa menghitung benda satu per satu, serta menyatakan jumlahnya dengan tepat.",
        "kind": "subitize",
    },
    {
        "id": "IND-MTK-A-K1-B.1-KM03-I01", "tp": "B.1 — Membilang, subitasi, dan membandingkan jumlah benda.",
        "km": "KM-MTK-A-K1-B.1-03 — Membandingkan dua kumpulan benda dan menyatakan sama banyak, lebih banyak, atau lebih sedikit.",
        "atp": "Kelas 1, ATP 1", "cat": "II",
        "text": "Membandingkan banyak benda dalam dua kumpulan yang ditampilkan melalui gambar, kemudian menentukan dan menyatakan hubungan jumlah kedua kumpulan secara tepat menggunakan istilah sama banyak, lebih banyak, atau lebih sedikit.",
        "kind": "compare",
    },
    {
        "id": "IND-MTK-A-K1-B.3-KM01-I01", "tp": "B.3 — Urutan, komposisi, dekomposisi, dan nilai tempat sampai 20.",
        "km": "KM-MTK-A-K1-B.3-01 — Mengurutkan bilangan cacah sampai 20 secara maju (dari kecil ke besar) dan mundur (dari besar ke kecil).",
        "atp": "Kelas 1, ATP 2", "cat": "II",
        "text": "Mengurutkan sejumlah bilangan cacah sampai 20 yang disajikan secara acak menjadi urutan dari bilangan terkecil ke terbesar atau dari bilangan terbesar ke terkecil secara tepat.",
        "kind": "order",
    },
    {
        "id": "IND-MTK-A-K1-B.3-KM02-I01", "tp": "B.3 — Urutan, komposisi, dekomposisi, dan nilai tempat sampai 20.",
        "km": "KM-MTK-A-K1-B.3-02 — Menentukan bilangan cacah sampai 20 yang terbentuk dari penggabungan bagian-bagian bilangan.",
        "atp": "Kelas 1, ATP 2", "cat": "II",
        "text": "Menentukan bilangan cacah sampai 20 yang terbentuk dari penggabungan bagian-bagian bilangan yang disajikan melalui gambar atau lambang bilangan, kemudian menyatakan bilangan keseluruhannya secara tepat.",
        "kind": "compose",
    },
    {
        "id": "IND-MTK-A-K1-B.3-KM03-I01", "tp": "B.3 — Urutan, komposisi, dekomposisi, dan nilai tempat sampai 20.",
        "km": "KM-MTK-A-K1-B.3-03 — Menguraikan bilangan cacah sampai 20 menjadi bagian-bagian bilangan yang membentuknya.",
        "atp": "Kelas 1, ATP 2", "cat": "II",
        "text": "Menguraikan bilangan cacah sampai 20 yang disajikan melalui gambar atau lambang bilangan menjadi bagian-bagian bilangan yang membentuknya, kemudian menyatakan hasil penguraian secara tepat.",
        "kind": "decompose",
    },
    {
        "id": "IND-MTK-A-K1-B.3-KM04-I01", "tp": "B.3 — Urutan, komposisi, dekomposisi, dan nilai tempat sampai 20.",
        "km": "KM-MTK-A-K1-B.3-04 — Mengidentifikasi nilai tempat puluhan dan satuan pada bilangan cacah sampai 20.",
        "atp": "Kelas 1, ATP 2", "cat": "II",
        "text": "Mengidentifikasi angka pada tempat puluhan dan satuan dalam bilangan cacah sampai 20 yang disajikan melalui lambang bilangan atau gambar, kemudian menentukan nilai yang diwakili setiap angka berdasarkan posisi tempatnya secara tepat.",
        "kind": "place",
    },
    {
        "id": "IND-MTK-A-K1-B.2-KM01-I01", "tp": "B.2 — Membaca dan menulis bilangan sampai 20.",
        "km": "KM-MTK-A-K1-B.2-01 — Mengenali lambang bilangan cacah sampai 20 dan menyebutkan nama bilangannya secara tepat.",
        "atp": "Kelas 1, ATP 3", "cat": "I",
        "text": "Mengenali lambang bilangan cacah sampai 20 yang disajikan secara tertulis, kemudian menyebutkan nama bilangan yang sesuai dengan lambang tersebut secara tepat.",
        "kind": "read",
    },
    {
        "id": "IND-MTK-A-K1-B.2-KM02-I01", "tp": "B.2 — Membaca dan menulis bilangan sampai 20.",
        "km": "KM-MTK-A-K1-B.2-02 — Menuliskan lambang bilangan cacah sampai 20 berdasarkan nama bilangan yang diberikan.",
        "atp": "Kelas 1, ATP 3", "cat": "I",
        "text": "Menuliskan lambang bilangan cacah sampai 20 yang sesuai dengan nama bilangan yang diberikan melalui sistem secara tepat.",
        "kind": "write",
    },
    {
        "id": "IND-MTK-A-K1-B.2-KM03-I01", "tp": "B.2 — Membaca dan menulis bilangan sampai 20.",
        "km": "KM-MTK-A-K1-B.2-03 — Memadankan lambang bilangan cacah sampai 20 dengan banyak benda melalui korespondensi satu-satu.",
        "atp": "Kelas 1, ATP 3", "cat": "I",
        "text": "Memadankan lambang bilangan cacah sampai 20 dengan kumpulan benda yang ditampilkan melalui gambar berdasarkan korespondensi satu-satu, kemudian menentukan kecocokan antara lambang bilangan dan banyak benda secara tepat.",
        "kind": "match",
    },
]

COUNTS = [4, 6, 5, 7, 8, 3, 9, 10, 12, 14]
PAIRS = [(3, 5), (6, 6), (7, 4), (4, 8), (9, 9), (2, 6), (8, 5), (5, 7), (10, 10), (6, 9)]
NUMBERS = [(2, 5, 9), (11, 4, 7), (6, 13, 2), (15, 8, 3), (1, 12, 7), (18, 5, 10), (9, 16, 4), (20, 11, 6), (14, 2, 19), (7, 17, 13)]
PARTS = [(2, 3), (4, 3), (5, 2), (6, 3), (7, 4), (8, 2), (9, 5), (10, 4), (6, 7), (11, 5)]
TOTALS = [5, 7, 7, 9, 11, 10, 14, 14, 13, 16]
NAMES = [("tiga", 3), ("lima", 5), ("tujuh", 7), ("sembilan", 9), ("sebelas", 11), ("dua belas", 12), ("empat belas", 14), ("enam belas", 16), ("delapan belas", 18), ("dua puluh", 20)]


def rubrics(kind: str):
    if kind in {"count", "subitize"}:
        return [{"kriteria": "Anak memberikan respons sesuai tuntutan proses yang diamati.", "bobot": 1}, {"kriteria": "Anak menyatakan jumlah akhir dengan tepat.", "bobot": 1}]
    return [{"kriteria": "Anak memberikan respons yang sesuai dengan hubungan atau nilai yang diminta.", "bobot": 1}]


def svg_for(kind: str, data: dict) -> str:
    if kind in {"count", "subitize", "match"}:
        n = data["n"]
        shape = data.get("shape", "lingkaran")
        cols = min(n, 10)
        rows = (n + cols - 1) // cols
        shapes = []
        for i in range(n):
            x = 30 + (i % cols) * 48
            y = 30 + (i // cols) * 48
            if shape == "persegi":
                shapes.append(f'<rect x="{x - 14}" y="{y - 14}" width="28" height="28" fill="#2563eb"/>')
            else:
                shapes.append(f'<circle cx="{x}" cy="{y}" r="14" fill="#2563eb"/>')
        w, h = 60 + cols * 48, 60 + rows * 48
        return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img">{"".join(shapes)}</svg>\n'
    if kind == "compare":
        a, b = data["a"], data["b"]
        def group(x0, n, color):
            return ''.join(f'<circle cx="{x0 + (i % 5)*28}" cy="{35 + (i//5)*28}" r="9" fill="{color}"/>' for i in range(n))
        h = 70 + 28 * max((a + 4)//5, (b + 4)//5)
        return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 330 {h}" role="img"><rect x="5" y="5" width="150" height="{h-10}" fill="#eff6ff" stroke="#2563eb"/><rect x="175" y="5" width="150" height="{h-10}" fill="#f0fdf4" stroke="#16a34a"/>{group(25,a,"#2563eb")}{group(195,b,"#16a34a")}</svg>\n'
    return ""


def base_question(meta, typ, no, question, method, *, choice=None, key=None, image=None, guide=None, concept=None, application=None, rubric=None):
    qid = f"SOAL-MTK-A-K1-{meta['id'].split('-K1-')[1]}-{typ}-{no:02d}"
    return {
        "id_soal": qid,
        "id_indikator": meta["id"],
        "jenis_soal": typ,
        "pertanyaan": question,
        "pilihan": choice,
        "kunci_jawaban": key,
        "panduan_orang_tua": guide or "Bacakan pertanyaan sesuai teks. Biarkan anak merespons sendiri dan catat responsnya tanpa memberi jawaban atau strategi tambahan.",
        "penjelasan_konsep": concept,
        "penerapan_nyata": application,
        "butuh_gambar": bool(image),
        "image_description": image["desc"] if image else None,
        "image_spec": "2D" if image else None,
        "metode_penilaian": method,
        "rubrik_penilaian": rubric if method == "ORANG_TUA" else None,
    }


def automatic_choices(correct, distractors, labels=("A", "B", "C"), *, answer_position=0):
    """Return exactly three distinct choices and rotate the correct label."""
    vals = [str(correct)]
    for value in distractors:
        text = str(value)
        if text not in vals:
            vals.append(text)
        if len(vals) == 3:
            break
    if len(vals) < 3:
        raise ValueError(f"Tidak tersedia tiga pilihan berbeda untuk {correct!r}: {distractors!r}")
    answer_position %= 3
    vals[0], vals[answer_position] = vals[answer_position], vals[0]
    return {labels[i]: vals[i] for i in range(3)}, labels[answer_position]


QUESTION_VARIANTS = {
    "count": {
        "DIA": [
            "Berapa banyak {shape} yang tampak pada gambar? Hitung setiap benda satu kali.",
            "Hitung kumpulan {shape} pada stimulus. Berapa jumlah akhirnya?",
            "Tunjuk {shape} satu per satu sambil membilang, lalu sebutkan hasilnya.",
            "Perhatikan gambar. Ada berapa {shape} seluruhnya?",
            "Berapakah banyak {shape} dalam kumpulan ini setelah kamu menghitungnya?",
            "Hitung dari kiri ke kanan tanpa melewatkan {shape}. Berapa hasilnya?",
            "Gunakan satu bilangan untuk setiap {shape}. Berapa jumlah benda pada gambar?",
            "Setelah semua {shape} dihitung, bilangan apa yang kamu sebutkan terakhir?",
            "Cermati stimulus dan hitung seluruh {shape}. Berapa banyak semuanya?",
            "Berapa jumlah {shape} pada susunan ini? Pastikan tidak ada yang dihitung dua kali.",
        ],
        "PGT": [
            "Tunjuk setiap {shape} sambil mengucapkan bilangan berurutan. Berapa banyak semuanya?",
            "Gunakan cara membilang satu-satu pada kumpulan {shape}, lalu sampaikan jumlah akhirnya.",
            "Telusuri {shape} dari kiri ke kanan. Bilangan terakhir yang kamu ucapkan menunjukkan berapa benda?",
            "Hitung dengan memasangkan satu bilangan pada satu {shape}. Berapa hasil penghitunganmu?",
            "Peragakan cara menghitung seluruh {shape} tanpa mengulang benda. Berapa jumlahnya?",
            "Bilanglah setiap {shape} tepat satu kali, kemudian nyatakan jumlah kumpulan itu.",
            "Gunakan jari untuk menunjuk {shape} satu per satu. Berapa jumlah benda yang ditemukan?",
            "Hitung perlahan kumpulan {shape}. Apa bilangan terakhir dan apa arti bilangan itu?",
            "Tunjukkan bahwa setiap {shape} sudah mendapat satu hitungan. Berapa jumlah akhirnya?",
            "Dengan strategi membilang satu-satu, tentukan banyak {shape} pada gambar ini.",
        ],
        "PYN": [
            "Bayangkan kamu sedang menata {shape} untuk dibagikan. Hitung semuanya dan sebutkan jumlahnya.",
            "Seorang teman ingin memastikan jumlah {shape}. Tunjukkan cara menghitungnya dan berikan hasil akhir.",
            "Jika setiap {shape} akan diberi satu label, berapa label yang kamu perlukan?",
            "Periksa kembali kumpulan {shape} dengan membilang satu per satu. Berapa banyak yang kamu temukan?",
            "Gunakan susunan pada gambar untuk menentukan jumlah {shape} tanpa menghitung benda yang sama dua kali.",
            "Kamu hendak memasukkan semua {shape} ke dalam kotak. Berapa benda yang harus masuk?",
            "Jelaskan melalui tindakan menunjuk bagaimana kamu mengetahui jumlah {shape}, lalu sebutkan hasilnya.",
            "Jika satu {shape} diambil setelah semua dihitung, berapa jumlah yang semula ada?",
            "Hitung kumpulan {shape} dan cocokkan hasilnya dengan bilangan terakhir yang kamu ucapkan.",
            "Tentukan banyak {shape} pada stimulus untuk menyiapkan jumlah benda yang sama.",
        ],
        "CU": [
            "Sebagai cek ulang, hitung kembali {shape} pada gambar. Berapa jumlah yang kamu peroleh?",
            "Periksa ketepatan hitunganmu dengan menunjuk setiap {shape} sekali lagi. Berapa hasilnya?",
            "Lakukan penghitungan ulang dari awal pada kumpulan {shape}. Berapa banyak semuanya?",
            "Cek susunan {shape} satu per satu. Bilangan terakhir yang kamu sebutkan berapa?",
            "Pastikan tidak ada {shape} yang terlewat atau terhitung dua kali. Berapa jumlahnya?",
            "Ulangi proses membilang pada stimulus {shape}. Berapa hasil pemeriksaanmu?",
            "Gunakan cara membilang yang sama untuk memeriksa jumlah {shape}. Apa jawabannya?",
            "Hitung kembali dengan tertib dari kiri ke kanan. Berapa {shape} yang terlihat?",
            "Verifikasi jumlah {shape} dengan satu bilangan untuk satu benda. Berapa hasil akhir?",
            "Setelah memeriksa semua {shape}, nyatakan jumlah seluruh benda secara tepat.",
        ],
    },
    "subitize": {
        "DIA": [
            "Lihat sekilas kumpulan titik pada gambar. Berapa banyak titik yang kamu kenali?",
            "Tanpa membilang satu per satu, sebutkan jumlah titik biru yang tampak.",
            "Perhatikan susunan titik sebentar. Berapa jumlahnya?",
            "Kenali banyak titik pada stimulus secara langsung, lalu ucapkan bilangannya.",
            "Ada berapa titik biru pada kumpulan kecil ini jika kamu melihatnya sekaligus?",
            "Sebutkan jumlah titik yang kamu lihat tanpa menunjuk setiap titik.",
            "Amati pola titik. Bilangan apa yang menyatakan banyak titik itu?",
            "Berapa titik yang tampak dalam satu pandangan pada gambar ini?",
            "Nyatakan banyak titik berdasarkan pengenalan langsung terhadap susunannya.",
            "Lihat kumpulan kecil ini dan jawab jumlahnya tanpa hitungan satu-satu.",
        ],
        "PGT": [
            "Kenali susunan titik secara langsung tanpa menyentuhnya satu per satu. Berapa banyak titik itu?",
            "Gunakan penglihatan untuk mengenali pola titik sekaligus. Bilangan berapa yang kamu lihat?",
            "Perhatikan kelompok titik biru dan sebutkan jumlahnya tanpa membilang satu-satu.",
            "Tunjukkan bahwa kamu mengenali jumlah titik dari polanya, bukan dari hitungan berurutan.",
            "Lihat stimulus sebentar. Berapa titik yang dapat kamu kenali sekaligus?",
            "Amati kumpulan kecil itu sebagai satu pola. Berapa banyak titiknya?",
            "Sebutkan jumlah titik berdasarkan pandangan langsung terhadap seluruh susunan.",
            "Tanpa menunjuk, kenali jumlah benda dari pola titik biru. Apa bilangannya?",
            "Gunakan subitasi untuk menentukan banyak titik pada gambar. Berapa jawabannya?",
            "Perhatikan susunan titik dan nyatakan jumlah yang langsung kamu kenali.",
        ],
        "PYN": [
            "Kamu melihat titik-titik ini sekilas sebelum bermain. Berapa banyak yang langsung kamu kenali?",
            "Jika pola titik muncul di kartu permainan, berapa jumlah yang dapat kamu sebutkan tanpa menghitung?",
            "Gunakan pengenalan cepat terhadap susunan titik untuk menentukan bilangannya.",
            "Seorang teman menutup gambar segera. Sebelum tertutup, berapa titik yang kamu kenali?",
            "Tentukan banyak titik dari pola keseluruhan, bukan dengan menunjuknya satu per satu.",
            "Bayangkan susunan ini sebagai pola pada dadu. Berapa jumlah titik yang terlihat?",
            "Kenali jumlah pada kelompok kecil ini lalu jelaskan bilangan yang kamu sebutkan.",
            "Perhatikan bentuk susunan titik untuk menemukan jumlahnya secara langsung.",
            "Tanpa menghitung berurutan, tentukan banyak titik yang diperlukan untuk membuat pola ini.",
            "Gunakan kemampuan mengenali jumlah kecil seketika. Berapa titik pada stimulus?",
        ],
        "CU": [
            "Cek ulang dengan melihat susunan titik tanpa membilang satu-satu. Berapa jumlah yang kamu kenali?",
            "Periksa jawabanmu dengan mengamati pola titik secara langsung. Berapa bilangannya?",
            "Lihat kembali kumpulan kecil itu dan sebutkan jumlah tanpa menunjuk titik satu per satu.",
            "Pastikan kamu mengenali pola seluruh titik sekaligus. Berapa banyak titiknya?",
            "Ulangi pengenalan langsung terhadap susunan biru. Apa jumlah yang tampak?",
            "Verifikasi jumlah dengan melihat pola, bukan dengan urutan hitungan. Berapa hasilnya?",
            "Amati sekali lagi stimulus titik. Bilangan apa yang paling tepat?",
            "Coba kenali seluruh kumpulan dalam satu pandangan. Berapa titik yang ada?",
            "Periksa apakah jumlah yang kamu sebutkan sesuai dengan pola titik pada gambar.",
            "Nyatakan kembali banyak titik setelah mengamati susunan kecil itu.",
        ],
    },
}


QUESTION_LEADS = {
    "DIA": [
        "Perhatikan informasi berikut.",
        "Jawablah berdasarkan stimulus yang tersedia.",
        "Gunakan data pada soal ini.",
        "Cermati bilangan dan keterangan yang diberikan.",
        "Amati situasi pada pertanyaan berikut.",
        "Baca tugas ini dengan teliti.",
        "Periksa semua informasi sebelum menjawab.",
        "Pahami keadaan yang dijelaskan pada soal.",
        "Gunakan lambang atau bilangan yang terlihat.",
        "Tentukan jawaban dari keadaan berikut.",
    ],
    "PGT": [
        "Gunakan cara yang sudah dipelajari.",
        "Terapkan konsepnya pada keadaan ini.",
        "Jelaskan pemikiranmu melalui pilihan yang tepat.",
        "Hubungkan informasi soal dengan konsep bilangan.",
        "Gunakan strategi yang membantu menemukan jawaban.",
        "Perhatikan hubungan antarbagian pada soal.",
        "Tunjukkan pemahamanmu terhadap situasi berikut.",
        "Pilih jawaban setelah memeriksa konsepnya.",
        "Gunakan penalaranmu, bukan tebakan.",
        "Terapkan pemahaman bilangan pada contoh ini.",
    ],
    "PYN": [
        "Bayangkan situasi ini terjadi dalam kegiatan sehari-hari.",
        "Gunakan informasi berikut untuk membantu sebuah keputusan.",
        "Pikirkan cara menerapkan konsep ini di luar latihan.",
        "Selesaikan tantangan kecil pada situasi berikut.",
        "Gunakan bilangan untuk menjelaskan keadaan yang diberikan.",
        "Perhatikan kebutuhan pada cerita singkat ini.",
        "Tentukan hasil yang berguna untuk kegiatan berikut.",
        "Gunakan strategi bilangan untuk menyelesaikan masalah ini.",
        "Hubungkan tugas ini dengan benda atau kegiatan nyata.",
        "Buktikan pemahamanmu melalui situasi yang berbeda.",
    ],
    "CU": [
        "Periksa kembali pemahamanmu.",
        "Lakukan pengecekan dengan teliti.",
        "Pastikan hubungan bilangan pada jawabanmu benar.",
        "Uji kembali cara yang kamu gunakan.",
        "Cermati ulang informasi sebelum memilih.",
        "Verifikasi jawabanmu pada tugas ini.",
        "Tinjau kembali bilangan yang tersedia.",
        "Pastikan tidak ada informasi yang terlewat.",
        "Cek ketepatan pemahaman terhadap konsep.",
        "Nyatakan hasil pemeriksaanmu secara tepat.",
    ],
}

QUESTION_CONTEXTS = {
    "compare": [
        "Kedua kumpulan berada di dua nampan yang berdampingan.",
        "Benda-benda itu diletakkan pada baki kiri dan baki kanan.",
        "Kumpulan pertama berada di kotak biru, sedangkan kumpulan kedua di kotak hijau.",
        "Dua anak menata masing-masing satu kelompok benda di meja.",
        "Kedua kelompok siap dibandingkan sebelum dibagikan.",
        "Kumpulan kiri dan kanan dibuat untuk permainan mencocokkan jumlah.",
        "Benda pada dua piring perlu diperiksa jumlahnya.",
        "Dua rak kecil berisi kelompok benda yang berbeda atau sama.",
        "Kedua kelompok terlihat bersamaan sehingga jumlahnya dapat dibandingkan.",
        "Gunakan tampilan dua kelompok pada stimulus sebagai dasar keputusan.",
    ],
    "order": [
        "Perhatikan semua bilangan sebelum menentukan pilihan.",
        "Setiap bilangan harus dipakai tepat satu kali.",
        "Mulailah dari bilangan yang sesuai dengan arah yang diminta.",
        "Jangan menghilangkan atau menambah bilangan pada susunan.",
        "Urutan akhir harus memuat ketiga bilangan tersebut.",
        "Bandingkan bilangan satu per satu sebelum menyusun.",
        "Gunakan tanda arah pada pertanyaan sebagai petunjuk.",
        "Pastikan posisi setiap bilangan mengikuti arah urutan.",
        "Pilih satu susunan lengkap yang paling tepat.",
        "Periksa kembali bilangan pertama, tengah, dan terakhir.",
    ],
    "compose": [
        "Kedua bagian akan digabungkan menjadi satu jumlah.",
        "Tidak ada benda yang hilang ketika kedua bagian disatukan.",
        "Bayangkan dua kelompok benda dimasukkan ke satu keranjang.",
        "Jumlah keseluruhan harus mewakili kedua bagian sekaligus.",
        "Gabungkan bagian pertama dan bagian kedua secara mental.",
        "Kedua kelompok merupakan bagian dari satu kumpulan utuh.",
        "Gunakan cerita penggabungan ini untuk memeriksa bilangan.",
        "Hasil yang dicari adalah jumlah setelah kedua bagian bertemu.",
        "Pikirkan benda dari dua tempat yang dikumpulkan bersama.",
        "Pilih bilangan yang tidak hanya mewakili salah satu bagian.",
    ],
    "decompose": [
        "Kedua bagian harus membentuk kembali bilangan semula.",
        "Tidak boleh ada bagian yang lebih besar daripada bilangan utuhnya.",
        "Bayangkan jumlah itu dibagi menjadi dua kelompok benda.",
        "Pasangan pilihan menunjukkan dua bagian dari satu keseluruhan.",
        "Jumlah kedua bagian menjadi pemeriksaan terhadap jawabanmu.",
        "Gunakan pasangan bilangan untuk mewakili satu kumpulan utuh.",
        "Pilih penguraian yang dapat digabungkan kembali tanpa sisa.",
        "Dua bagian boleh berbeda, tetapi jumlahnya harus tetap.",
        "Perhatikan bahwa bilangan utuh tidak berubah setelah diuraikan.",
        "Temukan pasangan yang paling tepat untuk memecah jumlah tersebut.",
    ],
    "place": [
        "Posisi angka menentukan nilai yang harus dipilih.",
        "Bedakan angka yang berada di kiri dan di kanan.",
        "Gunakan pemahaman tentang puluhan dan satuan.",
        "Nilai angka tidak selalu sama dengan bentuk digitnya.",
        "Periksa tempat angka sebelum memilih nilainya.",
        "Bilangan ini tersusun dari puluhan dan satuan.",
        "Tentukan nilai berdasarkan posisi, bukan hanya bentuk angka.",
        "Pikirkan pengelompokan sepuluh benda untuk tempat puluhan.",
        "Satuan menunjukkan benda tersisa setelah puluhan dibentuk.",
        "Pilihan yang benar harus sesuai dengan tempat yang disebutkan.",
    ],
    "read": [
        "Ucapkan nama bilangan dengan lafal yang jelas.",
        "Hubungkan lambang tertulis dengan kata bilangannya.",
        "Baca angka sebagai satu nama bilangan yang utuh.",
        "Perhatikan kedua digit jika lambangnya terdiri dari dua angka.",
        "Nama yang dipilih harus sesuai dengan lambang tersebut.",
        "Gunakan kosakata bilangan yang tepat.",
        "Jangan membaca digit secara terpisah jika membentuk satu bilangan.",
        "Sampaikan nama bilangan sesuai aturan bahasa Indonesia.",
        "Cocokkan lambang pada soal dengan nama yang kamu ketahui.",
        "Pastikan nama yang diucapkan mewakili nilai lambang.",
    ],
    "write": [
        "Ubah kata bilangan itu menjadi lambang angka.",
        "Tuliskan angka yang mewakili nama bilangan tersebut.",
        "Perhatikan apakah nama itu menunjukkan satu atau dua digit.",
        "Lambang yang ditulis harus memiliki nilai yang sama.",
        "Gunakan penulisan angka yang biasa dipakai dalam matematika.",
        "Tentukan digit yang sesuai dengan nama bilangan.",
        "Tulislah lambang tanpa menambahkan angka yang tidak disebutkan.",
        "Cocokkan tulisanmu dengan nilai kata bilangan.",
        "Periksa urutan digit sebelum menyelesaikan respons.",
        "Lambang akhir harus dapat dibaca sebagai nama yang diberikan.",
    ],
    "match": [
        "Jumlah benda pada gambar menjadi dasar pemadanan.",
        "Lambang yang dipilih harus memiliki nilai sama dengan kumpulan.",
        "Cocokkan satu benda dengan satu nilai bilangan.",
        "Jangan memilih angka hanya berdasarkan letak pilihan.",
        "Periksa banyak benda sebelum memadankannya dengan lambang.",
        "Kumpulan dan lambang harus menunjuk jumlah yang sama.",
        "Gunakan korespondensi satu-satu untuk memeriksa kecocokan.",
        "Angka yang benar akan menjadi label bagi seluruh kumpulan.",
        "Pilih lambang yang mewakili semua benda pada stimulus.",
        "Pastikan pemadanan tidak kurang dan tidak lebih satu benda.",
    ],
}


def styled_question(kind: str, typ: str, index: int, base: str) -> str:
    if kind in QUESTION_VARIANTS:
        shape = "{shape}"  # Replaced by the caller for the counting variants.
        template = QUESTION_VARIANTS[kind][typ][index]
        return template
    return f"{QUESTION_LEADS[typ][index]} {base} {QUESTION_CONTEXTS[kind][index]}"


def make_questions(meta):
    out = []
    kind = meta["kind"]
    for typ in ("DIA", "PGT", "PYN", "CU"):
        for i in range(10):
            no = i + 1
            type_index = ("DIA", "PGT", "PYN", "CU").index(typ)
            data_index = (i + type_index * 3) % 10
            method = "ORANG_TUA" if kind in {"count", "subitize", "read", "write"} else "OTOMATIS"
            image = None
            concept = None
            application = None
            rubric = rubrics(kind)
            if kind == "count":
                n = COUNTS[(i + (0 if typ == "DIA" else 2 if typ == "PGT" else 4 if typ == "PYN" else 1)) % len(COUNTS)]
                shape = "lingkaran" if i % 2 == 0 else "persegi"
                image = {"n": n, "desc": f"{n} {shape} berwarna biru tersusun rapi agar setiap benda dapat ditunjuk satu kali."}
                question = QUESTION_VARIANTS["count"][typ][i].format(shape=shape)
                guide = "Tampilkan stimulus. Amati apakah anak menunjuk atau menelusuri setiap benda tepat satu kali dan menyebutkan jumlah akhirnya; jangan menghitungkan."
                if typ in {"PGT", "PYN"}: concept = "Saat membilang, satu bilangan dipasangkan dengan satu benda dan bilangan terakhir menyatakan jumlah seluruh benda."
                if typ in {"PGT", "PYN"}: application = "Anak dapat menggunakan cara ini ketika menghitung mainan atau buah yang tersusun di rumah."
            elif kind == "subitize":
                n = [3, 4, 5, 6, 4, 5, 3, 6, 5, 4][data_index]
                image = {"n": n, "desc": f"Kumpulan kecil berisi {n} titik biru dengan susunan yang mudah dikenali tanpa membilang satu per satu."}
                question = QUESTION_VARIANTS["subitize"][typ][i]
                guide = "Tampilkan stimulus dan minta anak menyebutkan jumlah tanpa menunjuk atau membilang satu per satu. Jangan menetapkan batas waktu yang tidak tercantum."
                if typ in {"PGT", "PYN"}: concept = "Subitasi berarti mengenali banyak benda dalam kumpulan kecil secara langsung, bukan dengan membilang setiap benda satu per satu."
                if typ in {"PGT", "PYN"}: application = "Anak dapat mengenali jumlah kecil kancing atau balok yang terlihat sekilas tanpa menghitung satu per satu."
            elif kind == "compare":
                a, b = PAIRS[data_index]
                rel = "sama banyak" if a == b else "lebih banyak" if a > b else "lebih sedikit"
                image = {"a": a, "b": b, "desc": f"Dua kumpulan berdampingan; kumpulan kiri berisi {a} benda dan kumpulan kanan berisi {b} benda."}
                question = "Perhatikan dua kumpulan pada gambar. Bagaimana hubungan banyak benda pada kumpulan kiri dengan kumpulan kanan?"
                choice, key = automatic_choices(rel, ["lebih banyak", "lebih sedikit", "sama banyak"], answer_position=(i + type_index) % 3)
                question = styled_question(kind, typ, i, f"Kumpulan kiri memiliki {a} benda dan kumpulan kanan memiliki {b} benda. Pilih hubungan jumlah yang benar.")
                guide = "Bacakan pertanyaan dan biarkan anak memilih hubungan yang tepat dari tiga pilihan. Jangan menyebutkan hasil perbandingan."
                if typ in {"PGT", "PYN"}: concept = "Membandingkan dua kumpulan berarti menentukan apakah satu kumpulan lebih banyak, lebih sedikit, atau sama banyak daripada kumpulan lain."
                if typ in {"PGT", "PYN"}: application = "Anak dapat membandingkan jumlah pensilnya dengan jumlah pensil teman menggunakan istilah yang tepat."
            elif kind == "order":
                nums = NUMBERS[data_index]
                direction = "terkecil ke terbesar" if i % 2 == 0 else "terbesar ke terkecil"
                correct = sorted(nums, reverse=direction.startswith("terbesar"))
                distract = [sorted(nums), list(reversed(sorted(nums))), [nums[1], nums[2], nums[0]]]
                distract = [" – ".join(map(str, x)) for x in distract if x != correct]
                extra_distractors = [
                    " – ".join(map(str, [nums[0], nums[2], nums[1]])),
                    " – ".join(map(str, [nums[2], nums[0], nums[1]])),
                ]
                choice, key = automatic_choices(" – ".join(map(str, correct)), distract + extra_distractors, answer_position=(i + type_index) % 3)
                question = styled_question(kind, typ, i, f"Pilih urutan bilangan {', '.join(map(str, nums))} dari {direction}.")
                guide = "Bacakan arah pengurutan dan biarkan anak memilih satu urutan lengkap. Jangan membantu dengan menyebutkan bilangan yang lebih besar atau lebih kecil."
                if typ in {"PGT", "PYN"}: concept = "Urutan naik menempatkan bilangan dari yang paling kecil ke paling besar; urutan turun menggunakan arah sebaliknya."
                if typ in {"PGT", "PYN"}: application = "Anak dapat mengurutkan nomor halaman atau nomor antrean sesuai arah yang diminta."
            elif kind == "compose":
                a, b = PARTS[data_index]; total = a + b
                choice, key = automatic_choices(total, [total - 1, total + 1, total + 2], answer_position=(i + type_index) % 3)
                question = styled_question(kind, typ, i, f"Bagian pertama berjumlah {a} dan bagian kedua berjumlah {b}. Pilih bilangan yang menunjukkan jumlah seluruh bagian.")
                guide = "Bacakan kedua bagian dan minta anak memilih jumlah keseluruhan tanpa menyarankan operasi atau jawaban."
                if typ in {"PGT", "PYN"}: concept = "Menggabungkan dua bagian berarti menentukan jumlah keseluruhan dari kedua bagian tersebut."
                if typ in {"PGT", "PYN"}: application = "Anak dapat menentukan jumlah seluruh pensil ketika beberapa pensil berada di dua tempat berbeda."
            elif kind == "decompose":
                total = TOTALS[data_index]; a, b = PARTS[data_index]
                correct = f"{a} dan {b}"
                choice, key = automatic_choices(correct, [f"{a+1} dan {b}", f"{a} dan {b+1}", f"{a+2} dan {b+1}"], answer_position=(i + type_index) % 3)
                question = styled_question(kind, typ, i, f"Bilangan {total} dapat diuraikan menjadi dua bagian. Pilih pasangan bagian yang jumlahnya tepat {total}.")
                guide = "Bacakan bilangan dan pilihan. Biarkan anak menentukan pasangan bagian yang membentuk bilangan tersebut."
                if typ in {"PGT", "PYN"}: concept = "Menguraikan bilangan berarti menemukan bagian-bagian yang jika digabungkan kembali membentuk bilangan semula."
                if typ in {"PGT", "PYN"}: application = "Anak dapat memikirkan dua kelompok benda yang jika digabungkan menjadi jumlah yang sama."
            elif kind == "place":
                n = [12, 15, 18, 20, 14, 17, 19, 11, 16, 13][data_index]
                tens, ones = divmod(n, 10)
                ask_tens = i % 2 == 0
                digit, value, label = (tens, tens * 10, "puluhan") if ask_tens else (ones, ones, "satuan")
                choice, key = automatic_choices(value, [digit, n, value + 1], answer_position=(i + type_index) % 3)
                question = styled_question(kind, typ, i, f"Dalam bilangan {n}, berapakah nilai angka pada tempat {label}?")
                guide = "Bacakan bilangan dan tempat yang ditanyakan. Biarkan anak memilih nilai angka berdasarkan posisinya."
                if typ in {"PGT", "PYN"}: concept = "Nilai sebuah angka bergantung pada posisinya. Angka pada tempat puluhan bernilai sepuluh kali angka itu; angka pada satuan bernilai sesuai angkanya."
                if typ in {"PGT", "PYN"}: application = "Anak dapat menggunakan nilai tempat ketika membaca jumlah benda yang dikelompokkan menjadi puluhan dan satuan."
            elif kind == "read":
                name, n = NAMES[data_index]
                question = styled_question(kind, typ, i, f"Lihat lambang bilangan {n}. Sebutkan nama bilangan itu.")
                guide = "Tampilkan lambang bilangan dan minta anak menyebutkan namanya. Catat ucapan anak tanpa menawarkan pilihan nama."
                if typ in {"PGT", "PYN"}: concept = "Lambang bilangan adalah tanda tertulis yang mewakili nama dan banyaknya suatu bilangan."
                if typ in {"PGT", "PYN"}: application = "Anak dapat membaca nomor rumah atau nomor halaman dengan menyebutkan nama bilangannya."
            elif kind == "write":
                name, n = NAMES[(data_index + 2) % len(NAMES)]
                question = styled_question(kind, typ, i, f"Dengarkan nama bilangan: {name}. Tuliskan lambang bilangannya.")
                guide = "Bacakan nama bilangan dengan jelas. Minta anak menuliskan lambangnya pada fasilitas respons yang tersedia dan catat hasilnya."
                if typ in {"PGT", "PYN"}: concept = "Nama bilangan dapat diubah menjadi lambang bilangan yang ditulis dengan angka."
                if typ in {"PGT", "PYN"}: application = "Anak dapat menuliskan jumlah benda yang disebutkan orang tua dalam bentuk angka."
            elif kind == "match":
                n = [4, 7, 5, 9, 6, 8, 10, 12, 14, 16][data_index]
                image = {"n": n, "desc": f"Satu kumpulan gambar berisi tepat {n} benda yang dapat dipasangkan satu per satu dengan lambang bilangan."}
                choice, key = automatic_choices(n, [n - 1, n + 1, n + 2], answer_position=(i + type_index) % 3)
                question = styled_question(kind, typ, i, "Lihat kumpulan benda pada gambar. Pilih lambang bilangan yang cocok dengan banyak benda tersebut.")
                guide = "Tampilkan stimulus dan biarkan anak memilih lambang yang cocok. Jangan menghitungkan atau menunjuk benda untuk anak."
                if typ in {"PGT", "PYN"}: concept = "Lambang bilangan cocok dengan kumpulan benda jika jumlah bendanya sama dengan nilai lambang tersebut."
                if typ in {"PGT", "PYN"}: application = "Anak dapat memilih label angka yang sesuai untuk menandai jumlah balok atau kancing."
            if typ in {"DIA", "CU"}:
                concept = None
                application = None
            out.append(base_question(meta, typ, no, question, method, choice=choice if method == "OTOMATIS" else None, key=key if method == "OTOMATIS" else None, image=image, guide=guide, concept=concept, application=application, rubric=rubric))
    return out


def write_svg(question: dict, meta: dict):
    if not question["butuh_gambar"]:
        return
    kind = meta["kind"]
    qno = int(question["id_soal"].rsplit("-", 1)[1])
    # Reconstruct the small deterministic stimulus from the question number and type.
    typ = question["jenis_soal"]
    idx = qno - 1
    type_index = ("DIA", "PGT", "PYN", "CU").index(typ)
    data_index = (idx + type_index * 3) % 10
    if kind == "count":
        n = COUNTS[(idx + (0 if typ == "DIA" else 2 if typ == "PGT" else 4 if typ == "PYN" else 1)) % len(COUNTS)]
        svg_kind = "count"; data = {"n": n, "shape": "lingkaran" if idx % 2 == 0 else "persegi"}
    elif kind == "subitize":
        svg_kind = "subitize"; data = {"n": [3, 4, 5, 6, 4, 5, 3, 6, 5, 4][data_index]}
    elif kind == "compare":
        svg_kind = "compare"; data = {"a": PAIRS[data_index][0], "b": PAIRS[data_index][1]}
    else:
        svg_kind = "match"; data = {"n": [4, 7, 5, 9, 6, 8, 10, 12, 14, 16][data_index]}
    (IMG / f"{question['id_soal']}.svg").write_text(svg_for(svg_kind, data), encoding="utf-8")


def main():
    OUT.mkdir(parents=True, exist_ok=True); IMG.mkdir(parents=True, exist_ok=True)
    index = []
    for meta in INDICATORS:
        data = {
            "id_indikator": meta["id"],
            "hierarki": {"CP": CP, "ATP": meta["atp"], "TP": meta["tp"], "KM": meta["km"], "Indikator": f"{meta['id']} — {meta['text']}", "kategori": meta["cat"]},
            "soal": make_questions(meta),
        }
        path = OUT / f"MTK-A-K1-{meta['id'].split('-K1-')[1]}.json"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        for q in data["soal"]:
            write_svg(q, meta)
        index.append({"id_indikator": meta["id"], "json": str(path.relative_to(ROOT)), "jumlah": len(data["soal"]), "kategori": meta["cat"]})
    (ROOT / "batch_400_index.json").write_text(json.dumps({"total": sum(x["jumlah"] for x in index), "indikator": index}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
