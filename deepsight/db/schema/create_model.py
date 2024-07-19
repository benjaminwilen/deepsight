from sqlalchemy import create_engine, Column, Integer, String, Text, MetaData, Table, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

from config import Base, DATABASE_URI
from schema.create_user import User


engine = create_engine(DATABASE_URI)


class Model(Base):
    __tablename__ = 'model'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    user_relationship = relationship('User', back_populates='model')

# Create the table
Base.metadata.create_all(engine)