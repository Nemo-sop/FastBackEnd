from models.provincia import *
from main import app, SessionLocal


# Routes

# ruta para obtener un listado de todas las provincias en la bd
@app.get("/provincias", tags=["provincia"])
async def obtener_provincias():
    db = SessionLocal()

    provincias = db.query(Provincia).all()

    return {"provincias": [provincia for provincia in provincias]}