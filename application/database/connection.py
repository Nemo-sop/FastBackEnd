from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Database connection
def startConection():
    DATABASE_URL = "mysql://administrador:Grupo52023proyecto@proyecto-final-mysql.mysql.database.azure.com/proyecto_agro"
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
    return Base, SessionLocal