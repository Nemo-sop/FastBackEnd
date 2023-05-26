from main import app, SessionLocal
from models.localidad import *


# Routes

@app.get("/provincias/{provincia_id}/localidades")
async def obtener_localidades(provincia_id: int):
    db = SessionLocal()

    localidades = db.query(Localidad).filter(Localidad.provincia_id == provincia_id).all()

    return {"localidades": [localidad for localidad in localidades]}