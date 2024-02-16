import pytest
from attrs import define

from src.seriattrs import int8, int16, int32, int64, DbClass


@define
class Foo(DbClass):
    a: int = int8()
    b: int = int16()
    c: int = int32()
    d: int = int64()

@pytest.fixture
def foo_instance():
    return Foo(0, 0, 0, 0)

def test_attribute_a(foo_instance):
    with pytest.raises(ValueError):
        foo_instance.a = -129  # Below int8 range
    with pytest.raises(ValueError):
        foo_instance.a = 128  # Above int8 range

def test_attribute_b(foo_instance):
    with pytest.raises(ValueError):
        foo_instance.b = -32769  # Below int16 range
    with pytest.raises(ValueError):
        foo_instance.b = 32768  # Above int16 range

def test_attribute_c(foo_instance):
    with pytest.raises(ValueError):
        foo_instance.c = -2147483649  # Below int32 range
    with pytest.raises(ValueError):
        foo_instance.c = 2147483648  # Above int32 range

def test_attribute_d(foo_instance):
    with pytest.raises(ValueError):
        foo_instance.d = -9223372036854775809  # Below int64 range
    with pytest.raises(ValueError):
        foo_instance.d = 9223372036854775808  # Above int64 range

def test_attribute_a_positive(foo_instance):
    foo_instance.a = 50
    assert foo_instance.a == 50

def test_attribute_b_positive(foo_instance):
    foo_instance.b = -15000
    assert foo_instance.b == -15000

def test_attribute_c_positive(foo_instance):
    foo_instance.c = 2000000000
    assert foo_instance.c == 2000000000

def test_attribute_d_positive(foo_instance):
    foo_instance.d = -50000000000000000
    assert foo_instance.d == -50000000000000000
