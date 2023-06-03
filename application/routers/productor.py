from fastapi import Depends, HTTPException
from jose import JWTError, jwt
from models.usuario import Usuario
from main import app, SessionLocal
from models.productor import *
from security.configuracion_jwt import oauth2_scheme, SECRET_KEY, ALGORITHM


# Routes

# ruta para obtener un listado de todas las localidades en la bd
@app.get("/productores", tags=["productor"])
async def protected_obtener_productores(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        mail = payload.get("sub")
        if mail is None:
            raise HTTPException(status_code=401, detail="Invalid authentication token")
        # Implementa la lógica adicional para verificar y autorizar al usuario
        db = SessionLocal()


        # Obtener usuario a partir del mail
        usuario = db.query(Usuario).filter(Usuario.email == mail).first()

        # Obtener todos los productores que tengan en su campo usuario_id == al ide del usuario
        productores_de_usuario = db.query(Productor).filter(Productor.usuario_id == usuario.id)
        

        return [productor for productor in productores_de_usuario]
    
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication token")

