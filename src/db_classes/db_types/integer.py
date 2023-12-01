from abc import ABC, abstractmethod

from .db_type import db_type


class integer(db_type, ABC):
    bits: int

    @abstractmethod
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f'{value=} must be an integer')
