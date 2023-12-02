from ._abs_string import _abs_string


class _char(_abs_string):
    _length: int

    def _validate(self, text):
        super()._validate(text)
        if len(text) != self._length:
            raise ValueError(f'Length of {text=} must be {self._length} is {len(text)}')
