import pytest
from attrs import define

from src.seriattrs import DbClass, varchar, text


@define
class Foo(DbClass):
    a: str = varchar(5)
    b: str = varchar(6)
    c: str = varchar(7)
    d: str = varchar(8)
    e: str = text()


@pytest.fixture
def foo_instance():
    return Foo("", "", "", "", "")


def test_attribute_a_out_of_range(foo_instance):
    with pytest.raises(ValueError):
        foo_instance.a = "Too long string"


def test_attribute_b_out_of_range(foo_instance):
    with pytest.raises(ValueError):
        foo_instance.b = "Too long"  # Exceeds varchar(6) length


def test_attribute_c_out_of_range(foo_instance):
    with pytest.raises(ValueError):
        foo_instance.c = "Too biggg"  # Exceeds varchar(7) length


def test_attribute_d_out_of_range(foo_instance):
    with pytest.raises(ValueError):
        foo_instance.d = "Exceeded limit"  # Exceeds varchar(8) length


def test_attribute_e_wrong_type(foo_instance):
    with pytest.raises(TypeError):
        foo_instance.e = 1


# Positive tests - Valid assignments within range
def test_attribute_a_positive(foo_instance):
    foo_instance.a = "Hello"
    assert foo_instance.a == "Hello"


def test_attribute_b_positive(foo_instance):
    foo_instance.b = "Greet1"
    assert foo_instance.b == "Greet1"


def test_attribute_c_positive(foo_instance):
    foo_instance.c = "World23"
    assert foo_instance.c == "World23"


def test_attribute_d_positive(foo_instance):
    foo_instance.d = "Testing4"
    assert foo_instance.d == "Testing4"


def test_attribute_e_positive(foo_instance):
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
    foo_instance.e = passed_text
    assert foo_instance.e == passed_text
