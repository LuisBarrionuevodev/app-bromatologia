from app.models.domicilio import Domicilio
from app.validators.validar_domicilio import validar_domicilio
from mysql.connector import errors
from app.validators.comunes import validar_no_vacio

def crear_domicilio(calle,numero,detalle=None):

    try:
        validar_domicilio(calle,numero,detalle)
        Domicilio.create(calle,numero,detalle)
        print("Domicilio Creado Correctamente")

    except(ValueError,TypeError) as e:
        print(f"[Error de validacion]{e}")    

    except Exception as e:
        print(f"[Error inesperado] {e}")
