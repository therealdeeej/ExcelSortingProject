import json
from pathlib import Path

def load_config(project_root: Path) -> dict:
    """
    Loads the column configuration from config.json.
    """
    config_path = project_root / "config.json"
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")
    
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
    
    return config
