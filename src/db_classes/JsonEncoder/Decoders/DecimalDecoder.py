from decimal import Decimal
from typing import Any

import cattrs

from ...JsonEncoder import Decoder


class DecimalDecoder(Decoder):
    @staticmethod
    def is_valid(element: Any) -> bool:
        return element == Decimal

    @staticmethod
    def decode(element: Any, _) -> Decimal:
        return Decimal(element)


cattrs.register_structure_hook(Decimal, DecimalDecoder.decode)
