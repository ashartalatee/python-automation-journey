"""
Version 1 — Optimized SoC (Separation of Concerns)
"""

from typing import List, Dict

CartItem = Dict[str, int]
Cart = List[CartItem]


def tambah_barang(cart: Cart, nama: str, harga: int) -> None:
    cart.append({"nama": nama, "harga": harga})


def hapus_barang(cart: Cart, nama: str) -> None:
    cart[:] = [item for item in cart if item["nama"] != nama]


def hitung_total(cart: Cart) -> int:
    return sum(item["harga"] for item in cart)


def tampilkan_barang(cart: Cart) -> None:
    print("\nDaftar Barang:")
    for item in cart:
        print(f"- {item['nama']} = {item['harga']}")


def main():
    cart: Cart = []

    tambah_barang(cart, "apel", 5000)
    tambah_barang(cart, "roti", 12000)

    tampilkan_barang(cart)
    print("Total:", hitung_total(cart))


if __name__ == "__main__":
    main()
