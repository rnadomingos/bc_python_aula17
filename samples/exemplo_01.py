from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///meudb.db', echo=True)

print("Conexão com SQLite estabelecida")
