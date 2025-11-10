def hitung_total(daftar_harga):
    """Menghitung total harga dari dict item:harga"""
    return sum([harga for harga in daftar_harga.values()])

def main():
    belanja = {
        "apel": 3000,
        "pisang": 2000,
        "jeruk": 4000
    }

    print("Daftar Belanja:")
    for item, harga in belanja.items():
        print(f"{item}: Rp {harga}")

    total = hitung_total(belanja)
    print(f"\nSetelah menambah mangga, total: Rp {hitung_total(belanja)}")

if __name__ == "__main__":
    main()