import math
from dataclasses import dataclass

@dataclass
class Circle:
    radius: float

    def get_area(self):
        return math.pi * self.radius * self.radius

    def get_circumference(self):
        return 2 * math.pi * self.radius

@dataclass
class Rectangle:
    length: float
    width: float

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.width + self.length)


