from sqlalchemy import Column, Integer, String, ForeignKey, Double
from data.db import Base, Relationship

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(200))
    preco = Column(Double(15,2))
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))

    fornecedor = Relationship("Fornecedor")
