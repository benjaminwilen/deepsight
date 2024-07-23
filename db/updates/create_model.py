from sqlalchemy import create_engine, Column, Integer, String, Text, MetaData, Table, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

from config.db import DATABASE_URI

from db.schema import Base, Model, Hyperparameter, ModelHyperparameter

engine = create_engine(DATABASE_URI)



Base.metadata.create_all(engine, tables=[Model.__table__, Hyperparameter.__table__, ModelHyperparameter.__table__])
