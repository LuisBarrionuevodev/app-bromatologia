from app.database.config import obtener_conexion



class Contribuyente:
    def _init_(self,calle,numero,detalle=None):
        self.calle=calle
        self.numero=numero
        self.detalle=detalle


    def create(calle,numero,detalle=None):
        conn= obtener_conexion()
        cursor= conn.cursor()
        query="INSERT INTO domicilio(calle,numero,detalle) VALUES (%s,%s,%s,%s)"
        cursor.execute(query,(calle,numero,detalle))    
        conn.commit()
        cursor.close()
        conn.close()

    def get_all():
        conn=obtener_conexion()
        cursor=conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM contribuyente")
        resultado = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultado

    def get_by_id(id):
        conn=obtener_conexion()
        cursor=conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM domicilio WHERE id=%s",(id,))
        resultado=cursor.fetchone()
        cursor.close()
        conn.close()
        return resultado
    
    def exist (id):
        conn=obtener_conexion()
        cursor= conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM domicilio WHERE id=%s",(id))
        resultado= cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return resultado > 0
    
    def update(id,calle,numero,detalle=None):
        conn=obtener_conexion()
        cursor=conn.cursor()
        query= "UPDATE domicilio SET calle =%s, numero=%s, detalle=%s WHERE id =%s"
        cursor.execute(query,(calle,numero,detalle,id))
        conn.commit()
        cursor.close()
        conn.close()

    def delete(id):
        conn= obtener_conexion()
        cursor= conn.cursor()
        cursor.execute("DELETE FROM domicilio WHERE id =%s",(id,))  
        conn.commit()
        cursor.close()
        conn.close()  

