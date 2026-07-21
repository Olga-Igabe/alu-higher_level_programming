# python-inheritance

This project explores Python inheritance: introspecting objects with
`dir()`, subclassing built-in types like `list`, checking object/class
relationships (`type()` vs `isinstance()`), and building a small geometry
class hierarchy (`BaseGeometry` -> `Rectangle` -> `Square`) with private
attributes, custom validation, and method overriding.

## Files

- `0-lookup.py` — lists all attributes/methods of an object
- `1-my_list.py` — `MyList`, a `list` subclass with `print_sorted()`
- `2-is_same_class.py` — checks exact class match
- `3-is_kind_of_class.py` — checks class or subclass match
- `4-inherits_from.py` — checks strict subclass (not exact class) match
- `5-base_geometry.py` — empty `BaseGeometry` class
- `6-base_geometry.py` — adds `area()` that raises `NotImplementedError`-style `Exception`
- `7-base_geometry.py` — adds `integer_validator()` for input validation
- `8-rectangle.py` — `Rectangle` with private, validated `width`/`height`
- `9-rectangle.py` — adds `area()` and `__str__`
- `10-square.py` — `Square` inheriting from `Rectangle`, using `size`
- `11-square.py` — adds `__str__` override for `Square`
