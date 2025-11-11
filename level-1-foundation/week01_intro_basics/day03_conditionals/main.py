def cek_stok_barang(nama_barang: str, stok: int) -> str:
    if stok > 10:
        return f"Stok {nama_barang} aman"
    elif 1 <= stok <= 10:
        return f"Stok {nama_barang} hampir habis"
    else:
        return f"Stok {nama_barang} kosong"

def main():
    try:
        nama_barang = input("Masukkan nama barang: ").strip()
        stok = int(input(f"Masukkan jumlah stok {nama_barang}: "))
        if stok < 0:
            print("Jumlah stok tidak boleh negatif!")
            return
        hasil = cek_stok_barang(nama_barang, stok)
        print(hasil)
    except ValueError:
        print("Input tidak valid, masukkan angka untuk stok!")

if __name__ == "__main__":
    main()