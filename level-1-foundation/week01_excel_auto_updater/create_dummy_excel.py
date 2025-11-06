import pandas as pd
from pathlib import Path

# Folder data/raw
data_raw = Path("data/raw")
data_raw.mkdir(parents=True, exist_ok=True)

# Data dummy
data = {
    "ID": [1, 2, 3],
    "Name": ["Product A", "Product B", "Product C"],
    "Sales": [100, 150, 200],
    "Date": ["2025-11-01", "2025-11-02", "2025-11-03"]
}

df = pd.DataFrame(data)

# Simpan ke Excel valid
file_path = data_raw / "sample_data.xlsx"
df.to_excel(file_path, index=False, engine="openpyxl")

print(f"File Excel dummy berhasil dibuat di: {file_path}")
