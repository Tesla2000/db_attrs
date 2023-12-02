from ._abs_string import _abs_string


class text(_abs_string):

    def _validate(self, value):
        super()._validate(value)
