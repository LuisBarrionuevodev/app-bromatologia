from app.validators.comunes import validar_no_vacio, validar_longitud, validar_tipo

def validar_rubro(rubro_nombre):
    validar_no_vacio(rubro_nombre, "Rubro")
    validar_tipo(rubro_nombre, "Rubro", str)
    validar_longitud(rubro_nombre, 50, "Rubro")
