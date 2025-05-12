from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Double
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .class_fornecedor import Fornecedor
from .connect import connect

Base = declarative_base()

fornecedor = Fornecedor()

class Produto():
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(200))
    preco = Column(Double(15,2))
    fornecedor_id = Column(Integer, ForeignKey('fornecedor.id'))

    fornecedor = relationship(fornecedor)

connect()

