from main import app, SessionLocal
from models.productor import *
from models.usuario import Usuario
from fastapi import Depends, HTTPException
from security.configuracion_jwt import oauth2_scheme, SECRET_KEY, ALGORITHM
from jose import JWTError, jwt
# Routes

# ruta para obtener un listado de todas las localidades en la bd

@app.get("/productores", tags=['productor'])
async def protected_obtener_productores(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        mail = payload.get("sub")
        if mail is None:
            raise HTTPException(status_code=401, detail="Invalid authentication token")
        # Implementa la lógica adicional para verificar y autorizar al usuario
        db = SessionLocal()

        usuario = db.query(Usuario).filter(Usuario.email == mail).first()

        return {"message": "Access granted"}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication token")

