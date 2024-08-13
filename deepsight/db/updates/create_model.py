from sqlalchemy import create_engine

from deepsight.config.db import DATABASE_URI

from deepsight.db.schema import (
    Base,
    Model,
    Hyperparameter,
    ModelHyperparameter,
    ModelInstance,
)

engine = create_engine(DATABASE_URI)


Base.metadata.create_all(
    engine,
    tables=[
        Model.__table__,
        Hyperparameter.__table__,
        ModelInstance.__table__,
        ModelHyperparameter.__table__,
    ],
)
