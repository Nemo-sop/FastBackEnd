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
from fastapi import HTTPException, Depends, Request
from models.usuario import *
from sqlalchemy.orm import load_only
from security.configuracion_jwt import oauth2_scheme, SECRET_KEY, ALGORITHM
from jose import JWTError, jwt
from models.productor import *
# Routes


# ruta para obtener un listado de todas los campos en la bd de un usuario


@app.get("/campos", tags=["campo"])
async def protected_obtener_campos(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        mail = payload.get("sub")
        if mail is None:
            raise HTTPException(
                status_code=401, detail="Invalid authentication token")
        # Implementa la lógica adicional para verificar y autorizar al usuario
        db = SessionLocal()

        # Obtener usuario a partir del mail
        usuario = db.query(Usuario).filter(Usuario.email == mail).first()

        # Obtener todos los campos que tenga productores asociados a id del usuario
        campos = (db.query(Campo).filter(Campo.borrado_logico == False, Campo.productor_id.in_(
            db.query(Productor.id).filter(Productor.usuario_id == usuario.id)
        ),
        ).options(load_only(
            Campo.id, Campo.nombre, Campo.localidad_id, Campo.productor_id)).all())

        return [campo for campo in campos]

    except JWTError:
        raise HTTPException(
            status_code=401, detail="Invalid authentication token")


# ruta para obtener un campo de un usuario

@app.get("/campo/{campo_id}", tags=["campo"])
async def protected_obtener_campo(campo_id: int, token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        mail = payload.get("sub")
        if mail is None:
            raise HTTPException(
                status_code=401, detail="Invalid authentication token")
        # Implementa la lógica adicional para verificar y autorizar al usuario
        db = SessionLocal()

        # Obtener usuario a partir del mail
        usuario = db.query(Usuario).filter(Usuario.email == mail).first()

        # Obtener el campo deseado
        campo = (db.query(Campo).filter(Campo.borrado_logico == False, Campo.productor_id.in_(
            db.query(Productor.id).filter(Productor.usuario_id == usuario.id)
        ),).options(
        load_only(Campo.id, Campo.nombre, Campo.localidad_id, Campo.productor_id)).filter(Campo.id == campo_id).first())

        return campo
    
    except JWTError:
        raise HTTPException(
            status_code=401, detail="Invalid authentication token")

# ruta de alta de campo


@app.post("/campoAlta", tags=["campo"])
async def protected_alta_campo(campo: CampoBase, token: str = Depends(oauth2_scheme)):
    print(campo)
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        mail = payload.get("sub")
        if mail is None:
            raise HTTPException(status_code=401, detail="Invalid authentication token")

        # Implementa la lógica adicional para verificar y autorizar al usuario
        db = SessionLocal()

        # Obtener usuario a partir del mail
        usuario = db.query(Usuario).filter(Usuario.email == mail).first()
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        # Crear una instancia de la clase Campo
        nuevo_campo = Campo(
            nombre=campo.nombre,
            localidad_id=campo.localidad_id,
            productor_id=campo.productor_id,
            borrado_logico=False
        )

        # Guardar el nuevo campo en la base de datos
        db.add(nuevo_campo)
        db.commit()
        db.refresh(nuevo_campo)

        return nuevo_campo
    
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication token")


# ...

# ruta de actualización de campo


@app.put("/campoModificar/{campo_id}", tags=["campo"])
async def actualizar_campo(campo_id: int, campo: CampoBase, token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        mail = payload.get("sub")
        if mail is None:
            raise HTTPException(status_code=401, detail="Invalid authentication token")

        # Implementa la lógica adicional para verificar y autorizar al usuario
        db = SessionLocal()
        
        # Obtener usuario a partir del mail
        usuario = db.query(Usuario).filter(Usuario.email == mail).first()
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        # Verificar si el campo existe
        campo_existente = db.query(Campo).filter(Campo.id == campo_id).first()
        if not campo_existente:
            raise HTTPException(status_code=404, detail="Campo no encontrado")
        
        # Verificar si el usuario está asociado al productor del campo
        productor = db.query(Productor).filter(Productor.id == campo_existente.productor_id).first()
        if not productor or productor.usuario_id != usuario.id:
            raise HTTPException(status_code=403, detail="No tienes permisos para modificar este campo")

        # Actualizar los atributos del campo existente
        campo_existente.nombre = campo.nombre
        campo_existente.localidad_id = campo.localidad_id
        campo_existente.productor_id = campo.productor_id

        # Guardar los cambios en la base de datos
        db.commit()
        db.refresh(campo_existente)

        return campo_existente

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication token")


# ruta de eliminación de campo
@app.delete("/campoBaja/{campo_id}", tags=["campo"])
async def eliminar_campo(campo_id: int, token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        mail = payload.get("sub")
        if mail is None:
            raise HTTPException(status_code=401, detail="Invalid authentication token")
        
        # Implementa la lógica adicional para verificar y autorizar al usuario
        db = SessionLocal()

        # Obtener usuario a partir del mail
        usuario = db.query(Usuario).filter(Usuario.email == mail).first()
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        # Verificar si el campo existe
        campo_existente = db.query(Campo).filter(Campo.id == campo_id).first()
        if not campo_existente:
            raise HTTPException(status_code=404, detail="Campo no encontrado")
        
        # Verificar si el usuario está asociado al productor del campo
        productor = db.query(Productor).filter(Productor.id == campo_existente.productor_id).first()
        if not productor or productor.usuario_id != usuario.id:
            raise HTTPException(status_code=403, detail="No tienes permisos para eliminar este campo")

        # Borrado lógico del campo
        campo_existente.borrado_logico = True

        # Guardar los cambios en la base de datos
        db.commit()

        return {"message": "Campo eliminado correctamente"}
    
    except JWTError:
        raise HTTPException

