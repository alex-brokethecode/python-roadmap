# Create a Person class with attributes name and age. Add a method greet() that prints a greeting with the person's name.

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    def greet(self) -> None:
        print(f'Hello everybody, My name is {self.__name}')


if __name__ == '__main__':
    person = Person('John', 25)
    person.greet()

    person.name = 'Megan'
    print(person.name)
