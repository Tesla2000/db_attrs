from importlib import util
from pathlib import Path

specs = tuple(
    util.spec_from_file_location(module_path.name, module_path) for module_path in Path(__file__).parent.iterdir() if
    module_path.name not in ('__init__.py', '__pycache__'))
foo = tuple(map(util.module_from_spec, specs))
