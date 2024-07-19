from sqlalchemy.orm import declarative_base

Base = declarative_base()

DATABASE_URI = "postgresql+psycopg2://postgres:postgres@localhost/deepsight_db"
MAX_USERNAME_PASSWORD_LEN = 20
