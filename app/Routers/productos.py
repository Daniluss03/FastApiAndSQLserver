from fastapi import APIRouter, HTTPException, Depends
from app.database import get_connection
from app.schemas.schemasproductos import SalidaResponse
from fastapi.security import APIKeyHeader
from dotenv import load_dotenv
import os
import pyodbc

load_dotenv()

API_KEY = os.getenv("API_KEY")
api_key_header = APIKeyHeader(name="X-API-KEY")

def verify_api(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Could not validate the API KEY")
    return api_key

router = APIRouter()

@router.get("/Salidasmercancia", response_model=list[SalidaResponse])
async def get_salidas(api_key: str = Depends(verify_api,SalidaResponse.Fecha)):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
         SELECT TOP 10 * FROM SalidasDeMercancia
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            raise HTTPException(status_code=404, detail="No records found")

        results = [
            {
                "NoDocumento": row.NoDocumento,
                "CodigoAlterno": row.CodigoAlterno,
                "DescripcionLarga": row.DescripcionLarga,
                "CantidadSalida": row.CantidadSalida,
                "PrecioVenta": row.PrecioVenta,
                "Fecha":row.Fecha.strft('%H:%M:%S'),
            }
            for row in rows
        ]
        return results
    
    except pyodbc.InterfaceError:
        raise HTTPException(
            status_code=500,
            detail="Database connection error: Could not establish a connection to SQL Server. Check server address and configuration."
        )
    except pyodbc.DatabaseError:
        raise HTTPException(
            status_code=500,
            detail="Database query error: An error occurred while querying the database. Check the query and database status."
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An unexpected error occurred: {e}"
        )
