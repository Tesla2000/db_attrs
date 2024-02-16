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
    assert deserialized_cat._id == cat._id
    assert deserialized_cat.ala._id == cat.ala._id
    assert deserialized_cat.ala.cat._id == cat.ala.cat._id

    assert deserialized_ala._id == ala._id
    assert deserialized_ala.cat._id == ala.cat._id
    assert deserialized_ala.cat.ala._id == ala.cat.ala._id
