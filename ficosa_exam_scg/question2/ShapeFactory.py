from .shapes.Circle import Circle
from .shapes.Rectangle import Rectangle
from .shapes.Square import Square


class ShapeFactory:
    def get_shape(self, shape):
        if shape == 'circle':
            return Circle()
        elif shape == 'rectangle':
            return Rectangle()
        elif shape == 'square':
            return Square()