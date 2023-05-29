from MySQLdb import Binary
from sqlalchemy import Boolean, create_engine, Column, Integer, String, ForeignKey

from main import Base



class Persona(Base):
    __tablename__ = "personas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(30))
    apellido = Column(String(30))
    tipo_persona = Column(Integer, index=True)
    borrado_logico = Column(Boolean)