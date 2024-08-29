from pydantic import BaseModel
from datetime import datetime

class SalidaResponse(BaseModel):
    NoDocumento: str
    FechaDeSalida: datetime
    HoraDeSalida: str
    TotalUtilidad: float
    FechaDePedidoFactura: datetime

    class Config:
        orm_mode = True
