import json
import random
from copy import deepcopy
from typing import Any, Self, get_args, Mapping, Sequence

from attr import define, fields, field, has

from .DbClassCreator import DbClassCreator
from .db_attrs_converter import db_attrs_converter
from .JsonEncoder import Decoder, DefaultJsonEncoder
from .JsonEncoder.default_json_encoder import json_encoder


@define
class DbClass(metaclass=DbClassCreator):
    _id = field(init=False, type=Any, factory=lambda: random.randint(-2**63, 2**63 - 1))

    def __attrs_post_init__(self):
        if hasattr(self, 'id'):
            self._id = self.id
        self._decode()

    def serialize(self) -> dict:
        from .DbClassLiteral import DbClassLiteral

        return DefaultJsonEncoder.serialize_values(
                dict(
                    (
                        f.name,
                        getattr(self, f.name)._id
                        if isinstance(getattr(self, f.name), DbClass)
                        and not isinstance(getattr(self, f.name), DbClassLiteral)
                        else getattr(self, f.name),
                    )
                    for f in fields(type(self))
                ),
            )

    @classmethod
    def deserialize(cls, dictionary: dict) -> Self:
        type(cls).temp_instances = {}
        deserialized = db_attrs_converter.structure(dictionary, cls)
        type(cls).temp_instances = {}
        # cls._fill_deserialize_values(deserialized)
        # deserialized._fill_id(dictionary)
        return deserialized

    def _fill_id(self, dictionary: dict):
        from .DbClassLiteral import DbClassLiteral

        self._id = dictionary["_id"]
        for f in fields(type(self)):
            types = list(get_args(f.type))
            if isinstance(f.type, type):
                types.append(f.type)
            if any(issubclass(type(self) if field_type == Self else field_type, DbClassLiteral) for field_type in types):
                field_type = next(field_type for field_type in types if issubclass(type(self) if field_type == Self else field_type, DbClassLiteral))
                field_type._fill_id(getattr(self, f.name), dictionary[f.name])

    def _decode(self):
        for f in fields(type(self)):
            for decoder in Decoder.__subclasses__():
                if decoder.is_valid(f.type):
                    setattr(self, f.name, decoder.decode(getattr(self, f.name), f.type))
                    break
    
    @classmethod
    def _fill_deserialize_values(cls, values, short_term_memory=None):
        if short_term_memory is None:
            short_term_memory = dict()
        if isinstance(values, DbClass) and values._id in short_term_memory:
            return short_term_memory[values._id]
        elif isinstance(values, dict) and values.get('_id') in short_term_memory:
            return short_term_memory[values['_id']]
        elif isinstance(values, DbClass):
            short_term_memory[values._id] = values
        if isinstance(values, Mapping):
            for key, value in tuple(values.items()):
                values[key] = cls._fill_deserialize_values(value, short_term_memory)
            return values
        elif isinstance(values, Sequence):
            for index, item in values:
                values[index] = cls._fill_deserialize_values(item, short_term_memory)
            return values
        elif has(values):
            for f in fields(type(values)):
                setattr(values, f.name, cls._fill_deserialize_values(getattr(values, f.name), short_term_memory))
            return values
        else:
            return values
