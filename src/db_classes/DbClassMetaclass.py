from dataclasses import dataclass, is_dataclass


# class DataclassBlockedAnnotations(dict):
#     def __init__(self, values: dict):
#         super().__init__(values)
#
#     def __iter__(self):
#         pass


class DbClassMetaclass(type):
    def __new__(cls, name, bases, namespace):
        new_class = super().__new__(cls, name, bases, namespace)
        new_db_class = dataclass(new_class)
        new_db_class.__annotations__ = {}
        bases = list(base for base in new_db_class.__bases__)
        bases.insert(0, new_db_class)
        new_class = super().__new__(cls, name, tuple(bases), namespace)
        new_db_class = dataclass(new_class)
        new_db_class.__annotations__ = {}
        return new_db_class


if __name__ == '__main__':
    class Foo(metaclass=DbClassMetaclass):
        foo: int


    class Foo2(Foo):
        foo2: int


    Foo(1)
    Foo2(1, 2)

    assert is_dataclass(Foo)
