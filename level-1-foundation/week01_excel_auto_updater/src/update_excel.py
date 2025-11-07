# Fungsi untuk update file Excel

import pandas as pd
from pathlib import Path
from src.utils import log_message

def update_excel(file_path, column_to_update, new_value, output_path=None):
    file_path = Path(file_path)
    if not output_path:
        output_path = file_path
    else:
        output_path = Path(output_path)

    # Load Excel
    df = pd.read_excel(file_path)

    # Update kolom
    if column_to_update in df.columns:
        df[column_to_update] = new_value
        log_message(f"Updated column '{column_to_update}' in {file_path.name} with value {new_value}")
    else:
        log_message(f"Failed: Column '{column_to_update}' not found in {file_path.name}")
        raise ValueError(f"Column '{column_to_update}' tidak ditemukan di Excel.")
    
    # Simpan hasil
    df.to_excel(output_path, index=False)
    log_message(f"Saved updated file to {output_path}")
    return df

# Contoh penggunaan
if __name__ == "__main__":
    update_excel(
        file_path="../data/raw/sample_data.xlsx",
        column_to_update="Sales",
        new_value=777,
        output_path="../data/processed/sample_data_updated.xlsx"
    )