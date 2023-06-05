from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional, Union
from models.usuario import Usuario
from main import SessionLocal, app

from pydantic import BaseModel

SECRET_KEY = "your-secret-key"  # Cambia esto por tu propia clave secreta
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Duración del token de acceso (en minutos)

# Configuración del contexto de cifrado de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Generar una clave secreta aleatoria
def generate_salt() -> str:
    return pwd_context.bcrypt_salt()

class User(BaseModel):
    email: str
    contrasenia: str

class SignupUser(BaseModel):
    email: str
    contrasenia: str

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(email: str):
    # Implementa la lógica para obtener el usuario de una fuente de datos (base de datos, etc.)
    # Retorna el usuario o None si no se encuentra
    db = SessionLocal()

    user = db.query(Usuario).filter(Usuario.email == email).first()

    return user

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.contrasenia):
        return False
    return user

def create_user(db, email: str, contrasenia: str):
    user = Usuario(email=email, contrasenia=contrasenia)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

class LoginData(BaseModel):
    username:str
    password:str

@app.post("/token", tags=['Usuarios'])
#async def login_for_access_token(form_data: LoginData):
async def login_for_access_token(form_data:OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

@app.get("/protected_route", tags=['Usuarios'])
async def protected_route(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication token")
        # Implementa la lógica adicional para verificar y autorizar al usuario
        return {"message": "Access granted"}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication token")
    