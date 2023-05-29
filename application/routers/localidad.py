from main import app, SessionLocal
from models.localidad import *


# Routes

# ruta para obtener un listado de todas las localidades en la bd
@app.get("/localidades")
async def obtener_localidades():
    db = SessionLocal()

    localidades = db.query(Localidad).all()

    return {"localidades": [localidad for localidad in localidades]}

# ruta para obtener un listado de todas las localidades en la bd de una provincia
@app.get("/provincias/{provincia_id}/localidades")
async def obtener_localidades(provincia_id: int):
    db = SessionLocal()

    localidades = db.query(Localidad).filter(Localidad.provincia_id == provincia_id).all()

    return {"localidades": [localidad for localidad in localidades]}