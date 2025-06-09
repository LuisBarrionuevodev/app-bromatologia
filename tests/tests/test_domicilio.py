import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.services.domicilio_logica import crear_domicilio

creando_domicilio_dos= crear_domicilio("Las Heras",25,)
