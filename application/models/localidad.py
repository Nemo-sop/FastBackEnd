from sqlalchemy import Numeric, create_engine, Column, Integer, String, ForeignKey

from main import Base



class Localidad(Base):
    __tablename__ = "localidades"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    provincia_id = Column(Integer, index=True)
    centroide_lat = Column(Numeric(precision=65, scale=30))
    centroide_lon = Column(Numeric(precision=65, scale=30))
    borrado_logico = Column(bool)