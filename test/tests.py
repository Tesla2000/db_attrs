from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from dacite import from_dict, Config

from src import DbClass, ImplementingFromDict
from src.DbClassLiteral import DbClassLiteral
from src.JsonEncoder.JsonOperator import datetime_format


def test_imports():
    __all__ = [
        "DbClass",
        "ImplementingFromDict"
    ]
    assert __all__


def test_serialize():
    @dataclass
    class Bar(DbClassLiteral):
        dictionary: dict
        date: datetime
        decimal: Decimal

    @dataclass
    class Foo(DbClass):
        dictionary: dict
        date: datetime
        decimal: Decimal
        bar: Bar
    time = datetime.strptime(datetime.now().strftime(datetime_format), datetime_format)
    foo = Foo({}, time, Decimal(1), Bar({}, time, Decimal(1)))
    serialized = foo.get_db_representation()
    deserialized = from_dict(Foo, serialized, Config(check_types=False))
    assert deserialized == foo


if __name__ == '__main__':
    test_serialize()
