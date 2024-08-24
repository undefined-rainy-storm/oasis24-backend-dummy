from typing import Generic, TypeVar

T = TypeVar('T')

class Vector2(Generic[T]):
    def __init__(self, x: T, y: T):
        self.x: T = x
        self.y: T = y

    def __str__(self):
        return f'Vector2({self.x}, {self.y})'

    def __repr__(self):
        return f'({repr(self.x)}, {repr(self.y)})'
