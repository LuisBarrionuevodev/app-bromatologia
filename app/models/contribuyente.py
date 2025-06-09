from app.database.config import obtener_conexion

class Contribuyente:
    def _init_(self,nombre,apellido,cuit,sexo):
        self.nombre= nombre
        self.apellido= apellido
        self.cuit=cuit
        self.sexo=sexo

    def create(nombre,apellido,cuit, sexo):
            conn= obtener_conexion()
            cursor =conn.cursor()
            query ="INSERT INTO contribuyente(nombre,apellido,cuit,sexo) VALUES (%s,%s,%s,%s)"
            cursor.execute(query,(nombre,apellido,cuit,sexo))
            conn.commit()
            cursor.close()
            conn.close()
        
    def get_all():
        conn=obtener_conexion()
        cursor=conn.cursor(dictionary=True) #el dictionary=True es para que te devuelva un diccionario,no una tupla
        cursor.execute("SELECT * FROM contribuyente")
        resultado= cursor.fetchall()
        cursor.close()
        conn.close()
        return resultado
    
    def get_by_cuit(cuit):
            conn=obtener_conexion()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM contribuyente WHERE cuit =%s",(cuit,))
            resultado= cursor.fetchone()
            cursor.close()
            conn.close()
            return resultado   
        
    def exists(cuit):
        conn= obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM contribuyente WHERE cuit = %s", (cuit,))
        resultado = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return resultado > 0
    
    def update (cuit,nombre,apellido,sexo):
            conn= obtener_conexion()
            cursor =conn.cursor()
            query= "UPDATE contribuyente SET nombre = %s, apellido = %s, sexo=%s WHERE cuit = %s"
            cursor.execute(query,(nombre,apellido,sexo,cuit))
            conn.commit()
            cursor.close()
            conn.close()      
    def delete(cuit):
            conn =obtener_conexion()
            cursor =conn.cursor()
            cursor.execute("DELETE FROM contribuyente WHERE cuit =%s",(cuit,))  
            conn.commit()
            cursor.close()
            conn.close()
           

            