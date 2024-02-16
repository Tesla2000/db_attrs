import pytest
from attrs import define

from src.seriattrs import DbClass, char


@define
class Foo(DbClass):
    a: str = char(5)
    b: str = char(6)
    c: str = char(7)
    d: str = char(8)


@pytest.fixture
def foo_instance():
    return Foo("12345", "204984", "fnsaffa", "oinifonc")


def test_init_error():
    with pytest.raises(ValueError):
        Foo("12345", "204984", "fnsafa", "oinifonc")


def test_init_positive():
    Foo("12345", "204984", "fnsaffa", "oinifonc")


def test_attribute_out_of_range(foo_instance):
    with pytest.raises(ValueError):
        foo_instance.a = "Too long string"
    with pytest.raises(ValueError):
        foo_instance.d = "short"


def test_attribute_in_range(foo_instance):
    foo_instance.a = "nisad"
    foo_instance.d = "oinifonc"
