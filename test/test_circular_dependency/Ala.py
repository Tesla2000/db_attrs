from typing import TYPE_CHECKING

from attr import define

from src.seriattrs import DbClass

if TYPE_CHECKING:
    from test.test_circular_dependency.Cat import Cat


@define
class Ala(DbClass):
    cat: "Cat"
