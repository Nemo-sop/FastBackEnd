"""
CAMPOS

http://127.0.0.1:8000/api/campoList/

Devuelve un listado de todos los objetos del tipo campo de la BD en formato tipo JSON

http://127.0.0.1:8000/api/campoAlta/

Permite enviar un metodo POST para crear un campo y guardarlo en la BD, requiere que se le envie en formato JSON, nombre, id de provincia, id de localidad, id de productor

http://127.0.0.1:8000/api/campoConsulta/<int>/

Devuelve todos los datos sobre el campo que tenga un pk=<int> en formato JSON
"""

from application.models.campo import Campo
from main import app, SessionLocal
from models.localidad import *

# Routes

# ruta para obtener un listado de todas los campos en la bd de un usuario
@app.get("/campos/{usuario_id}", tags=["campo"])
async def obtener_campos(usuario_id: int):
    db = SessionLocal()

    campos = db.query(Campo).filter(Campo.usuario_id == usuario_id).all()

    return {"campos": [campo for campo in campos]}

# ruta para obtener un listado de todas las localidades en la bd de una provincia
@app.get("/campos/{usuario_id}/{campo_id}", tags=["campo"])
async def obtener_campo(usuario_id: int, campo_id: int):
    db = SessionLocal()

    campos = db.query(Campo).filter(Campo.usuario_id == usuario_id).filter(Campo.id == campo_id).first()

    return {"campos": [campo for campo in campos]}