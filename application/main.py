from fastapi import FastAPI
from database.connection import startConection
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware




# Create the FastAPI app
app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

# Conexion a la base de datos
Base, SessionLocal = startConection()

# Definir las rutas
from routers.campo import *
from routers.localidad import *
from routers.provincia import *
from routers.productor import *
from security.configuracion_jwt import *

@app.get("/")
def home_page():
    return {"up and running"}


# Run the application with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
