# Fungsi untuk update file Excel

import pandas as pd
from pathlib import Path

def update_excel(file_path, column_to_update, new_value, output_path=None):
    """
    Update nilai kolom tertentu di Excel dan simpan hasilnya.
    
    Args:
        file_path (str/Path): Path file Excel asli
        column_to_update (str): Nama kolom yang ingin di update
        new_Value: Nilai baru untuk update
        output_path (str/Path, opsional): Path simpan hasil. Jika None, overwrite file asli.
        
    Returns:
        pd.DataFrame: DataFrame hasil update
    """
    file_path = Path(file_path)
    if not output_path:
        output_path = file_path
    else:
        output_path = Path(output_path)

    # Load Excel
    df = pd.read_excel(file_path, engine="openpyxl")

    # Update kolom
    if column_to_update in df.columns:
        df[column_to_update] = new_value
    else:
        raise ValueError(f"Column '{column_to_update}' tidak ditemukan di Excel.")
    
    # Simpan hasil
    df.to_excel(output_path, index=False)
    print(f"File berhasil diupdate dan disimpan di: {output_path}")
    return df

# Contoh penggunaan
if __name__ == "__main__":
    update_excel(
        file_path="../data/raw/sample_data.xlsx",
        column_to_update="Sales",
        new_value=999,
        output_path="../data/processed/sample_data_updated.xlsx"
    )