from abc import ABC, abstractmethod

from ._db_type import _db_type


class _abs_integer(_db_type, int, ABC):
    bits: int
    _default = 0

    @abstractmethod
    def _validate(self, value):
        if not isinstance(value, int):
            raise ValueError(f'{value=} must be an integer')
