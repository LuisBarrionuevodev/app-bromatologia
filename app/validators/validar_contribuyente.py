from app.validators.comunes import validar_no_vacio, validar_longitud, validar_tipo, validar_fecha,validar_cuit,validar_opcion_en_lista


def validar_contribuyente(cuit,nombre,apellido,sexo):
    #Cuit
    validar_no_vacio(cuit,"CUIT")
    validar_tipo(cuit,"CUIT",str)
    validar_cuit(cuit)

    #nombre
    validar_no_vacio(nombre,"Nombre")
    validar_longitud(nombre,100,"Nombre")
    validar_tipo(nombre,"Nombre",str)

    #apellido
    validar_no_vacio(apellido,"Apellido")
    validar_longitud(apellido,100,"Apellido")
    validar_tipo(apellido,"Apellido",str)

    #sexo
    opciones_validas = ["hombre", "mujer", "no binario"]
    validar_opcion_en_lista(sexo,opciones_validas,"Sexo")



