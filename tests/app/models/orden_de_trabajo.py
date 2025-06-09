from app.database.config import obtener_conexion

class OrdenDeTrabajo:
    def __init__(self, id_orden, fecha):
        self.id_orden = id_orden
        self.fecha = fecha
        
    def create(id_orden, fecha):
        conn = obtener_conexion()
        cursor = conn.cursor()
        query = "INSERT INTO orden_de_trabajo (id_orden, fecha) VALUES (%s, %s)"
        cursor.execute(query, (id_orden, fecha))
        conn.commit()
        cursor.close()
        conn.close()


    def get_all():
        conn = obtener_conexion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM orden_de_trabajo")
        resultado = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultado

    def get_by_id(id_orden):
        conn = obtener_conexion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM orden_de_trabajo WHERE id_orden = %s", (id_orden,))
        resultado = cursor.fetchone()
        cursor.close()
        conn.close()
        return resultado

  
    def exists(id_orden):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM orden_de_trabajo WHERE id_orden = %s", (id_orden,))
        resultado = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return resultado > 0

  
    def update(id_orden, fecha):
        conn = obtener_conexion()
        cursor = conn.cursor()
        query = "UPDATE orden_de_trabajo SET fecha = %s WHERE id_orden = %s"
        cursor.execute(query, (fecha, id_orden))
        conn.commit()
        cursor.close()
        conn.close()

 
    def delete(id_orden):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM orden_de_trabajo WHERE id_orden = %s", (id_orden,))
        conn.commit()
        cursor.close()
        conn.close()