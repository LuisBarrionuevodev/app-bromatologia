from app.models.contribuyente import Contribuyente
def validar_cuit_unico(cuit):
    if Contribuyente.exists(cuit):
        raise ValueError(f"El cuit {cuit} ya está registrado.")

def validar_cuit_existente(cuit):
    if not Contribuyente.exists(cuit):
        raise ValueError(f"El cuit {cuit} no existe en la base de datos.")    
