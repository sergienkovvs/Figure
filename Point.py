from main import Figure


class Point(Figure):
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
