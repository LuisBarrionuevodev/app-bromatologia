import mysql.connector 
from app.database.config import obtener_conexion
from app.validators.validar_contribuyente import validar_contribuyente
from app.services.contribuyente_logic import validar_cuit_existente, validar_cuit_unico
from mysql.connector import errors


class Contribuyente:
    def _init_(self,nombre,apellido,cuit,sexo):
        self.nombre= nombre
        self.apellido= apellido
        self.cuit=cuit
        self.sexo=sexo

    def create(nombre,apellido,cuit, sexo):
        try:
            validar_contribuyente(cuit,nombre,apellido,sexo)
            validar_cuit_unico(cuit)
            conn= obtener_conexion()
            cursor =conn.cursor()
            query ="INSERT INTO contribuyente(nombre,apellido,cuit,sexo) VALUES (%s,%s,%s,%s)"
            cursor.execute(query,(nombre,apellido,cuit,sexo))
            conn.commit()
            cursor.close()
            conn.close()
        except(ValueError,TypeError)as e:
            print(f"[Error de validacion] {e}")

        except errors.IntegrityError as e:
            print(f"[Error de integridad] {e}")

        except Exception as e:
            print(f"[Error inesperado] {e}")        

        
    def get_all():
        conn=obtener_conexion()
        cursor=conn.cursor(dictionary=True) #el dictionary=True es para que te devuelva un diccionario,no una tupla
        cursor.execute("SELECT * FROM contribuyente")
        resultado= cursor.fetchall()
        cursor.close()
        conn.close()
        return resultado
    
    def get_by_id(cuit):
        try:
            validar_cuit_existente(cuit)
            conn=obtener_conexion()
            cursor = conn.cursor("SELECT * FROM contribuyente WHERE cuit =%s",(cuit,))
            resultado= cursor.fetchone()
            cursor.close
            conn.close()
            return resultado
        except(ValueError,TypeError)as e:
            print(f"[Error de validacion] {e}")

        except errors.IntegrityError as e:
            print(f"[Error de integridad] {e}")

        except Exception as e:
            print(f"[Error inesperado] {e}")     
        
    def exists(cuit):
        conn= obtener_conexion()
        cursor=conn.cursor("SELECT COUNT(*) FROM contribuyente WHERE cuit =%s",(cuit,))
    
    def update (cuit,nombre,apellido,sexo):
        try:
            validar_contribuyente(cuit,nombre,apellido,sexo)
            validar_cuit_existente(cuit)
            conn= obtener_conexion()
            cursor =conn.cursor()
            query= "UPDATE contribuyente SET nombre = %s, apellido = %s, sexo=%s WHERE cuit = %s"
            cursor.execute(query,(nombre,apellido,sexo,cuit))
            conn.commit()
            cursor.close()
            conn.close()
        except(ValueError,TypeError)as e:
            print(f"[Error de validacion] {e}")

        except errors.IntegrityError as e:
            print(f"[Error de integridad] {e}")

        except Exception as e:
            print(f"[Error inesperado] {e}")         

    def delete(cuit):
        try:
            validar_cuit_existente(cuit)

            conn =obtener_conexion()
            cursor =conn.cursor()
            cursor.execute("DELETE FROM contribuyente WHERE cuit =%s",(cuit,))  
            resultado= cursor.fetchone()[0]
            cursor.close()
            conn.close()
            return resultado >0
        
        except(ValueError,TypeError)as e:
            print(f"[Error de validacion] {e}")

        except errors.IntegrityError as e:
            print(f"[Error de integridad] {e}")

        except Exception as e:
            print(f"[Error inesperado] {e}")    

            