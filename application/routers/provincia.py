from fastapi import Depends, HTTPException
from jose import JWTError, jwt
from models.provincia import *
from main import app, SessionLocal
from security.configuracion_jwt import oauth2_scheme, SECRET_KEY, ALGORITHM


# Routes

# ruta para obtener un listado de todas las provincias en la bd
@app.get("/provincias", tags=["provincia"])
async def obtener_provincias(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication token")
        # Implementa la lógica adicional para verificar y autorizar al usuario
        db = SessionLocal()

        provincias = db.query(Provincia).all()

        return [provincia for provincia in provincias]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication token")
    