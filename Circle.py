from Point import Point
from main import Figure


class Circle(Figure):
    radius = 0

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius


    def __str__(self):
        return super(Circle, self).__str__()[-1] + f", radius = {self.radius})"

    def __eg__(self, orther):
        return self.radius == orther.radius

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Circle(x, y, self.radius)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        radius = self.radius - other.radius
        if radius < 0:
            radius *= -1
        if radius == 0:
            return Point(x, y)
        else:
            return Circle(x, y, radius)