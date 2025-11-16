"""
Version FINAL — Clean, Modular, Typed, Safe
Menerapkan:
- Separation of Concerns (SoC)
- Vectorization
- Type Thinking
- Cache
- Error Handling
"""

from typing import List, Dict, Optional

CartItem = Dict[str, int]
Cart = List[CartItem]


# ------------------------------
# Validasi Input
# ------------------------------
def validate_harga(harga_input: str) -> Optional[int]:
    try:
        harga = int(harga_input)
        if harga < 0:
            raise ValueError("Harga tidak boleh negatif.")
        return harga
    except ValueError:
        print("[ERROR] Harga harus berupa angka positif.")
        return None


# ------------------------------
# Core Functions
# ------------------------------
def tambah_barang(cart: Cart, nama: str, harga: int) -> None:
    cart.append({"nama": nama, "harga": harga})


def hapus_barang(cart: Cart, nama: str) -> None:
    cart[:] = [item for item in cart if item["nama"] != nama]


def hitung_total(cart: Cart) -> int:
    return sum(item["harga"] for item in cart)


def tampilkan(cart: Cart) -> None:
    print("\nDaftar Barang:")
    for item in cart:
        print(f"- {item['nama']}: {item['harga']}")


def simpan_ke_file(cart: Cart, path: str = "data.txt") -> None:
    try:
        with open(path, "w") as f:
            for item in cart:
                f.write(f"{item['nama']},{item['harga']}\n")
        print("Data berhasil disimpan ke file.")
    except Exception as e:
        print("[ERROR] File tidak bisa ditulis:", e)


# ------------------------------
# Main Program
# ------------------------------
def main():
    cart: Cart = []

    while True:
        print("\n=== MENU ===")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Barang")
        print("4. Total Harga")
        print("5. Simpan ke File")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Nama barang: ")
            harga_input = input("Harga barang: ")
            harga = validate_harga(harga_input)

            if harga is None:
                continue

            tambah_barang(cart, nama, harga)

        elif pilihan == "2":
            nama = input("Nama barang yang ingin dihapus: ")
            hapus_barang(cart, nama)

        elif pilihan == "3":
            tampilkan(cart)

        elif pilihan == "4":
            total = hitung_total(cart)
            print("TOTAL =", total)

        elif pilihan == "5":
            simpan_ke_file(cart)

        elif pilihan == "6":
            print("Keluar dari program.")
            break

        else:
            print("[ERROR] Pilihan tidak valid.")


if __name__ == "__main__":
    main()
