# shopping_manager.py
from typing import List, Tuple, Optional, Dict
from utils import parse_number, compute_total, compute_total_by_category, is_valid_product

Product = Tuple[str, str, float]


class ShoppingManager:
    def __init__(self):
        self.products: List[Product] = []

    # CRUD Operations
    def add_product(self, name: str, category: str, price_str: str) -> bool:
        price = parse_number(price_str)
        if price is None:
            print("❌ Harga tidak valid.")
            return False
        
        product = (name, category, price)
        if not is_valid_product(product):
            print("❌ Data produk tidak valid.")
            return False
        
        self.products.append(product)
        print(f"✔ Produk ditambahkan: {product}")
        return True

    def remove_product(self, name: str) -> bool:
        for p in self.products:
            if p[0].lower() == name.lower():
                self.products.remove(p)
                print(f"✔ Produk '{name}' dihapus.")
                return True
        print(f"❌ Produk '{name}' tidak ditemukan.")
        return False

    def list_products(self) -> List[Product]:
        if not self.products:
            print("📭 Belum ada produk.")
        else:
            print("\n🛒 Daftar Produk:")
            for p in self.products:
                print(f"- {p[0]} | {p[1]} | {p[2]}")
        return self.products

    # Calculation
    def total_price(self) -> float:
        total = compute_total(self.products)
        print(f"\n💰 Total Harga: {total}")
        return total

    def total_per_category(self) -> Dict[str, float]:
        totals = compute_total_by_category(self.products)
        print("\n📊 Total per Kategori:")
        for cat, amount in totals.items():
            print(f"- {cat}: {amount}")
        return totals


    # File I/O
    def save(self, filename: str) -> None:
        try:
            with open(filename, "w", encoding="utf-8") as f:
                for name, cat, price in self.products:
                    f.write(f"{name},{cat},{price}\n")
            print(f"💾 Data disimpan ke {filename}")
        except Exception as e:
            print("❌ Gagal menyimpan:", e)

    def load(self, filename: str) -> None:
        try:
            with open(filename, "r", encoding="utf-8") as f:
                self.products.clear()
                for line in f:
                    name, cat, price = line.strip().split(",")
                    num = parse_number(price)
                    if num is not None:
                        self.products.append((name, cat, num))
            print(f"📂 Data dimuat dari {filename}")
        except FileNotFoundError:
            print("❌ File tidak ditemukan.")
        except Exception as e:
            print("❌ Gagal load:", e)
