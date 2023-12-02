import cattrs
from attr import fields
from attrs import define

from .DbClass import DbClass


@define
class DbClassLiteral(DbClass):
    pass


def _handle_new_db(value, db_class_type):
    if isinstance(value, int):
        return value
    id_value = value.pop("_id")
    new_instance = db_class_type(**value)
    new_instance._id = id_value
    value["_id"] = id_value
    for f in fields(db_class_type):
        if issubclass(f.type, DbClassLiteral):
            setattr(new_instance, f.name, cattrs.structure(value[f.name], f.type))
    return new_instance


cattrs.register_structure_hook_func(lambda t: issubclass(t, DbClass), _handle_new_db)
