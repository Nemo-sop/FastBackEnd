from MySQLdb import Binary
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean

from main import Base



class Tipo_Persona(Base):
    __tablename__ = "tipos_persona"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(30))
    borrado_logico = Column(Boolean)