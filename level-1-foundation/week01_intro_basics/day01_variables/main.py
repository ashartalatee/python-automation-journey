# main.py - Day 01: Variables & Basic Operations
def kalkulator():
    try:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))

        total = a + b
        rata = (a + b) / 2

        print(f"\nHasil penjumlahan: {total}")
        print(f"Rata-rata: {rata}")

    except ValueError:
        print(" Error: Pastikan input berupa angka (int atau float).")

if __name__ == "__main__":
    kalkulator()