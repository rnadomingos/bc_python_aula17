from data.db import SessionLocal, engine, Base
from data.models.fornecedor import Fornecedor

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
