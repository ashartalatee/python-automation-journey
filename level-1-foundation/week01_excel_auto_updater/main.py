# Entry point untuk Excel Auto-Updater

from src.update_excel import update_excel
from pathlib import Path

def main():
    raw_file = Path("data/raw/sample_data.xlsx")
    processed_file = Path("data/processed/sample_data_updated.xlsx")

    # Update kolom "Sales" dengan nilai baru (contoh)
    update_excel(
        file_path=raw_file,
        column_to_update="Sales",
        new_value=888,
        output_path=processed_file
    )

if __name__ == "__main__":
    main()