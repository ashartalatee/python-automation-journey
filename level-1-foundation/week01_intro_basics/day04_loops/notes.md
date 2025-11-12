# Day 04 — Loops & Iteration Thinking

## Konsep
- for, while, range(), nested loops
- list comprehension (vectorization)
- generator expressions + sum()
- enumerate(), zip(), itertools (kapan pakai)

## Praktik hari ini
1. Buat script menghitung total harga (lihat main.py)
2. Tambah per-kategori dengan nested loop sederhana
3. Refactor jadi generator + sum, atau dict accumulation

## Observasi & Tips
- Gunakan generator (`sum(p[2] for p in products)`) untuk performa dan readability.
- Jangan ulang perhitungan berat: cache hasil ketika akan dipakai berulang.
- Pisahkan validasi/data parsing ke helper agar fungsi utama bersih (SoC).
- Tambahkan type hints agar IDE bantu cek tipe.
- Untuk nested loops besar (N^2), pikirkan optimasi (sort + two-pointer, atau prune).

## To Improve
- Uji edge-case: produk dengan tipe harga string, list kosong, None.
- Konversi `find_bundle_options` ke lebih efisien jika dataset besar.
