# src/utils.py
from pathlib import Path
from datetime import datetime

LOG_FILE = Path(__file__).parent.parent / "data" / "logs" / "activity.log"

def log_message(message: str, log_file: Path = LOG_FILE):
    log_file.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(f"[LOG] {message}")
