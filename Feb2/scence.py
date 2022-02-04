from dataclasses import dataclass
from shapes import Circle, Rectangle

@dataclass
class Scene:
    shapes: list

    def add_shapes(self, new_shape):
        assert isinstance(new_shape, Circle) or isinstance(new_shape, Rectangle),'Shape must be a circle or a rectangle'
        self.shapes.append(new_shape)