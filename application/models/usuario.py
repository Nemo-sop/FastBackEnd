from typing import Annotated, Union
from MySQLdb import Binary
from pydantic import BaseModel
from sqlalchemy import Boolean, LargeBinary, create_engine, Column, Integer, String, ForeignKey

from main import Base



class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(60))
    contrasenia = Column(LargeBinary)
    persona_id = Column(Integer, index=True)
    borrado_logico = Column(Boolean)

"""
class Usuario(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None"""