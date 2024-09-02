from sqlalchemy import Column, Integer, String, DateTime, Float, Time
from app.database import Base

class SalidasDeMercancia(Base):
    __tablename__ = "SalidasDeMercanciaDetalle"

    id = Column(Integer, primary_key=True, index=True)
    NoDocumento = Column(String)
    CodigoAlterno = Column(String)
    DescripcionLarga = Column(String)
    CantidadSalida = Column(Float)
    PrecioVenta = Column(Float)
    Fecha=Column(DateTime)
