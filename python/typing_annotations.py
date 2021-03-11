# Annotating return type with class name

# this only works in 3.7+
from __future__ import annotations

# otherwise you have to do something like
class Blah:
    """Just a forward declaration."""
    pass

# the class to be annotated
class Blah:
    def __init__(self):
        self.thing = 'blah'

    @classmethod
    def make_blah(cls, raw: str) -> Blah:
        return Blah()