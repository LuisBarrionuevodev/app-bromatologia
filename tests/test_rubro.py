import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.rubro_logica import obtener_rubro_por_nombre

# Probamos buscar un rubro ya cargado, por ejemplo "CARNICERÍA"
rubros = obtener_rubro_por_nombre("CARNICERÍA").values()

for rubro in rubros:
    print(rubro)

