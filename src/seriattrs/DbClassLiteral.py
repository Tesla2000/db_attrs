from typing import get_args, Self

from attr import fields
from attrs import define

from .DbClass import DbClass
from .db_attrs_converter import db_attrs_converter


@define
class DbClassLiteral(DbClass):
    pass


def _handle_new_db(value, db_class_type):
    if isinstance(value, int):
        return value
    if db_class_type.__name__ not in type(db_class_type).temp_instances:
        type(db_class_type).temp_instances[db_class_type.__name__] = {}
    if value["_id"] in type(db_class_type).temp_instances[db_class_type.__name__]:
        return type(db_class_type).temp_instances[db_class_type.__name__][value["_id"]]
    else:
        if db_class_type not in type(db_class_type).created_types.values():
            db_class_type = next(class_ for class_ in type(db_class_type).created_types.values() if class_.__name__ == db_class_type.__name__)
        id_value = value.pop("_id")
        new_instance = db_class_type(**value)
        new_instance._id = id_value
        value["_id"] = id_value
        type(db_class_type).temp_instances[db_class_type.__name__][id_value] = new_instance
    for f in fields(db_class_type):
        types = list(get_args(f.type))
        if isinstance(f.type, type):
            types.append(f.type)
        references = tuple(field_type for field_type in types if isinstance(field_type, str))
        if references:
            raise ValueError("Data can't be deserialized as field {} in {} has a forward references {}. Consider making classes {} DbClasses and initializing them.".format(f.name, db_class_type.__name__, references, references))
        try:
            if any(issubclass(db_class_type if field_type == Self else field_type, DbClassLiteral) for field_type in types):
                setattr(
                    new_instance,
                    f.name,
                    db_attrs_converter.structure(value[f.name], f.type),
                )
        except Exception as e:
            pass
    return new_instance


db_attrs_converter.register_structure_hook_func(
    lambda t: issubclass(t, DbClass), _handle_new_db
)
