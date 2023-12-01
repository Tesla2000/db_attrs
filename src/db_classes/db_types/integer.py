from abc import ABC, abstractmethod

from .db_type import db_type


class integer(db_type, int, ABC):
    bits: int
    _default = 0

    @abstractmethod
    def _validate(self, value):
        if not isinstance(value, int):
            raise ValueError(f'{value=} must be an integer')
