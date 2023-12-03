from test.test_circular_dependency.Ala import Ala
from test.test_circular_dependency.Cat import Cat


def test_circular_dependency():
    cat = Cat(None)
    ala = Ala(cat)
    cat.ala = ala

    serialized_cat = cat.serialize()
    serialized_ala = ala.serialize()
    cat.ala = ala._id
    ala.cat = cat._id
    assert Cat.deserialize(serialized_cat) == cat
    assert Ala.deserialize(serialized_ala) == ala


if __name__ == '__main__':
    test_circular_dependency()
