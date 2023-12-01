from abc import ABC, abstractmethod


class db_type(ABC):
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    @abstractmethod
    def __set__(self, instance, value):
        pass
