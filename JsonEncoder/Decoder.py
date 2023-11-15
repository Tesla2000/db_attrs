from abc import abstractmethod
from typing import Any

from db_class.JsonEncoder.JsonOperator import JSONOperator


class Decoder(JSONOperator):

    @staticmethod
    @abstractmethod
    def is_valid(element: Any) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def decode(element: Any) -> str:
        pass
