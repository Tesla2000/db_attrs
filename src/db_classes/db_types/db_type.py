from abc import ABC, abstractmethod
from typing import Any


class db_type(ABC):

    def __init__(self, instance: Any = None, value: int = None):
        if instance and value:
            self.__set__(instance, value)

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    @abstractmethod
    def __set__(self, instance, value):
        pass
