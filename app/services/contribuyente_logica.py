from app.models.contribuyente import Contribuyente
from app.validators.validar_contribuyente import validar_contribuyente
from mysql.connector import errors
from app.validators.comunes import validar_cuit , validar_tipo , validar_no_vacio
def validar_cuit_unico(cuit):
    if Contribuyente.exists(cuit):
        raise ValueError(f"El cuit {cuit} ya está registrado.")

def validar_cuit_existente(cuit):
    if not Contribuyente.exists(cuit):
        raise ValueError(f"El cuit {cuit} no existe en la base de datos.")    


def crear_contribuyente(nombre,apellido,cuit,sexo):
    try:
        validar_contribuyente(cuit,nombre,apellido,sexo)
        validar_cuit_unico(cuit)
        Contribuyente.create(nombre,apellido,cuit,sexo)

        print("Contribuyente creado correctamente.")
    except(ValueError,TypeError) as e:
        print(f"[Error de validacion] {e}")

    except Exception as e:
        print(f"[Error inesperado] {e}")


def obtener_contribuyente(cuit):
    try:
        validar_no_vacio(cuit, "CUIT")
        validar_tipo(cuit, "CUIT", str)
        validar_cuit(cuit)  
        validar_cuit_existente(cuit)
        resultado= Contribuyente.get_by_cuit(cuit)
        print(f"Contribuyente encontrado: {resultado}")
        return resultado

    except (ValueError,TypeError) as e:
        print(f"[Error de validacion] {e}")
        return None

    except Exception as e:
        print(f"[Error al obtener contribuyente]")
        return None
    
def actualizar_contribuyente(nombre,apellido,cuit,sexo):
    try:
        validar_contribuyente(cuit,nombre,apellido,sexo)
        validar_cuit_existente(cuit)
        Contribuyente.update(cuit,nombre,apellido,sexo)
        print("Contibuyente actualizado correctamente.")
    except(ValueError,TypeError) as e:
        print(f"[Error de validacion] {e}")
    except Exception as e:
        print(f"[Error inesperado al actualizar] {e}")

def eliminar_contribuyente(cuit):
    try:
        validar_no_vacio(cuit, "CUIT")
        validar_tipo(cuit, "CUIT", str)
        validar_cuit(cuit)  
        validar_cuit_existente(cuit)
        Contribuyente.delete(cuit)
        print("Contribuyente eliminado correctamente. ")
    except(ValueError,TypeError) as e:
        print(f"[Error de validacion] {e}")

    except Exception as e:
        print(f"[Error inesperado al eliminar] {e}")    

