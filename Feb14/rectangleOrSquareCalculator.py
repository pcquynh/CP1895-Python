class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def perimeter_calculator(self):
        return (self.width + self.height) * 2

    def area_calculator(self):
        return self.width * self.height

    def get_shape(self):
        shape = ''
        x = '   '
        for i in range(1, self.height + 1):
            if i == 1 or i == self.height:
                shape += ('*  ' * self.width) + '\n'
            else:
                shape += ('*  ' + x * (self.width-2) + '*') + '\n'
        return shape

    def __str__(self):
        return (f'Perimeter: {self.perimeter_calculator()}'
                f'\nArea: {self.area_calculator()}'
                f'\n{self.get_shape()}')


class Square(Rectangle):
    def __init__(self, height, width):
        Rectangle.__init__(self, height, width)

    def __str__(self):
        return Rectangle.__str__(self)

