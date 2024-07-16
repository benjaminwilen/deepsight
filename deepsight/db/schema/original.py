from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DATABASE_URL = "postgresql+psycopg2://root:webelieve@localhost/deepsight_db"
MAX_USERNAME_PASSWORD_LEN = 20

engine = create_engine(DATABASE_URL)


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(MAX_USERNAME_PASSWORD_LEN), unique=True, nullable=False)
    password = Column(String(MAX_USERNAME_PASSWORD_LEN), nullable=False)

    model_relationship = relationship('Model', back_populates='user')

# Create the table
Base.metadata.create_all(engine)