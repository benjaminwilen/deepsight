import enum

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey,
    Boolean,
    Enum,
    DateTime,
    func,
    UniqueConstraint,
)

from sqlalchemy.dialects.postgresql import JSONB

Base = declarative_base()


class TrainingStatus(enum.Enum):
    TRAINING = "training"
    FAILED = "failing"
    COMPLETE = "complete"


class Model(Base):
    __tablename__ = "model"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)
    description = Column(Text)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, default=func.now(), onupdate=func.now(), nullable=False
    )

    instances = relationship("ModelInstance", back_populates="model")


class ModelInstance(Base):
    __tablename__ = "model_instance"
    id = Column(Integer, primary_key=True, autoincrement=True)
    model_id = Column(Integer, ForeignKey("model.id"))
    training_status = Column(Enum(TrainingStatus), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)

    model = relationship("Model", back_populates="instances")
    hyperparameters = relationship(
        "ModelHyperparameter", back_populates="model_instance"
    )


class Hyperparameter(Base):
    __tablename__ = "hyperparameter"
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    type = Column(Text, nullable=False)

    model_instances = relationship(
        "ModelHyperparameter", back_populates="hyperparameter"
    )
    __table_args__ = (UniqueConstraint("name", "type", name="_hyperparameter_uc"),)


class ModelHyperparameter(Base):
    __tablename__ = "model_hyperparameter"
    id = Column(Integer, primary_key=True, autoincrement=True)
    model_id = Column(Integer, ForeignKey("model.id"))
    hyperparameter_id = Column(Integer, ForeignKey("hyperparameter.id"))
    value = Column(Text, nullable=False)

    model_instance = relationship("ModelInstance", back_populates="hyperparameters")
    hyperparameter = relationship("Hyperparameter", back_populates="model_instances")

    __table_args__ = (
        UniqueConstraint(
            "model_id", "hyperparameter_id", name="uix_model_hyperparameter"
        ),
    )


class Weights(Base):
    __tablename__ = "weights"
    id = Column(Integer, primary_key=True, autoincrement=True)
    weights = Column(JSONB, nullable=False)
    model_instance = Column(Integer, ForeignKey("model_instance.id"))
    iteration = Column(Integer, nullable=False)
    is_inference_weights = Column(
        Column(Boolean, nullable=False, default=False)
    )  # most recent weights
