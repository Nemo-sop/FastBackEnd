from MySQLdb import Binary
from sqlalchemy import DATETIME, create_engine, Column, Integer, String, ForeignKey

from main import Base



class Sesion(Base):
    __tablename__ = "sesiones"

    id = Column(Integer, primary_key=True, index=True)
    fecha_hora_apertura = Column(DATETIME)
    fecha_hora_cierre = Column(DATETIME)
    usuario_id = Column(Integer, index=True)
    borrado_logico = Column(bool)