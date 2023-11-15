from typing import Any

from db_class.src.JsonEncoder.Decoder import Decoder


class DecimalDecoder(Decoder):

    @staticmethod
    def is_valid(element: Any) -> bool:
        pass

    @staticmethod
    def decode(element: Any) -> str:
        pass
