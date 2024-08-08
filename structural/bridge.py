from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


class Color(ABC):
    @abstractmethod
    def apply_color(self):
        pass


class Circle(Shape):
    def draw(self):
        print(f"Drawing a circle with {self.color.apply_color()} color.")


class Square(Shape):
    def draw(self):
        print(f"Drawing a square with {self.color.apply_color()} color.")


class Red(Color):
    def apply_color(self):
        return "#ff0000"


class Blue(Color):
    def apply_color(self):
        return "#0000ff"


if __name__ == "__main__":
    red_color = RedColor()
    blue_color = BlueColor()

    red_circle = Circle(red_color)
    blue_square = Square(blue_color)

    red_circle.draw()
    blue_square.draw()