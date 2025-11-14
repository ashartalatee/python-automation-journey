# main.py
from utils import *

if __name__ == "__main__":
    sample = [
        ("Roti", "Grocery", 5),
        ("Susu", "Grocery", 10),
        ("Sabun", "Toiletries", 3.5),
    ]

    print("Pipeline Output:")
    result = run_pipeline(sample)
    print(result)

    save_to_file(str(result), "output.txt")
    print("Output disimpan ke output.txt")
