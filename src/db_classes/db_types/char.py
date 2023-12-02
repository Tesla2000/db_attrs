from ._char import _char


def char(length: int):
    class char(_char):
        _default = length * ' '
        _length = length

    return char
