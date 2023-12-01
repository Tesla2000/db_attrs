from .integer import integer


class _int(integer):

    def _validate(self, value):
        super()._validate(value)
        if value < -(2 ** (self.bits - 1)):
            raise ValueError(f'{value=} must be more than {-(2 ** (self.bits - 1))}')
        if value > 2 ** (self.bits - 1) - 1:
            raise ValueError(f'{value=} must be less than {2 ** (self.bits - 1) - 1}')
