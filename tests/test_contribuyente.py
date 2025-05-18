import sys
import os

# Agregar la carpeta raíz del proyecto al sys.path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# ⚠️ Cambiar "modelo" por el nombre real de tu clase
from app.models.contribuyente import Contribuyente


def test_create():
    try:
        Contribuyente.create(
            nombre="Luis",
            apellido="Barrionuevo",
            cuit="20123456789",
            sexo="hombre"
        )
        print("✅ Contribuyente creado correctamente.")
    except Exception as e:
        print(f"❌ Error en create(): {e}")


def test_get():
    try:
        result = Contribuyente.get_by_cuit("20123456789")
        if result:
            print("✅ get_by_cuit() correcto:", result)
        else:
            print("❌ CUIT no encontrado.")
    except Exception as e:
        print(f"❌ Error en get(): {e}")


def test_update():
    try:
        Contribuyente.update(
            cuit="20123456789",
            nombre="Luisito",
            apellido="Barrionuevo",
            sexo="no binario"
        )
        print("✅ Contribuyente actualizado correctamente.")
    except Exception as e:
        print(f"❌ Error en update(): {e}")


def test_delete():
    try:
        Contribuyente.delete("20123456789")
        print("✅ Contribuyente eliminado correctamente.")
    except Exception as e:
        print(f"❌ Error en delete(): {e}")


if __name__ == "__main__":
    test_create()
    test_get()
    test_update()
    test_delete()
