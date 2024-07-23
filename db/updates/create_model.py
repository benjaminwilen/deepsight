from sqlalchemy import create_engine, Column, Integer, String, Text, MetaData, Table, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

from config import DATABASE_URI

from schema import Base, Model

engine = create_engine(DATABASE_URI)



Base.metadata.create_all(engine, tables=[Model.__table__])
