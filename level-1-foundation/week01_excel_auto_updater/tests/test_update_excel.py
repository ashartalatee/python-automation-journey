# Basic testing untuk update_excel.py

import unittest
from pathlib import Path
import pandas as pd
from src.update_excel import update_excel

class TestUpdateExcel(unittest.TestCase):
    def setUp(self):
        # Path file dummy
        self.raw_file = Path("../data/raw/sample_data.xlsx")
        self.test_file = Path("../data/processed/sample_data_updated.xlsx")

    def test_update_existing_column(self):
        # Update kolom 'Sales' menjadi 123
        df = update_excel(
            file_path=self.raw_file,
            column_to_update="Sales",
            new_value=123,
            output_path=self.test_file
        )
        # Pastikan kolom sudah terupdate
        self.assertTrue((df['Sales'] == 123).all())

    def test_update_nonexistent_column(self):
        # Pastikan ValueError muncul jika kolom tidak ada
        with self.assertRaises(ValueError):
            update_excel(
                file_path=self.raw_file,
                new_value=999,
                output_path=self.test_file
            )

if __name__ == "__main__":
    unittest.main()