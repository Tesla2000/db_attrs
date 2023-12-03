from typing import TYPE_CHECKING, Optional

from attr import define

from src.seriattrs import DbClass
if TYPE_CHECKING:
    from test.test_circular_dependency.Ala import Ala


@define
class Cat(DbClass):
    ala: Optional["Ala"]
