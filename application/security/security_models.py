from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str


class User(BaseModel):
    # Clase de Usuario unicamente usada en el tema de autenticacion
    id: int
    email: str
    persona_id: int
    borrado_logico: bool


class UserInDB(User):
    contrasenia: str