from pydantic import BaseModel
from typing import Optional

class CampoBase(BaseModel):
    id: Optional[int]
    nombre: str
    #usuario_id: int
    localidad_id: int
    productor_id: int
    borrado_logico: bool