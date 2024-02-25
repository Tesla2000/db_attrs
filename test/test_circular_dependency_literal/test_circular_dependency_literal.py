def test_circular_dependency_literal():
    from test.test_circular_dependency_literal.Ala import Ala
    from test.test_circular_dependency_literal.Cat import Cat
    cat = Cat(None)
    ala = Ala(cat)
    cat.ala = ala

    serialized_cat = cat.serialize()
    serialized_ala = ala.serialize()
    deserialized_cat = Cat.deserialize(serialized_cat)
    deserialized_ala = Ala.deserialize(serialized_ala)
    assert deserialized_cat.id == cat.id
    assert deserialized_cat.ala.id == cat.ala.id
    assert deserialized_cat.ala.cat.id == cat.ala.cat.id

    assert deserialized_ala.id == ala.id
    assert deserialized_ala.cat.id == ala.cat.id
    assert deserialized_ala.cat.ala.id == ala.cat.ala.id
