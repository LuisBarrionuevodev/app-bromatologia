from app.validators.comunes import validar_no_vacio, validar_longitud, validar_tipo, validar_fecha

def validar_orden_de_trabajo(id_orden, fecha):
    # ID de la orden
    validar_no_vacio(id_orden, "ID de Orden")
    validar_tipo(id_orden, "ID de Orden", int)
    validar_longitud(id_orden, 6, "ID de Orden")  
    # Fecha
    validar_no_vacio(fecha, "Fecha")
    validar_fecha(fecha, "%Y-%m-%d")