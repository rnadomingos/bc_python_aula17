from data.db import SessionLocal, engine, Base
from data.models.fornecedor import Fornecedor
from data.models.produto import Produto

Base.metadata.create_all(bind=engine)

def add_fornecedor_to_db() -> Fornecedor:
    with SessionLocal() as db:
        db_fornecedor = Fornecedor(
            nome="OCS", 
            telefone="12345678", 
            email="japa@ocs.com", 
            endereco="Butantã"   
            )
        db.add(db_fornecedor)
        db.commit()
        db.refresh(db_fornecedor)
    return db_fornecedor

def add_produto_to_db() -> Produto:
    with SessionLocal() as db:
        db_produto = Produto(
            nome="Produto 2", 
            descricao="Descrição do Produto 2", 
            preco=100, 
            fornecedor_id=1
            )
        db.add(db_produto)
        db.commit()
        db.refresh(db_produto)
    return db_produto