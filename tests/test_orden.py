import sys
import os

# Agrega la carpeta raíz al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.orden_de_trabajo_logica import crear_orden

if __name__ == "__main__":
    print("▶ Ejecutando test de creación de orden...")
    crear_orden(800, "2025-02-02")

