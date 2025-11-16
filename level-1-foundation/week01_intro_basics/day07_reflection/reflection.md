# Day 07 — Reflection & Code Interrogation  
Week 01 — Python & Logic Thinking Foundation

## 1. Script yang Dipilih
- File: program_manajemen_belanja (Day 06)
- Alasan: mengandung semua komponen fundamental — variabel, list, dict, loops, kondisi, fungsi, error handling, dan file I/O — sehingga ideal untuk dianalisis menggunakan 5 Lensa Kritis.

---

## 2. Analisis Menggunakan 5 Lensa Kritis

### Lensa 1 — Vectorization
**Temuan:**
- Beberapa loop manual dapat digantikan list comprehension.
- Perhitungan total harga dapat lebih ringkas dengan fungsi `sum()`.

**Perbaikan:**
- `cart[:] = [...]` untuk penghapusan barang.
- `sum(item["harga"] for item in cart)`.

---

### Lensa 2 — Separation of Concerns (SoC)
**Temuan:**
- Banyak logika bercampur di dalam `main()`.
- Beberapa fungsi melakukan lebih dari 1 tanggung jawab.

**Perbaikan:**
Pisahkan menjadi fungsi kecil:
- tambah_barang()
- hapus_barang()
- hitung_total()
- tampilkan_barang()
- simpan_ke_file()
- validate_input()

---

### Lensa 3 — Type Thinking
**Temuan:**
- Tidak ada type hints.
- Struktur data belum diberi alias atau type definition.

**Perbaikan:**
- Tambah type hints di semua fungsi.
- Gunakan alias:
  - CartItem = Dict[str, int]  
  - Cart = List[CartItem]

---

### Lensa 4 — Cache
**Temuan:**
- Tidak ada caching, tetapi beberapa operasi bisa disimpan sementara.

**Perbaikan:**
- Simpan hasil perhitungan total ke variabel bila dibutuhkan berulang.

---

### Lensa 5 — Error Handling
**Temuan:**
- Input harga rawan error (string bukan angka).
- Potensi file write error.

**Perbaikan:**
- Tambahkan try/except.
- Tambahkan fungsi validasi input.

---

## 3. Insight Utama
> “Refactor membuat saya sadar bahwa kode yang bersih, modular, dan memiliki struktur jelas jauh lebih efisien dan scalable daripada kode yang sekadar bisa berjalan.”

---

## 4. Rencana Perbaikan (Roadmap)
- Tambahkan type hints di seluruh kode.  
- Bentuk ulang program berdasarkan fungsi modular.  
- Hilangkan loop manual → gunakan comprehension.  
- Tambahkan error handling lengkap.  
- Buat file `version_final` sebagai versi paling matang.  

---

## 5. Daftar Versi Peningkatan
- version_original.py  
- version_optimized_soc.py  
- version_vectorized.py  
- version_final.py  

