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

novo_usuario = Usuario(nome='João', idade=20)
session.add(novo_usuario)
session.commit()

print("Usuario inserido com sucesso")


# O atributo .all() retorna o dado com dict, por isso precisa ser listado por um laço
usuario = session.query(Usuario).filter_by(nome="João").all()

for usr in usuario:
  print(f"Usuario encontrado: {usr.nome}, Idade: {usr.idade}")


# O atributo .fist() retorna um unico registro
usuario = session.query(Usuario).filter_by(nome="João").first()
print(f"Usuario encontrado: {usr.nome}, Idade: {usr.idade}")
