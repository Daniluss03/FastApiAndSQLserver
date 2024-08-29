import pyodbc



# Configura los detalles de conexión
server = ''
database = ''
username = ''
password = ''

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
    print(conn)
    cursor = conn.cursor()
    #ahora un query basico
    c=cursor.execute("SELECT * FROM '' ")
    print("Conexión exitosa.")
    print(c)
    conn.close()
except Exception as e:
    print(f"Error al conectar: {e}")