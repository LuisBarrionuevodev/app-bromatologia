import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

#esto carga el dotnev de archivo .env 
load_dotenv()



def obtener_conexion():
 try:
    conexion = mysql.connector.connect(
        host= os.getenv("DB_HOST"),
        user =os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    if conexion.is_connected():   
     return conexion
    
 except Error as e:
   print(f"[ERROR] no se pudo conectar a la base {e}")
   return None   
 