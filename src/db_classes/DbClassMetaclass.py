from dataclasses import dataclass, is_dataclass


class DbClassMetaclass(type):
    def __new__(cls, *args, **kwargs):
        return dataclass(super().__new__(cls, *args, **kwargs))


if __name__ == '__main__':
    class Foo(metaclass=DbClassMetaclass):
        foo: int


    class Foo2(Foo):
        foo2: int


    Foo(1)
    Foo2(1, 2)

    assert is_dataclass(Foo)
