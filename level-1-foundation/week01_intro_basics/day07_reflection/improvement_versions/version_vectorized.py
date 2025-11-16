"""
Version 2 — Vectorized
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


def get_nama_semua_barang(cart: Cart) -> List[str]:
    return [item["nama"] for item in cart]


def main():
    cart: Cart = []

    tambah_barang(cart, "susu", 15000)
    tambah_barang(cart, "teh", 8000)

    print("Semua barang:", get_nama_semua_barang(cart))
    print("Total harga:", hitung_total(cart))


if __name__ == "__main__":
    main()
