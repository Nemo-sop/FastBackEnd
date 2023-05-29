from MySQLdb import Binary
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey

from main import Base



class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(60))
    contrasenia = Column(Binary(length=512))
    persona_id = Column(Integer, index=True)
    borrado_logico = Column(bool)