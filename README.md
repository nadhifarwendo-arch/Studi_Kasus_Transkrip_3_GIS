# Studi Kasus Transkrip 3 — GIS untuk Pengelolaan Aset

## Ringkasan
Paket ini berangkat dari **Transkrip 3**, yang membahas GIS dan penerapannya pada pekerjaan/pengelolaan aset. Studi kasus latihan ini menggambarkan tim yang perlu mendata aset, melihat jumlah aset menurut kategori dan status, serta menyiapkan data koordinat agar dapat digunakan dalam sistem geospasial.

## Rumusan masalah
Bagaimana menyusun data aset berkoordinat agar lebih mudah diringkas dan dibawa ke aplikasi pemetaan?

## Tujuan
1. Membaca data aset dari CSV.
2. Menghitung jumlah aset per kategori dan status.
3. Membuat ekspor GeoJSON berisi titik koordinat aset.

## Isi repositori
```text
.
├── README.md
├── transkrip-3-gis-asli.txt
└── studi-kasus-gis-pengelolaan-aset/
    ├── data/assets.csv
    ├── src/analyze_assets.py
    └── output/                 # dibuat saat program dijalankan
```

## Implementasi
Program menggunakan Python standar, jadi tidak memerlukan library eksternal. Data aset pada `data/assets.csv` adalah **data contoh/fiktif**. Koordinat pada dataset tidak boleh dianggap sebagai data operasional yang telah diverifikasi.

### Cara menjalankan
Pastikan Python 3 sudah terpasang. Dari folder utama hasil ekstraksi:

```bash
python studi-kasus-gis-pengelolaan-aset/src/analyze_assets.py
```

Di Windows, apabila perintah `python` tidak dikenali, coba `py`.

### Output
Program membuat tiga file di folder `output/`:
- `summary_by_category.csv` — jumlah aset menurut kategori.
- `summary_by_status.csv` — jumlah aset menurut status.
- `assets.geojson` — data titik aset dengan urutan koordinat GeoJSON `[longitude, latitude]`.

## Hubungan dengan materi
Studi kasus ini mengubah bahasan GIS/data spasial dan pengelolaan aset menjadi tugas pemrosesan data sederhana. Implementasi ini merupakan contoh pembelajaran, bukan sistem GIS lengkap.

## Batasan
- Data dan koordinat bersifat fiktif.
- Program tidak memvalidasi kebenaran posisi aset atau sistem referensi koordinat untuk penggunaan profesional.
- Untuk sistem produksi, data harus divalidasi dan disesuaikan dengan kebutuhan organisasi.
