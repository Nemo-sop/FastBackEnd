from fastapi import Depends, HTTPException
from jose import JWTError, jwt
from models.provincia import *
from main import app, SessionLocal
from models.localidad import *
from security.configuracion_jwt import oauth2_scheme, SECRET_KEY, ALGORITHM


# Routes

# ruta para obtener un listado de todas las localidades en la bd
@app.get("/localidades", tags=["localidad"])
async def obtener_localidades(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication token")
        # Implementa la lógica adicional para verificar y autorizar al usuario
        db = SessionLocal()

        localidades = db.query(Localidad).all()

        return [localidad for localidad in localidades]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication token")
    

# ruta para obtener un listado de todas las localidades en la bd de una provincia
@app.get("/provincias/{provincia_id}/localidades", tags=["localidad"])
async def obtener_localidades(provincia_id: int, token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication token")
        # Implementa la lógica adicional para verificar y autorizar al usuario
        db = SessionLocal()

        localidades = db.query(Localidad).filter(Localidad.provincia_id == provincia_id).all()

        return [localidad for localidad in localidades]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication token")


