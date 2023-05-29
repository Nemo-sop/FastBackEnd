from sqlalchemy import Numeric, create_engine, Column, Integer, String, ForeignKey
from main import Base

# Database models

class Provincia(Base):
    __tablename__ = "provincias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(60))
    centroide_lat = Column(Numeric(precision=65, scale=30))
    centroide_lon = Column(Numeric(precision=65, scale=30))
    borrado_logico = Column(bool)

