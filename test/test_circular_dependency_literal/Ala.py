from typing import TYPE_CHECKING

from attr import define

from src.seriattrs import DbClassLiteral

if TYPE_CHECKING:
    from test.test_circular_dependency_not_literal.Cat import Cat


@define
class Ala(DbClassLiteral):
    cat: "Cat"
