from app.models.domicilio import Domicilio
from app.validators.validar_domicilio import validar_domicilio
from mysql.connector import errors
from app.validators.comunes import validar_no_vacio, validar_tipo

def crear_domicilio(calle, numero, detalle=None):
    try:
        validar_domicilio(calle, numero, detalle)
        Domicilio.create(calle, numero, detalle)
        print("Domicilio creado correctamente.")
    except (ValueError, TypeError) as e:
        print(f"[Error de validación] {e}")
    except Exception as e:
        print(f"[Error inesperado] {e}")

def obtener_domicilio(id_domicilio):
    try:
        validar_no_vacio(id_domicilio, "ID de domicilio")
        validar_tipo(id_domicilio, "ID de domicilio", int)
        resultado = Domicilio.get_by_id(id_domicilio)
        if resultado:
            print(f"Domicilio encontrado: {resultado}")
            return resultado
        else:
            print("No se encontró ningún domicilio con ese ID.")
            return None
    except (ValueError, TypeError) as e:
        print(f"[Error de validación] {e}")
        return None
    except Exception as e:
        print(f"[Error al obtener domicilio] {e}")
        return None

def actualizar_domicilio(id_domicilio, calle, numero, detalle=None):
    try:
        validar_no_vacio(id_domicilio, "ID de domicilio")
        validar_tipo(id_domicilio, "ID de domicilio", int)
        validar_domicilio(calle, numero, detalle)
        Domicilio.update(id_domicilio, calle, numero, detalle)
        print("Domicilio actualizado correctamente.")
    except (ValueError, TypeError) as e:
        print(f"[Error de validación] {e}")
    except Exception as e:
        print(f"[Error inesperado al actualizar] {e}")

def eliminar_domicilio(id_domicilio):
    try:
        validar_no_vacio(id_domicilio, "ID de domicilio")
        validar_tipo(id_domicilio, "ID de domicilio", int)
        Domicilio.delete(id_domicilio)
        print("Domicilio eliminado correctamente.")
    except (ValueError, TypeError) as e:
        print(f"[Error de validación] {e}")
    except Exception as e:
        print(f"[Error inesperado al eliminar] {e}")
