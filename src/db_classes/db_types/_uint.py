from .integer import integer


class _uint(integer):

    def _validate(self, value):
        super()._validate(value)
        if value < 0:
            raise ValueError(f'{value=} must be positive')
        if value > 2 ** self.bits - 1:
            raise ValueError(f'{value=} must be less than {2 ** self.bits - 1}')

