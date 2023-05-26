from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from main import Base

# Database models

class Provincia(Base):
    __tablename__ = "api_provincia"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))

