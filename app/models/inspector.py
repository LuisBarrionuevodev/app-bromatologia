from app.database.config import obtener_conexion

class Inspector:
    def create(nr_afiliado,nombre, apellido, id_turno):
        conn = obtener_conexion()
        cursor = conn.cursor()
        query = """
            INSERT INTO inspector (nr_afiliado,nombre, apellido, id_turno)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (nr_afiliado,nombre, apellido, id_turno))
        conn.commit()
        cursor.close()
        conn.close()

    def get_all():
        conn = obtener_conexion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM inspector")
        resultado = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultado

    def get_by_id(nr_afiliado):
        conn = obtener_conexion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM inspector WHERE nr_afiliado = %s", (nr_afiliado,))
        resultado = cursor.fetchone()
        cursor.close()
        conn.close()
        return resultado

    def exists(nr_afiliado):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM inspector WHERE nr_afiliado = %s", (nr_afiliado,))
        resultado = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return resultado > 0

    def update(nr_afiliado, nombre, apellido, id_turno):
        conn = obtener_conexion()
        cursor = conn.cursor()
        query = """
            UPDATE inspector
            SET nombre = %s, apellido = %s, id_turno = %s
            WHERE nr_afiliado = %s
        """
        cursor.execute(query, (nombre, apellido, id_turno, nr_afiliado))
        conn.commit()
        cursor.close()
        conn.close()

    def delete(nr_afiliado):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM inspector WHERE nr_afiliado = %s", (nr_afiliado,))
        conn.commit()
        cursor.close()
        conn.close()
