from typing import TYPE_CHECKING, Optional

from attr import define

from src.seriattrs import DbClassLiteral

if TYPE_CHECKING:
    from test.test_circular_dependency_not_literal.Ala import Ala


@define
class Cat(DbClassLiteral):
    ala: Optional["Ala"]
