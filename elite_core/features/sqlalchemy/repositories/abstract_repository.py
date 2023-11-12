from abc import ABC
from typing import Generic, TypeVar, Type

from sqlalchemy.orm import DeclarativeBase

from elite_core.features.sqlalchemy.repositories.elite_session import EliteSession

TEntity = TypeVar('TEntity', bound=DeclarativeBase)


class AbstractRepository(Generic[TEntity], ABC):
    def __init__(self, session: EliteSession[TEntity], model: Type[TEntity]):
        self.session = session
        self.model = model

