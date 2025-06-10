from app.validators.comunes import (
    validar_no_vacio,
    validar_longitud,
    validar_tipo
)

def validar_inspector(nr_afiliado, nombre, apellido, id_turno):
    # Número de afiliado
    validar_no_vacio(nr_afiliado, "Número de Afiliado")
    validar_tipo(nr_afiliado, "Número de Afiliado", int)
    validar_longitud(nr_afiliado, 5, "Número de Afiliado")

    # Nombre
    validar_no_vacio(nombre, "Nombre")
    validar_tipo(nombre, "Nombre", str)
    validar_longitud(nombre, 100, "Nombre")

    # Apellido
    validar_no_vacio(apellido, "Apellido")
    validar_tipo(apellido, "Apellido", str)
    validar_longitud(apellido, 100, "Apellido")

    # ID Turno
    validar_no_vacio(id_turno, "ID Turno")
    validar_tipo(id_turno, "ID Turno", int)
    if id_turno not in [1, 2]:
        raise ValueError("El turno debe ser 1 (mañana) o 2 (tarde)")