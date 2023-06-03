from fastapi import Depends, HTTPException
from jose import JWTError, jwt
from models.usuario import Usuario
from main import app, SessionLocal
from models.productor import *


# Routes

# ruta para obtener un listado de todas las localidades en la bd
@app.get("/productores", tags=["productor"])
async def obtener_productores():
    db = SessionLocal()

    productores = db.query(Productor).all()

    return [productor for productor in productores]