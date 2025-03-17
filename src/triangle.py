from src.figure import Figure
import math


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Triangle sides can't be less than 0")
        if side_a + side_c < side_b or side_a + side_b < side_c or side_b + side_c < side_a:
            raise ValueError("Triangle doesn't exist")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    @property
    def get_area(self):
        hp = self.get_perimeter / 2
        return math.sqrt(hp * (hp - self.side_a) * (hp - self.side_b) * (hp - self.side_c))