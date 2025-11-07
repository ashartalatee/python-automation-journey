# Fungsi tambahan untuk logging & tanggal
from datetime import datetime
from pathlib import Path

def log_message(message: str, log_file: str = "../data/logs/activity.log"):
    """
    Menyimpan pesan log ke file log harian.
    
    
    Args:
        message (str): Pesan log
        log_file (str/Path): Path file log
    """
    log_file = Path(log_file)
    log_file.parent.mkdir(parents=True, exist_ok=True) #Buat folder log otomatis

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    
    print(f"[LOG] {message}")