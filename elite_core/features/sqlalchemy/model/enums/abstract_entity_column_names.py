from enum import Enum


class AbstractEntityColumnNames(str, Enum):
    ID = 'id'
    CREATED_ON = 'created_on'
    UPDATED_ON = 'updated_on'
