import os
from dotenv import load_dotenv
import pyodbc

load_dotenv()



print(f"Nombre del servidor cargado desde .env: {server}")
# Crea la cadena de conexión
conn_str = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password}'
)

def get_connection():
    try:
        # Conéctate a la base de datos
        conn = pyodbc.connect(conn_str)
        return conn
    except Exception as e:
        print(f"Error al conectar: {e}")
        raise
