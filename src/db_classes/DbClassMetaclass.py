from dataclasses import field

from .db_types.db_type import db_type


class DbClassMetaclass(type):
    def __new__(cls, name, bases, namespace):
        for annotation, value in namespace.get('__annotations__', {}).items():
            if annotation not in namespace and issubclass(value, db_type):
                f = field()
                f.default = value()
                namespace[annotation] = f
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
