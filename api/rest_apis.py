from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any
from enum import Enum

from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

from config.db import DATABASE_URI
from db.schema import TrainingStatus

engine = create_engine(DATABASE_URI)

metadata = MetaData()
model_table = Table('model', metadata, autoload_with=engine)
# address_table = Table('addresses', metadata, autoload_with=engine)

Session = sessionmaker(bind=engine)
session = Session()


app = FastAPI()

class NewModel(BaseModel):
    name: str
    description: str = None
    hyperparameters: Dict[str, Any]
    status: TrainingStatus

class ExistingModel(BaseModel):
    model_id: int
    name: str
    description: str = None
    hyper_params: Dict[str, Any]
    status: TrainingStatus



@app.get("/model/")
def read_models():
    query = session.query(model_table.c.id, model_table.c.name).all()
    return {model.c.id: ExistingModel.model_validate(model) for model in query}
    
@app.get("/model/{model_id}")
def read_model(model_id: int):
    return "Not implemented yet"

@app.post("/model/")
def create_model(model: NewModel):
    return "Should return model_id"

@app.put("/model/{model_id}")
def update_model(model_id: int, model: ExistingModel):
    return "Not implemented yet"

@app.delete("/model/{model_id}")
def delete_item(model_id: int):
    return "Not implemented yet"
