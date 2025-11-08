import shutil
from pathlib import Path

def organize_file(source_dir: str, dest_dir: str, extensions_map: dict):
    """Organize files from source directory into destination folders."""
    source = Path(source_dir)
    dest = Path(dest_dir)
    dest.mkdir(parents=True, exist_ok=True)

    for file in source.iterdir():
        if file.is_file():
            ext = file.sutfix.lower()
            folder_name = extensions_map.get(ext, "others")
            target_folder = dest / folder_name
            target_folder.mkdir(exist_ok=True)
            shutil.move(str(file), str(target_folder / file.name))
            print(f"Moved: {file.name} → {folder_name}")