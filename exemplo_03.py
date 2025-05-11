from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///meudb.db', echo=True)

print("Conexão com SQLite estabelecida")

Base = declarative_base()

class Usuario(Base):
   __tablename__ = 'usuarios'

   id = Column(Integer, primary_key=True)
   nome = Column(String)
   idade = Column(Integer)

# Cria tabela no banco de dados
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

# Sem o With
try: 
   novo_usuario = Usuario(nome="Ana", idade=25)
   session.add(novo_usuario)
   session.commit()
except:
   session.rollback()
   raise
finally:
   session.close()

# Com o With
Session = sessionmaker(bind=engine)
session = Session()

try:
    with Session() as session:
        novo_usuario = Usuario(nome="Maria",idade=90)
        session.add(novo_usuario)
        session.commit()
        # O rollback é automaticamente chamado se uma exceção ocorrer
        # A sessão é fechada automaticamente ao sair do bloco with
except TypeError as e:
    print(e)