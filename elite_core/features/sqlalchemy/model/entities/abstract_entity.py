from datetime import datetime

from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import declarative_base, DeclarativeBase

from elite_core.features.sqlalchemy.model.enums.abstract_entity_column_names import AbstractEntityColumnNames

Base = declarative_base()


class AbstractEntity(DeclarativeBase):
    __abstract__ = True

    id = Column(Integer, primary_key=True, name=AbstractEntityColumnNames.ID)

    createdOn = Column(DateTime, default=datetime.utcnow, name=AbstractEntityColumnNames.CREATED_ON)

    updatedOn = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow,
                       name=AbstractEntityColumnNames.UPDATED_ON)
