from .integer import integer


class _uint(integer):

    def __set__(self, instance, value):
        super().__set__(instance, value)
        if value < 0:
            raise ValueError(f'{value=} must be positive')
        if value > 2 ** self.bits - 1:
            raise ValueError(f'{value=} must be less than {2 ** self.bits - 1}')
