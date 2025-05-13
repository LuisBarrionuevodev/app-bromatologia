import mysql.connector
from app.database.config import obtener_conexion


class Contribuyente:
    def _init_(self,nombre,apellido,cuit,sexo):
        self.nombre= nombre
        self.apellido= apellido
        self.cuit=cuit
        self.sexo=sexo

    def create(nombre,apellido,cuit, sexo):
        conn= obtener_conexion
            