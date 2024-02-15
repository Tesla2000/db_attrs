import pytest
from attrs import define

from src.seriattrs import uint8, uint16, uint32, uint64, DbClass


@define
class Foo(DbClass):
    a: int = uint8()
    b: int = uint16()
    c: int = uint32()
    d: int = uint64()


@pytest.fixture
def foo_instance():
    return Foo(0, 0, 0, 0)


# Negative tests - ValueErrors on out-of-range assignments
def test_attribute_a_out_of_range(foo_instance):
    with pytest.raises(ValueError):
        foo_instance.a = -1  # Below uint8 range
    with pytest.raises(ValueError):
        foo_instance.a = 256  # Above uint8 range


def test_attribute_b_out_of_range(foo_instance):
    with pytest.raises(ValueError):
        foo_instance.b = -1  # Below uint16 range
    with pytest.raises(ValueError):
        foo_instance.b = 65536  # Above uint16 range


def test_attribute_c_out_of_range(foo_instance):
    with pytest.raises(ValueError):
        foo_instance.c = -1  # Below uint32 range
    with pytest.raises(ValueError):
        foo_instance.c = 4294967296  # Above uint32 range


def test_attribute_d_out_of_range(foo_instance):
    with pytest.raises(ValueError):
        foo_instance.d = -1  # Below uint64 range
    with pytest.raises(ValueError):
        foo_instance.d = 18446744073709551616  # Above uint64 range


def test_attribute_a_positive(foo_instance):
    foo_instance.a = 50
    assert foo_instance.a == 50


def test_attribute_b_positive(foo_instance):
    foo_instance.b = 15000
    assert foo_instance.b == 15000


def test_attribute_c_positive(foo_instance):
    foo_instance.c = 2000000000
    assert foo_instance.c == 2000000000


def test_attribute_d_positive(foo_instance):
    foo_instance.d = 50000000000000000
    assert foo_instance.d == 50000000000000000
