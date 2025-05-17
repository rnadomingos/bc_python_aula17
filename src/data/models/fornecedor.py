from sqlalchemy import Column, Integer, String
from data.db import Base

class Fornecedor(Base):
    __tablename__ = 'fornecedores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(20))
    email = Column(String(100))
    endereco = Column(String(100))