import pyodbc
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configura los detalles de conexión
server = os.getenv("DB_SERVER")
database = os.getenv("DB_DATABASE")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")


# Crea la cadena de conexión
conn_str = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password}'
)

try:
    # Conéctate a la base de datos
    conn = pyodbc.connect(conn_str)
    print("Conexión exitosa.")
    
    cursor = conn.cursor()
    # Ejecutar una consulta básica
    cursor.execute("SELECT  top  10 *FROM SalidasDeMercancia")
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
    
    conn.close()
except Exception as e:
    print(f"Error al conectar: {e}")
