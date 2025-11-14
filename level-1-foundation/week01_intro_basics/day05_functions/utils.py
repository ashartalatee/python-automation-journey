# utils.py
from typing import List, Tuple, Dict, Optional

Product = Tuple[str, str, float]  # (name, category, price)

# Parsing & Type Conversion
def parse_number(value: str) -> Optional[float]:
    """
    Convert string to number.
    Return None kalau tidak valid.
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


# Computation Functions
def average(numbers: List[float]) -> float:
    """Hitung rata-rata dengan vectorized approach."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def compute_total(products: List[Product]) -> float:
    """Hitung total harga produk dengan generator expression."""
    return sum(p[2] for p in products if is_valid_product(p))


def compute_total_by_category(products: List[Product]) -> Dict[str, float]:
    """Total harga per kategori."""
    totals = {}
    for name, category, price in products:
        if not is_valid_product((name, category, price)):
            continue
        totals[category] = totals.get(category, 0) + price
    return totals


def filter_by_category(products: List[Product], category: str) -> List[Product]:
    """Filter produk berdasarkan kategori."""
    return [p for p in products if is_valid_product(p) and p[1] == category]


# Validation
def is_valid_product(p: Product) -> bool:
    """Validasi satu produk (name, category, price)."""
    try:
        name, cat, price = p
        return isinstance(name, str) and isinstance(cat, str) and isinstance(price, (int, float))
    except Exception:
        return False


# File I/O
def save_to_file(content: str, filename: str) -> None:
    """Simpan text ke file dengan error handling."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        print("Gagal menyimpan file:", e)


def load_products_from_txt(path: str) -> List[Product]:
    """
    Load produk dari file format:
    nama,kategori,harga
    """
    results = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) != 3:
                    continue
                name, cat, price_str = parts
                price = parse_number(price_str)
                if price is not None:
                    results.append((name, cat, price))
    except FileNotFoundError:
        print("File tidak ditemukan:", path)

    return results


# Pipeline (Automation Style)
def run_pipeline(products: List[Product]) -> Dict[str, float]:
    """
    Jalankan pipeline lengkap:
    1. Validasi
    2. Hitung total
    3. Hitung per-kategori
    """
    valid = [p for p in products if is_valid_product(p)]
    total = compute_total(valid)
    totals_by_cat = compute_total_by_category(valid)

    return {
        "total": total,
        "per_category": totals_by_cat
    }
