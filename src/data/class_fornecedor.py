from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from .connect import connect


Base = declarative_base()

class Fornecedor(Base):
    __tablename__ = 'fornecedores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(20))
    email= Column(String(100))
    endereco = Column(String(100))

connect()