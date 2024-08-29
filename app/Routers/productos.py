from fastapi import APIRouter, HTTPException
from app.database import get_connection
from app.schemas.schemasproductos import SalidaResponse

router = APIRouter()

@router.get("/Salidasmercancia", response_model=list[SalidaResponse])
def get_salidas():
    try:
        # Establecer conexión
        conn = get_connection()
        cursor = conn.cursor()
        # Ejecutar la consulta
        query = """
         SELECT  top  10 *FROM $#@$#@$#@$@$@
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        # Cerrar la conexión
        conn.close()
        # Si no hay filas, lanzar una excepción
        if not rows:
            raise HTTPException(status_code=404, detail="No records found")
        # Crear una lista de diccionarios a partir de los resultados
        results = [
            {
                "NoDocumento": row.NoDocumento,
                "FechaDeSalida": row.FechaDeSalida,
                "HoraDeSalida": row.HoraDeSalida.strftime('%H:%M:%S'),  # Convertir a string
                "TotalUtilidad": row.TotalUtilidad,
                "FechaDePedidoFactura": row.FechaDePedidoFactura
            }
            for row in rows
        ]
        return results
    except Exception as e:
        # Registrar el error y lanzar una excepción HTTP con detalles
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
