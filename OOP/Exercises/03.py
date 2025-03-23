# Modify the Rectangle class to include a __str__ method that returns a string representation of the rectangle

class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.__width = width
        self.__height = height

    def area(self) -> float:
        return self.__width * self.__height

    def __str__(self) -> str:
        return f'Rectangle:\nwidth: {self.__width}\nheight: {self.__height}'


if __name__ == '__main__':
    rectangle = Rectangle(10, 5)
    print(rectangle)
