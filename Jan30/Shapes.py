import math
from dataclasses import dataclass

@dataclass
class Circle:
    radius: float
    center_position: tuple = (0, 0)

    def get_area(self):
        return math.pi * self.radius * self.radius

    def get_circumference(self):
        return 2 * math.pi * self.radius

@dataclass
class Rectangle:
    length: float
    width: float
    top_left_corner_position: tuple = (0, 0)

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.width + self.length)


