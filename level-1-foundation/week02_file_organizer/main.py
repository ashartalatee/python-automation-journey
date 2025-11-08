from src.organizer import organize_files

if __name__ == "__main__":
    extensions_map = {
        ".csv": "data",
        ".xlsx": "excel",
        ".pdf": "pdfs",
        ".jpg": "images",
        ".png": "images",
    }

    organize_files(
        source_dir="data/raw",
        dest_dir="data/processed",
        extensions_map=extensions_map,
    )