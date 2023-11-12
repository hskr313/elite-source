from typing import TypeVar, Type, Generic, List, Optional, Union, Any, Dict

from sqlalchemy import select
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import Session

TEntity = TypeVar('TEntity')
T = TypeVar('T')


class EliteSession(Generic[TEntity], Session):
    def __init__(self):
        super().__init__()

    def any(self, entity_class: Type[TEntity], options: Dict[str, Any]) -> bool:
        query = select(entity_class).filter_by(**options)
        return self.execute(query).scalar() is not None

    def find_many(self, entity_class: Type[TEntity], options: Dict[str, Any]) -> List[TEntity]:
        return self.query(entity_class).filter_by(**options).all()

    def find_one_or_none(self, entity_class: Type[TEntity], id_or_options: Union[int, Dict[str, Any]]) -> Optional[
        TEntity]:
        if isinstance(id_or_options, int):
            return self.query(entity_class).get(id_or_options)
        else:
            if EliteSession._validate_options(entity_class, id_or_options):
                return self.query(entity_class).filter_by(**id_or_options)

    def find_one_or_not_found(self, entity_class: Type[TEntity], id_or_options: Union[int, Dict[str, Any]]) -> TEntity:
        entity = self.find_one_or_none(entity_class, id_or_options)

        if not entity:
            raise ValueError('Entity Not Found')
        return entity

    def remove_by_id(self, entity_class: Type[TEntity], entity_id: int, commit: bool = True) -> None:
        entity = self.find_one_or_not_found(entity_class, entity_id)
        self.delete(entity)

        if commit:
            self.commit()

    @staticmethod
    def _validate_options(entity_class: Type[TEntity], options: Dict[str, Any]) -> bool:
        entity_info = inspect(entity_class)
        for key, value in options.items():
            if key not in entity_info.attrs:
                raise ValueError(f"'{key}' not in {entity_class.__name__}")

            expected_type = type(getattr(entity_class, key))
            if not isinstance(value, expected_type):
                raise TypeError(f"Incorrect type for '{key}': expected {expected_type}, received {type(value)}")

        return True
