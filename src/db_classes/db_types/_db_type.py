from abc import ABC, abstractmethod


class _db_type(ABC):
    _default = None

    @abstractmethod
    def _validate(self, value):
        pass

    def __init__(self, *args):
        value = self._default
        if args:
            value = args[0]
        self._validate(value)
        self.value = value

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, self.value)

    def __set__(self, instance, value):
        self._validate(value)
        instance.__dict__[self.name] = value
