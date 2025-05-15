
from datetime import datetime
def validar_no_vacio(valor,campo):
    if not valor:
        raise ValueError(f"El campo {campo} no puede estar vacio")
    

def validar_tipo (valor,campo,dato_correcto):
    if not isinstance(valor,dato_correcto):
        raise TypeError(f"El campo {campo} de ser de tipo {dato_correcto}")
    
def validar_longitud(valor,max_length,campo):
    if len(str(valor))>max_length:
        raise ValueError(f"La longitud del campo {campo} debe contener {max_length} caracteres ") 
     
def validar_cuit(valor):
    if len(valor)!=11:
        raise ValueError("El cuit debe contener 11 digitos")
def validar_fecha(fecha,formato="%Y-%m-%d"):  
   try: 
    return datetime.strptime(fecha,formato)
   except:
       raise ValueError(f"La fecha {fecha} no es valida o no tiene el formato {formato}") 