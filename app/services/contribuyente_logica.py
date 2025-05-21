from app.models.contribuyente import Contribuyente
from app.validators.validar_contribuyente import validar_contribuyente
from app.services.contribuyente_logica import validar_cuit_existente, validar_cuit_unico
from mysql.connector import errors
def validar_cuit_unico(cuit):
    if Contribuyente.exists(cuit):
        raise ValueError(f"El cuit {cuit} ya está registrado.")

def validar_cuit_existente(cuit):
    if not Contribuyente.exists(cuit):
        raise ValueError(f"El cuit {cuit} no existe en la base de datos.")    
