from pydantic import BaseModel
from datetime import datetime

class SalidaResponse(BaseModel):
    NoDocumento: str
    CodigoAlterno: str
    DescripcionLarga: str
    CantidadSalida:float
    PrecioVenta: float
    Fecha: datetime

    class Config:
        orm_mode = True
