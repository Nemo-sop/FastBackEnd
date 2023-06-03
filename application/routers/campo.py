"""
CAMPOS

http://127.0.0.1:8000/api/campoList/

Devuelve un listado de todos los objetos del tipo campo de la BD en formato tipo JSON

http://127.0.0.1:8000/api/campoAlta/

Permite enviar un metodo POST para crear un campo y guardarlo en la BD, requiere que se le envie en formato JSON, nombre, id de provincia, id de localidad, id de productor

http://127.0.0.1:8000/api/campoConsulta/<int>/

Devuelve todos los datos sobre el campo que tenga un pk=<int> en formato JSON
"""

from models.campo import *
from main import app, SessionLocal
from models.localidad import *
from schemas.campo import *
from fastapi import HTTPException
from models.usuario import *
# Routes

# ruta para obtener un listado de todas los campos en la bd de un usuario
@app.get("/campos/{usuario_id}", tags=["campo"])
async def obtener_campos(usuario_id: int):
    db = SessionLocal()

    campos = db.query(Campo).filter(Campo.usuario_id == usuario_id).all()

    return [campo for campo in campos]

# ruta para obtener un campo de un usuario
@app.get("/campos/{usuario_id}/{campo_id}", tags=["campo"])
async def obtener_campo(usuario_id: int, campo_id: int):
    db = SessionLocal()

    campos = db.query(Campo).filter(Campo.usuario_id == usuario_id).filter(Campo.id == campo_id).first()

    return [campo for campo in campos]

# ruta de alta de campo
@app.post("/campoAlta/{usuario_id}", tags=["campo"])
async def alta_campo(usuario_id: int, campo: CampoBase):
     print(campo)
     db = SessionLocal()

     # Verificar si el usuario existe
     usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
     if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

     # Crear una instancia de la clase Campo
     nuevo_campo = Campo(
        nombre=campo.nombre,
        usuario_id=usuario_id,
        localidad_id=campo.localidad_id,
        productor_id=campo.productor_id,
        borrado_logico=False
    )

     # Guardar el nuevo campo en la base de datos
     db.add(nuevo_campo)
     db.commit()
     db.refresh(nuevo_campo)

     return nuevo_campo
     
# ...

# ruta de actualización de campo
@app.put("/campoModificar/{usuario_id}/{campo_id}", tags=["campo"])
async def actualizar_campo(campo_id: int, campo: CampoBase):
    db = SessionLocal()

    # Verificar si el campo existe
    campo_existente = db.query(Campo).filter(Campo.id == campo_id).first()
    if not campo_existente:
        raise HTTPException(status_code=404, detail="Campo no encontrado")

    # Actualizar los atributos del campo existente
    campo_existente.nombre = campo.nombre
    campo_existente.localidad_id = campo.localidad_id
    campo_existente.productor_id = campo.productor_id

    # Guardar los cambios en la base de datos
    db.commit()
    db.refresh(campo_existente)

    return campo_existente


# ruta de eliminación de campo
@app.delete("/campoBaja/{usuario_id}/{campo_id}", tags=["campo"])
async def eliminar_campo(campo_id: int):
    db = SessionLocal()

    # Verificar si el campo existe
    campo_existente = db.query(Campo).filter(Campo.id == campo_id).first()
    if not campo_existente:
        raise HTTPException(status_code=404, detail="Campo no encontrado")

    # Borrado lógico del campo
    campo_existente.borrado_logico = True

    # Guardar los cambios en la base de datos
    db.commit()

    return {"message": "Campo eliminado correctamente"}
    