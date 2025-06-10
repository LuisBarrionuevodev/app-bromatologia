from app.models.rubro import Rubro
from app.validators.validar_rubro import validar_rubro
from app.validators.comunes import validar_no_vacio, validar_tipo, validar_longitud

# Validaciones lógicas
def validar_rubro_existente_por_nombre(nombre):
    if not Rubro.exists_by_nombre(nombre):
        raise ValueError(f"El rubro '{nombre}' no existe.")

def validar_rubro_unico_por_nombre(nombre):
    if Rubro.exists_by_nombre(nombre):
        raise ValueError(f"El rubro '{nombre}' ya está registrado.")

# Crear
def crear_rubro(nombre):
    try:
        validar_rubro(nombre)
        validar_rubro_unico_por_nombre(nombre)
        Rubro.create(nombre)
        print("✅ Rubro creado correctamente.")
    except (ValueError, TypeError) as e:
        print(f"[Error de validación] {e}")
    except Exception as e:
        print(f"[Error inesperado al crear rubro] {e}")

# Obtener
def obtener_rubro_por_nombre(nombre):
    try:
        validar_no_vacio(nombre, "Rubro")
        validar_tipo(nombre, "Rubro", str)
        validar_rubro_existente_por_nombre(nombre)
        resultado = Rubro.get_by_nombre(nombre)
        print(f"✅ Rubro encontrado: {resultado}")
        return resultado
    except (ValueError, TypeError) as e:
        print(f"[Error de validación] {e}")
        return None
    except Exception as e:
        print(f"[Error inesperado al obtener rubro] {e}")
        return None

# Obtener todos (para dropdown, combos, etc.)
def obtener_todos_los_rubros():
    try:
        return Rubro.get_all()
    except Exception as e:
        print(f"[Error al listar rubros] {e}")
        return []
