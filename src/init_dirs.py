# src/init_dirs.py
"""
Crea la estructura de carpetas básica para el proyecto JEQUIMA OCR.
Idempotente: si las carpetas ya existen, no ocurre nada.
"""
from pathlib import Path

BASE_DIRS = [
    "data/diagnostico_raw",
    "data/final_raw",
    "output",
]

def main() -> None:
    for folder in BASE_DIRS:
        Path(folder).mkdir(parents=True, exist_ok=True)
        print(f"✔  Carpeta lista: {folder}")

if __name__ == "__main__":
    main()
