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


def read_sensor_data(sensors_path: Path, calibrations_path: Path) -> pd.DataFrame:
    """Read sensors info and calibration logs, and join them on sensor_id."""
    # Les excel-filen med rom og eier for hver sensor
    sensors = pd.read_excel(sensors_path)
    # Les CSV-filen med antall dager siden kalibrering
    calibrations = pd.read_csv(calibrations_path)
    # Koble tabellene sammen der sensor_id er lik (som FINN.RAD i Excel)
    return sensors.merge(calibrations, on="sensor_id")


def find_overdue_sensors(sensor_data:pd.DataFrame, max_days: int) -> list[dict]:
    """Return sensors where days since calibration exceeds max_days."""
    # Behold bare radene der antall dager er over grensen
    overdue = sensor_data[sensor_data["days_since_calibration"] > max_days]
    # Gjør tabellen om til en liste med dictionaries, én per sensor
    return overdue.to_dict(orient="records")


# Les instillingene fra config.yml
config = read_config(DATA_DIR / "config.yml")

# Les og koble sammen sensordataene
sensor_data = read_sensor_data(DATA_DIR / "sensors.xlsx", DATA_DIR / "calibrations.csv")

# Midlertidlig test: sjekk at bare sensorene over grensen blir med
overdue = find_overdue_sensors(sensor_data, config["max_days_since_calibration"])
print(overdue)

