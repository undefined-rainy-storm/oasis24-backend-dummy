from json import dumps
from .vector2 import Vector2

class Polyline:
    def __init__(self, path: list[Vector2]):
        self.path: list[Vector2] = path

    def __repr__(self):
        return dumps(self.path)

    def __str__(self):
        return dumps(self.path)
