import json
from src.organizer import organize_files
from pathlib import Path

def load_config(config_path="config.json"):
    with open(config_path, "r") as f:
        return json.load(f)

if __name__ == "__main__":
    config = load_config()
    organize_files(
        source_dir=config["source_dir"],
        dest_dir=config["dest_dir"],
        extensions_map=config["extensions_map"],
    )