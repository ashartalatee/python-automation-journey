# src/utils.py
from pathlib import Path
from datetime import datetime

def get_project_root() -> Path:
    """
    Cari root folder proyek (folder yang mengandung folder 'src')
    """
    return Path(__file__).resolve().parents[1]

def get_log_file() -> Path:
    """
    Pastikan log selalu tersimpan di /data/logs/activity.log
    """
    project_root = get_project_root()
    log_dir = project_root / "data" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    return log_dir / "activity.log"

def log_message(message: str):
    log_file = get_log_file()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(f"[LOG] {message}")
