from pydantic import BaseModel
from typing import Optional

class UsuarioBase(BaseModel):
    id: Optional[int]
    email: str
    contrasenia: str
    persona_id: int
    borrado_logico: bool
