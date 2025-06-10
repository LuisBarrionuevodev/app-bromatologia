from app.models.inspector import Inspector
from app.validators.validar_inspector import validar_inspector
from app.validators.comunes import validar_no_vacio, validar_tipo
from mysql.connector import errors

def validar_afiliado_unico(nr_afiliado):
    if Inspector.exists(nr_afiliado):
        raise ValueError(f"El número de afiliado {nr_afiliado} ya está registrado.")

def validar_afiliado_existente(nr_afiliado):
    if not Inspector.exists(nr_afiliado):
        raise ValueError(f"El número de afiliado {nr_afiliado} no existe en la base de datos.")

def crear_inspector(nr_afiliado, nombre, apellido, id_turno):
    try:
        validar_inspector(nr_afiliado, nombre, apellido, id_turno)
        validar_afiliado_unico(nr_afiliado)
        Inspector.create(nr_afiliado, nombre, apellido, id_turno)
        print("Inspector creado correctamente.")
    except (ValueError, TypeError) as e:
        print(f"[Error de validación] {e}")
    except Exception as e:
        print(f"[Error inesperado] {e}")

def obtener_inspector(nr_afiliado):
    try:
        validar_no_vacio(nr_afiliado, "Número de Afiliado")
        validar_tipo(nr_afiliado, "Número de Afiliado", int)
        validar_afiliado_existente(nr_afiliado)
        resultado = Inspector.get_by_id(nr_afiliado)
        print(f"Inspector encontrado: {resultado}")
        return resultado
    except (ValueError, TypeError) as e:
        print(f"[Error de validación] {e}")
        return None
    except Exception as e:
        print(f"[Error inesperado al obtener inspector] {e}")
        return None

def actualizar_inspector(nr_afiliado, nombre, apellido, id_turno):
    try:
        validar_inspector(nr_afiliado, nombre, apellido, id_turno)
        validar_afiliado_existente(nr_afiliado)
        Inspector.update(nr_afiliado, nombre, apellido, id_turno)
        print("Inspector actualizado correctamente.")
    except (ValueError, TypeError) as e:
        print(f"[Error de validación] {e}")
    except Exception as e:
        print(f"[Error inesperado al actualizar inspector] {e}")

def eliminar_inspector(nr_afiliado):
    try:
        validar_no_vacio(nr_afiliado, "Número de Afiliado")
        validar_tipo(nr_afiliado, "Número de Afiliado", int)
        validar_afiliado_existente(nr_afiliado)
        Inspector.delete(nr_afiliado)
        print("Inspector eliminado correctamente.")
    except (ValueError, TypeError) as e:
        print(f"[Error de validación] {e}")
    except Exception as e:
        print(f"[Error inesperado al eliminar inspector] {e}")