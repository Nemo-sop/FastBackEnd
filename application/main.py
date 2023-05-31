from fastapi import FastAPI
from database.connection import startConection
from models.provincia import *
from sqlalchemy.orm import Session


# Create the FastAPI app
app = FastAPI()

# Conexion a la base de datos
Base, SessionLocal = startConection()

# Definir las rutas
from routers.localidad import *
from security.configuracion_jwt import *

@app.get("/")
def home_page():
    return {"up and running"}


# Run the application with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
