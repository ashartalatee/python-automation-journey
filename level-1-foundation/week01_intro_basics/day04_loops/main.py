# main.py
from typing import List, Dict, Tuple

Product = Tuple[str, str, float]  # (name, category, price)

def compute_total(products: List[Product]) -> float:
    """
    Hitung total harga semua produk.
    """
    if not isinstance(products, list):
        raise TypeError("products must be a list")
    # Generator + sum = vectorized pattern (no manual loop accumulation)
    return sum(p[2] for p in products if _is_valid_product(p))

def compute_total_by_category(products: List[Product]) -> Dict[str, float]:
    """
    Kembalikan total harga per kategori.
    """
    totals: Dict[str, float] = {}
    for name, category, price in products:
        if not _is_valid_product((name, category, price)):
            continue
        totals[category] = totals.get(category, 0.0) + price
    return totals

# Helper kecil untuk validasi (SoC)
def _is_valid_product(p: Product) -> bool:
    try:
        name, cat, price = p
    except Exception:
        return False
    if not isinstance(name, str) or not isinstance(cat, str):
        return False
    if not (isinstance(price, (int, float))):
        return False
    return True

# Example: nested loop usage (pairwise combos)
def find_bundle_options(products: List[Product], budget: float) -> List[Tuple[Product, Product]]:
    """
    Cari pasangan produk (bundle) yang totalnya <= budget.
    Menggunakan nested loops; bisa dioptimasi nanti.
    """
    bundles = []
    n = len(products)
    for i in range(n):
        for j in range(i+1, n):
            a = products[i]
            b = products[j]
            if not (_is_valid_product(a) and _is_valid_product(b)):
                continue
            if a[2] + b[2] <= budget:
                bundles.append((a, b))
    return bundles

if __name__ == "__main__":
    sample_products: List[Product] = [
        ("Susu", "Grocery", 10.0),
        ("Roti", "Grocery", 5.0),
        ("Pasta Gigi", "Toiletries", 15.0),
        ("Sabun", "Toiletries", 3.5),
    ]

    total = compute_total(sample_products)
    print("Total semua:", total)

    totals_by_cat = compute_total_by_category(sample_products)
    print("Total per kategori:", totals_by_cat)

    bundles_under_20 = find_bundle_options(sample_products, budget=20.0)
    print("Bundles <=20:", bundles_under_20)
