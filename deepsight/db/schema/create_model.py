from sqlalchemy import create_engine, Column, Integer, String, Text, MetaData, Table, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

from original import Base, User, DATABASE_URL, MAX_USERNAME_PASSWORD_LEN

engine = create_engine(DATABASE_URL)


class Model(Base):
    __tablename__ = 'model'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    user_relationship = relationship('User', back_populates='model')

# Create the table
Base.metadata.create_all(engine)