from .db_types._db_type import _db_type
from typing import get_args


class DbClassMetaclass(type):
    def __new__(cls, name, bases, namespace):
        for annotation, value in namespace.get('__annotations__', {}).items():
            if annotation in namespace:
                continue
            if (args := get_args(value)) and (db_types := tuple(v for v in args if issubclass(v, _db_type))):
                if len(db_types) > 1:
                    raise ValueError(f'Only one db_type allowed in hinting is {db_types=}')
                namespace[annotation] = db_types[0]()
            elif issubclass(value, _db_type):
                namespace[annotation] = value()
        new_class = super().__new__(cls, name, bases, namespace)
        return new_class


if __name__ == '__main__':
    from dataclasses import is_dataclass


    class Foo(metaclass=DbClassMetaclass):
        foo: int


    class Foo2(Foo):
        foo2: int


    Foo(1)
    Foo2(1, 2)

    assert is_dataclass(Foo)
