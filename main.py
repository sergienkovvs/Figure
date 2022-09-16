import math


class Figure:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eg__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)