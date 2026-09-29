"""Check labaratory sensors that are overdue for calibration"""

# Importerer standardbibliotek først, så tredjepartspakker (PEP8)
import json
from pathlib import Path

# Verktøy installert via -venv
import pandas as pd
import yaml

# Mappen der dette scriptet ligger. Brukes for å finne datafilene.
DATA_DIR = Path(__file__).parent


def read_config(path: Path) -> dict:
    """Read settings from a YAML file and return them as a dictionary."""
    # Åpne filen, les innholdet og gjør det om til en dictionary
    with path.open(encoding="utf-8") as file:
        return yaml.safe_load(file)


# Midlertidlig test: sjekk at config.yml leses riktig
config = read_config(DATA_DIR / "config.yml")
print(config)

