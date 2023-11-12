from abc import ABC
from typing import Type

from elite_core.features.sqlalchemy.repositories.abstract_repository import AbstractRepository, TEntity
from elite_core.features.sqlalchemy.repositories.elite_session import EliteSession


class OandaRepository(AbstractRepository):
    def __init__(self, session: EliteSession[TEntity], model: Type[TEntity]):
        super().__init__(session, model)

