import shutil
from pathlib import Path
from datetime import datetime

LOG_FILE = Path(__file__).parent.parent / "data" / "logs" / "organizer.log"

def log(message: str):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def organize_files(source_dir: str, dest_dir: str, extensions_map: dict):
    """Organize files from source directory into destination folders."""
    source = Path(source_dir)
    dest = Path(dest_dir)
    dest.mkdir(parents=True, exist_ok=True)

    for file in source.iterdir():
        if file.is_file():
            ext = file.suffix.lower()
            folder_name = extensions_map.get(ext, "others")
            target_folder = dest / folder_name
            target_folder.mkdir(exist_ok=True)
            shutil.move(str(file), str(target_folder / file.name))
            message = f"Moved {file.name} → {folder_name}/"
            print(message)
            log(message)
