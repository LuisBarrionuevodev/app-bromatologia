from app.validators.comunes import validar_cuit,validar_fecha,validar_longitud,validar_no_vacio,validar_opcion_en_lista,validar_tipo


def validar_domicilio(calle,numero,detalle=None):
  
   #validando calle
   validar_no_vacio(calle,"Calle")
   validar_tipo(calle,"Calle",str)
   validar_longitud(calle,255,"Calle")

   #validando numero
   validar_no_vacio(numero,"Numero")
   validar_tipo(numero,"Numero",int)
   validar_longitud(numero,10,"Numero")

   #validando detalle
   if detalle:
     validar_tipo(detalle,"Detalle",str)
     validar_longitud(detalle,255,"Detalle")

   
      