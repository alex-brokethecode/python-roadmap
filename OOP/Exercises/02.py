# Create a Rectangle class with attributes width and height. Add a method area() to return the area of the rectangle.

class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.__width = width
        self.__height = height

    def area(self) -> float:
        return self.__width * self.__height


if __name__ == '__main__':
    rectangle = Rectangle(10, 5)
    print(rectangle)
    print(rectangle.area())
