from sqlalchemy import create_engine, Column, Integer, String, ForeignKey

from main import Base



class Localidad(Base):
    __tablename__ = "api_localidad"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))
    provincia_id = Column(Integer, index=True)