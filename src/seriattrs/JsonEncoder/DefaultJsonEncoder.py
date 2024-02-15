from json import JSONEncoder

from .Encoder import Encoder


class DefaultJsonEncoder(JSONEncoder):
    def default(self, obj, strict: bool=True):
        for encoder in Encoder.__subclasses__():
            if encoder.is_valid(obj):
                return encoder.encode(obj)
        else:
            if strict:
                raise ValueError(obj, "can't be encoded")
            return obj
