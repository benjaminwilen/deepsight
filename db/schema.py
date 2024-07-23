from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Text, MetaData, Table, ForeignKey

Base = declarative_base()

class Model(Base):
    __tablename__ = 'model'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)
    status = #TODO: start here, finish schema, check postman API

    user_relationship = relationship('User', back_populates='model')