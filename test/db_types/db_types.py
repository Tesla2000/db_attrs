from dataclasses import dataclass, fields

from src.db_classes import uint8, uint16, uint32, uint64, DbClass


@dataclass
class Foo(DbClass):
    a: uint8
    b: uint16
    c: uint32
    d: uint64


Foo(-100, 100, 100, 100)
