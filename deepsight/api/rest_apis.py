from typing import Dict, Any, List

from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import insert

from config.db import DATABASE_URI
from db.schema import TrainingStatus, Hyperparameter

engine = create_engine(DATABASE_URI)

metadata = MetaData()
model_table = Table("model", metadata, autoload_with=engine)
model_instance_table = Table("addresses", metadata, autoload_with=engine)
hyperparameter_table = Table()
model_hyperparameter_table = 
weights_table = 

Session = sessionmaker(bind=engine)
session = Session()


app = FastAPI()


class NewHyperparameter(BaseModel):
    """
    Used for the creation of a hyperparameter in association with a new model instance (mostly for create purposes)
    """

    name: str
    value: str
    type: str


class NewModel(BaseModel):
    """
    Represents a newly created model (mostly for create purposes)
    """

    name: str
    description: str = None


class NewModelInstance(BaseModel):
    """
    Represents a newly created model instance (mostly for create purposes)
    """

    model_id: int
    hyperparameters: List[NewHyperparameter]
    training_status: TrainingStatus


class NewWeights(BaseModel):
    """
    Represents a snapshot of a model instance's weights (mostly for create purposes)
    """

    model_instance: int
    weights: Any


class ExistingHyperparameter(BaseModel):
    """
    Used for the creation of a hyperparameter in association with a new model instance (mostly for read purposes)
    """

    hyperparameter_id: int
    name: str
    value: str
    type: str


class ExistingModel(BaseModel):
    """
    Represents a model that exists in database (mostly for read purposes)
    """

    model_id: int
    name: str
    description: str = None


class ExistingModelInstance(BaseModel):
    """
    Represents a model instance that exists in database (mostly for read purposes)
    """

    model_instance_id: int
    model_id: int
    hyperparameters: List[ExistingHyperparameter]
    training_status: TrainingStatus


class ExistingWeights(BaseModel):
    """
    Represents a snapshot of a model instance's weights (mostly for read purposes)
    """

    weights_id: int
    model_instance: int
    weights: Any


@app.get("/model/")
def read_models():
    """
    Get all models
    """

    query = session.query(model_table.c.id, model_table.c.name).all()
    return "HERE"
    return {model.c.id: ExistingModel.model_validate(model) for model in query}


@app.get("/model/{model_id}")
def read_model(model_id: int):
    return "Not implemented yet"


@app.post("/model/")
def create_model(model: NewModel):
    # See what hyper parameters aren't in storage yet
    new_hyperparameters = [
        {"name": hyperparam.name, "type": hyperparam.type}
        for hyperparam in model.hyperparameters
    ]
    stmt = (
        insert(Hyperparameter)
        .values(new_hyperparameters)
        .on_conflict_do_nothing(index_elements=["name", "type"])
    )
    session.execute(stmt)

    # Example of adding a new model with hyperparameters
    new_model = {"name": model.name, "status": model.training_status}

    # Define new hyperparameters
    hyperparam1 = Hyperparameter(name="learning_rate", value="0.01")
    hyperparam2 = Hyperparameter(name="batch_size", value="32")

    # Associate the hyperparameters with the model
    new_model.hyperparameters = [hyperparam1, hyperparam2]

    # Add the model (and implicitly the hyperparameters) to the session
    session.add(new_model)

    # Commit the session to save the data to the database
    session.commit()
    return "Should return model_id"


@app.put("/mohdel/{model_id}")
def update_model(model_id: int, model: ExistingModel):
    return "Not implemented yet"


@app.delete("/model/{model_id}")
def delete_item(model_id: int):
    return "Not implemented yet"
