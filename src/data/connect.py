from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def connect():
  Base = declarative_base()
  # Create connection
  engine = create_engine('sqlite:///desafio.db', echo=True)

  Base.metadata.create_all(engine)
  Session = sessionmaker(bind=engine)
  session = Session()
  return session