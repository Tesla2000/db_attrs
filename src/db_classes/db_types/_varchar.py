from ._abs_string import _abs_string


class _varchar(_abs_string):
    _max_length: int

    def _validate(self, text):
        super()._validate(text)
        if len(text) > self._max_length:
            raise ValueError(f'Length of {text=} must be less than {self._max_length} is {len(text)}')
