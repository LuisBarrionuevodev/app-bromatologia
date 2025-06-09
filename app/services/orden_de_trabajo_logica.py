from app.models.orden_de_trabajo import OrdenDeTrabajo
from app.validators.validar_orden import validar_orden_de_trabajo
from mysql.connector import errors
from app.validators.comunes import validar_tipo, validar_no_vacio

def validar_id_existente(id_orden):
    if not OrdenDeTrabajo.exists(id_orden):
        raise ValueError(f"La orden con ID {id_orden} no existe.")

def validar_id_unico(id_orden):
    if OrdenDeTrabajo.exists(id_orden):
        raise ValueError(f"La orden con ID {id_orden} ya está registrada.")

def crear_orden(id_orden, fecha):
    try:
        validar_orden_de_trabajo(id_orden, fecha)
        validar_id_unico(id_orden)
        OrdenDeTrabajo.create(id_orden, fecha)
        print("Orden de trabajo creada correctamente.")
    except (ValueError, TypeError) as e:
        print(f"[Error de validación] {e}")
    except Exception as e:
        print(f"[Error inesperado al crear orden] {e}")

def obtener_orden(id_orden):
    try:
        validar_no_vacio(id_orden, "ID de Orden")
        validar_tipo(id_orden, "ID de Orden", int)
        validar_id_existente(id_orden)
        resultado = OrdenDeTrabajo.get_by_id(id_orden)
        print(f"Orden encontrada: {resultado}")
        return resultado
    except (ValueError, TypeError) as e:
        print(f"[Error de validación] {e}")
        return None
    except Exception as e:
        print(f"[Error inesperado al obtener orden] {e}")
        return None

def actualizar_orden(id_orden, fecha):
    try:
        validar_orden_de_trabajo(id_orden, fecha)
        validar_id_existente(id_orden)
        OrdenDeTrabajo.update(id_orden, fecha)
        print("Orden actualizada correctamente.")
    except (ValueError, TypeError) as e:
        print(f"[Error de validación] {e}")
    except Exception as e:
        print(f"[Error inesperado al actualizar orden] {e}")

def eliminar_orden(id_orden):
    try:
        validar_no_vacio(id_orden, "ID de Orden")
        validar_tipo(id_orden, "ID de Orden", int)
        validar_id_existente(id_orden)
        OrdenDeTrabajo.delete(id_orden)
        print("Orden eliminada correctamente.")
    except (ValueError, TypeError) as e:
        print(f"[Error de validación] {e}")
    except Exception as e:
        print(f"[Error inesperado al eliminar orden] {e}")
