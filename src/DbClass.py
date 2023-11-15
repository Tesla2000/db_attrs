import json
import random
from typing import Any

from dataclasses import dataclass, field, asdict, fields

from db_class.src.JsonEncoder import Decoder
from db_class.src.JsonEncoder.DefaultJsonEncoder import DefaultJsonEncoder


@dataclass
class DbClass:
    _id: Any = field(init=False, default_factory=lambda: random.randint(0, 2 ** 64))
    json_encoder = DefaultJsonEncoder

    def __post_init__(self):
        for field in fields(self):
            for decoder in Decoder.__subclasses__():
                if decoder.is_valid(field.type):
                    setattr(self, field.name, decoder.decode(getattr(self, field.name)))
                    break

    def get_firebase_representation(self) -> dict:
        return json.loads(
            json.dumps(
                dict(
                    (
                        field.name,
                        value._id
                        if isinstance(value := getattr(self, field.name), DbClass)
                        else value,
                    )
                    for field in fields(self)
                ),
                cls=self.json_encoder,
            )
        )

    def serialize(self) -> dict:
        return json.loads(json.dumps(asdict(self), cls=self.json_encoder))
