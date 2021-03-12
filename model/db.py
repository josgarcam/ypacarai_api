from psycopg2 import connect
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:admin@localhost:5432/paraguay_jose')
# engine = create_engine('postgresql://postgres:postgres@192.168.20.21:5432/FlotaDrones')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()