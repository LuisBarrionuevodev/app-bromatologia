import sys
import os

# Aseguramos que la raíz del proyecto esté en sys.path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from app.services.contribuyente_logica import (
    crear_contribuyente,
    obtener_contribuyente,
    actualizar_contribuyente,
    eliminar_contribuyente
)

def test_create():
    crear_contribuyente(
        nombre="Luis",
        apellido="Barrionuevo",
        cuit="20123456789",
        sexo="MASCULINO"
    )

def test_get():
    obtener_contribuyente("20123456789")

def test_update():
    actualizar_contribuyente(
        nombre="Luisito",
        apellido="Barrionuevo",
        cuit="20123456789",
        sexo="NO BINARIO"
    )

def test_delete():
    eliminar_contribuyente("20123456789")

if __name__ == "__main__":
    test_create()
    test_get()
    test_update()
    test_get()
    test_delete()
    test_get()  # Para verificar que fue eliminado

