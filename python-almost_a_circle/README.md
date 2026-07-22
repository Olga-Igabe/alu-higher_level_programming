# python-almost_a_circle

This project builds a small class hierarchy (`Base` -> `Rectangle` ->
`Square`) covering core OOP concepts in Python: private attributes with
property getters/setters, input validation, inheritance, `*args`/`**kwargs`,
JSON serialization, and file persistence. All classes are covered by a
`unittest` suite.

## Structure
models/
├── init.py
├── base.py         # Base: id management, JSON (de)serialization, file I/O
├── rectangle.py     # Rectangle: width/height/x/y, area, display, str
└── square.py        # Square: inherits Rectangle, adds size property
tests/
├── init.py
└── test_models/
├── init.py
├── test_base.py
├── test_rectangle.py
└── test_square.py
## Running the tests
## PEP8
