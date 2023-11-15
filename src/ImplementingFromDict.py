from abc import abstractmethod, ABC
from dataclasses import dataclass

from .DbClass import DbClass


@dataclass
class ImplementingFromDict(DbClass, ABC):
    @classmethod
    @abstractmethod
    def from_dict(cls, dictionary: dict):
        pass
