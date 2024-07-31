import pytest

from sqlalchemy import create_engine, inspect

DATABASE_URI = "postgresql+psycopg2://postgres:postgres@localhost/deepsight_db"

@pytest.fixture(scope='module')
def connection():
    engine = create_engine(DATABASE_URI)
    connection = engine.connect()
    yield connection
    connection.close()

def test_tables_exist(connection):
    inspector = inspect(connection)
    expected_tables = ['user', 'model']
    existing_tables = inspector.get_table_names()

    for table in expected_tables:
        assert table in existing_tables, f"Table '{table}' does not exist in the database"