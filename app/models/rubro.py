from app.database.config import obtener_conexion

class Rubro:
    def get_all():
        conn = obtener_conexion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM rubro")
        resultado = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultado

    def get_by_id(id_rubro):
        conn = obtener_conexion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM rubro WHERE id_rubro = %s", (id_rubro,))
        resultado = cursor.fetchone()
        cursor.close()
        conn.close()
        return resultado

    def exists(id_rubro):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM rubro WHERE id_rubro = %s", (id_rubro,))
        resultado = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return resultado > 0


    def get_by_nombre(rubro_nombre):
        conn = obtener_conexion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM rubro WHERE nombre = %s", (rubro_nombre,))
        resultado = cursor.fetchone()
        cursor.close()
        conn.close()
        return resultado

    def exists_by_nombre(rubro_nombre):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM rubro WHERE nombre = %s", (rubro_nombre,))
        resultado = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return resultado > 0
