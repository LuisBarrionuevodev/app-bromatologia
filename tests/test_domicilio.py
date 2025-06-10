import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.services.domicilio_logica import crear_domicilio

if __name__ == "__main__":
    print("▶ Ejecutando test de creación de domicilio...")
    crear_domicilio("Bernabe Araoz",1000,)
