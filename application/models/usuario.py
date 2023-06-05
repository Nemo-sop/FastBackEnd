# from typing import Annotated, Union
from MySQLdb import Binary
from pydantic import BaseModel
from sqlalchemy import Boolean, LargeBinary, create_engine, Column, Integer, String, ForeignKey

from main import Base



class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(60))
    contrasenia = Column(String(100))
    persona_id = Column(Integer, index=True)
    borrado_logico = Column(Boolean)

"""
class Usuario(BaseModel):
    id: str
    email: str
    contrasenia: str
    persona_id: Union[int, None] = None
    disabled: Union[bool, None] = None"""