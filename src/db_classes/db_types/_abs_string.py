from abc import ABC, abstractmethod

from ._db_type import _db_type


class _abs_string(_db_type, str, ABC):
    _default = ''

    @abstractmethod
    def _validate(self, value):
        if not isinstance(value, str):
            raise ValueError(f'{value=} must be a string')
