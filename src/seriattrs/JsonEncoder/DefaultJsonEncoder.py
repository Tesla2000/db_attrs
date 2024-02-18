from json import JSONEncoder
from typing import Mapping

from .Encoder import Encoder


class DefaultJsonEncoder(JSONEncoder):
    @classmethod
    def default(cls, obj, strict: bool = True):
        for encoder in Encoder.__subclasses__():
            if encoder.is_valid(obj):
                return encoder.encode(obj)
        else:
            if strict:
                raise ValueError(obj, "can't be encoded")
            return obj

    @classmethod
    def serialize_values(cls, values, short_term_memory=None):
        if short_term_memory is None:
            short_term_memory = dict()
        if id(values) in short_term_memory:
            return short_term_memory[id(values)]
        else:
            short_term_memory[id(values)] = values
        if isinstance(values, Mapping):
            short_term_memory[id(values)] = dict(
                (key, cls.serialize_values(value, short_term_memory)) for key, value in values.items())
            return short_term_memory[id(values)]
        elif isinstance(values, list | set):
            short_term_memory[id(values)] = list(cls.serialize_values(item, short_term_memory) for item in values)
            return short_term_memory[id(values)]
        else:
            short_term_memory[id(values)] = cls._serialize_value(values)
            return short_term_memory[id(values)]

    @classmethod
    def _serialize_value(cls, obj):
        return DefaultJsonEncoder().default(obj, strict=False)
