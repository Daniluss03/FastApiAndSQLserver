from sqlalchemy import Column, Integer, String, DateTime, Float, Time
from app.database import Base

class SalidasDeMercancia(Base):
    __tablename__ = "SalidasDeMercancia"

    id = Column(Integer, primary_key=True, index=True)
    NoDocumento = Column(String)
    FechaDeSalida = Column(DateTime)
    HoraDeSalida = Column(Time)
    TotalUtilidad = Column(Float)
    FechaDePedidoFactura = Column(DateTime)
