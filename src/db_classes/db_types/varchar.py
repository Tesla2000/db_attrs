from ._varchar import _varchar


def varchar(max_length: int):

    class varchar(_varchar):
        _max_length = max_length

    return varchar
