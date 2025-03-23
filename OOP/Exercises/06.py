# Create a Shape abstract class with an abstract method area(). Implement Circle and Square classes that inherit from Shape.

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Square(Shape):
    def __init__(self, side) -> None:
        self.side = side

    @property
    def side(self) -> float:
        return self.__side

    @side.setter
    def side(self, side) -> None:
        if side < 0:
            raise ValueError('Side cannot be negative')
        self.__side = side

    def area(self) -> float:
        return self.side * self.side


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    @property
    def radius(self) -> float:
        return self.__radius

    @radius.setter
    def radius(self, radius: float) -> None:
        if radius < 0:
            raise ValueError('Radius cannot be negative')

        self.__radius = radius

    def area(self) -> float:
        return self.radius ** 2 * pi


if __name__ == '__main__':
    try:
        square = Square(5)
        print(square.area())

        circle = Circle(5)
        print(circle.area())
    except ValueError as e:
        print(e)
