# main.py
from shopping_manager import ShoppingManager

manager = ShoppingManager()

def menu():
    print("""
   SHOPPING MANAGER v1
1. Tambah produk
2. Hapus produk
3. Lihat produk
4. Total harga
5. Total per kategori
6. Simpan ke file
7. Load dari file
8. Exit
""")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Pilih menu: ")

        if choice == "1":
            name = input("Nama: ")
            cat = input("Kategori: ")
            price = input("Harga: ")
            manager.add_product(name, cat, price)

        elif choice == "2":
            name = input("Nama produk yang ingin dihapus: ")
            manager.remove_product(name)

        elif choice == "3":
            manager.list_products()

        elif choice == "4":
            manager.total_price()

        elif choice == "5":
            manager.total_per_category()

        elif choice == "6":
            filename = input("Nama file: ")
            manager.save(filename)

        elif choice == "7":
            filename = input("Nama file: ")
            manager.load(filename)

        elif choice == "8":
            print("👋 Keluar...")
            break

        else:
            print("❌ Pilihan tidak valid.")
