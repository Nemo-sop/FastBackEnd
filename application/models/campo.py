    
from sqlalchemy import Boolean, create_engine, Column, Integer, String, ForeignKey

from main import Base



class Campo(Base):
    __tablename__ = "campos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(30))
    usuario_id = Column(Integer, index=True)
    localidad_id = Column(Integer, index=True)
    productor_id = Column(Integer, index=True)
    borrado_logico = Column(Boolean)