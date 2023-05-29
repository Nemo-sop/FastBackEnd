from sqlalchemy import Boolean, create_engine, Column, Integer, String, ForeignKey

from main import Base



class Productor(Base):
    __tablename__ = "productores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(60))
    apellido = Column(String(60))
    cuit_cuil = Column(String(13))
    email = Column(String(60))
    referencia = Column(String(100))
    borrado_logico = Column(Boolean)