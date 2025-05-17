from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

SQLALCHEMY_DATA_BASE_URL = 'sqlite:///desafio.db'
engine = create_engine(SQLALCHEMY_DATA_BASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Relationship = relationship
Base = declarative_base()