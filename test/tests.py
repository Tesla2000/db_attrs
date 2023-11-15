from src import DbClass, ImplementingFromDict


def test_imports():
    __all__ = [
        "DbClass",
        "ImplementingFromDict"
    ]
    assert __all__
