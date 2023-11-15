from decimal import Decimal

from ..Decoder import Decoder


class DatetimeDecoder(Decoder):

    @staticmethod
    def is_valid(field_type: type) -> bool:
        return field_type == Decimal

    @staticmethod
    def decode(element: str) -> Decimal:
        return Decimal(element)
