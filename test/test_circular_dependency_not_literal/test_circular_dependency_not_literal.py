def test_circular_dependency_not_literal():
    from test.test_circular_dependency_not_literal.Ala import Ala
    from test.test_circular_dependency_not_literal.Cat import Cat
    cat = Cat(None)
    ala = Ala(cat)
    cat.ala = ala

    serialized_cat = cat.serialize()
    serialized_ala = ala.serialize()
    cat.ala = ala.id
    ala.cat = cat.id
    assert Cat.deserialize(serialized_cat) == cat
    assert Ala.deserialize(serialized_ala) == ala
