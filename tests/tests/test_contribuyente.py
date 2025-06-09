
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.services.contribuyente_logica import crear_contribuyente


creando_contribuyente= crear_contribuyente("Lionel","Andres","22222222222","MASCULINO",)

