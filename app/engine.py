from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///mydatabase.db', echo=True)
Session = sessionmaker(engine, expire_on_commit=False)
api = FastAPI()
Base = declarative_base()
