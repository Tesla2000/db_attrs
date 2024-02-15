import pytest
from attrs import define

from src.seriattrs import int8, DbClass, varchar, text, uint16


@define
class Foo(DbClass):
    a: int = int8()
    b: int = uint16()
    c: str = varchar(7)
    d: str = text()

@pytest.fixture
def foo_instance():
    return Foo(0, 0, '', '')

def test_attribute_a(foo_instance):
    with pytest.raises(ValueError):
        foo_instance.a = -129  # Below int8 range
    with pytest.raises(ValueError):
        foo_instance.a = 128  # Above int8 range

def test_attribute_b_out_of_range(foo_instance):
    with pytest.raises(ValueError):
        foo_instance.b = -1  # Below uint16 range
    with pytest.raises(ValueError):
        foo_instance.b = 65536  # Above uint16 range

def test_attribute_c_out_of_range(foo_instance):
    with pytest.raises(ValueError):
        foo_instance.c = "Too bigg"

def test_attribute_d_positive(foo_instance):
    passed_text = """I'm the Scatman
Ski-bi dibby dib yo da dub dub
Yo da dub dub
Ski-bi dibby dib yo da dub dub
Yo da dub dub
(I'm the Scatman)
Ski-bi dibby dib yo da dub dub
Yo da dub dub
Ski-bi dibby dib yo da dub dub
Yo da dub dub
Ba-da-ba-da-ba-be bop bop bodda bope
Bop ba bodda bope
Be bop ba bodda bope
Bop ba bodda
Ba-da-ba-da-ba-be bop ba bodda bope
Bop ba bodda bope
Be bop ba bodda bope
Bop ba bodda bope"""
    foo_instance.d = passed_text
    assert foo_instance.d == passed_text
