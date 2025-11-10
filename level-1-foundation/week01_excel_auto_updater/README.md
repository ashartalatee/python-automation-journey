 Level 1 – Foundation Builder 🧩
> Fokus: Fundamental Python Automation (File, Excel, Folder, dan Data Cleaning)

 📅 Minggu 1: Excel Auto-Updater

 Tujuan
Membuat sistem sederhana untuk **memperbarui file Excel secara otomatis**, mencatat aktivitas (logging), dan menyimpan hasilnya secara terstruktur.

 Capaian Teknis
✅ Automasi update file Excel dengan `pandas`  
✅ Logging sistem otomatis menggunakan `datetime`  
✅ Struktur folder profesional untuk data & kode  
✅ Dokumentasi README lengkap + demo visual  
✅ Testing dasar dengan `unittest`

Day 1 - Tujuan Hari Ini
- Setup repo & struktur folder profesional
- Membuat README awal
- Siap coding besok

 Day 2 – Data & Eksplorasi
✅ File Excel contoh sudah disiapkan di data/raw/
✅ Notebook exploration.ipynb berisi analisis awal struktur file Excel

💡 Insight:
- Memahami kolom & tipe data sebelum automasi sangat penting
- Notebook membantu eksperimen tanpa mengganggu script utama

 Day 3 – Coding Fungsi Utama
✅ update_excel.py dibuat, bisa:
- Membaca file Excel
- Update kolom tertentu
- Simpan hasil ke folder processed/

✅ main.py dibuat sebagai entry point

💡 Insight:
- Fungsi modular memudahkan testing & penggunaan berulang
- Output dipisahkan di folder processed agar file asli tetap aman

 Day 4 – Logging & Utility
✅ utils.py dibuat untuk logging & helper functions
✅ update_excel.py sekarang otomatis mencatat setiap update di data/logs/activity.log

💡 Insight:
- Logging penting untuk tracking aktivitas automasi
- Folder logs membuat data historis mudah dilacak

 Day 5 – Testing & Polishing
✅ test_update_excel.py dibuat untuk memastikan fungsi update_excel() bekerja
✅ Code sudah dirapikan & docstring konsisten
✅ Folder logs/processed bersih & rapi

💡 Insight:
- Testing penting agar script aman digunakan berulang
- Polishing meningkatkan profesionalisme proyek & mempermudah kolaborasi

