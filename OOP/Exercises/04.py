# Create a Student class that inherits from Person. Add a new attribute grade and modify greet() to include the grade.

class Person:
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name


class Student(Person):
    def __init__(self, name: str, grade: float) -> None:
        super().__init__(name)
        self.__grade = grade

    def __str__(self) -> str:
        return f'Student:\nname: {self.name}\ngrade: {self.__grade}'


if __name__ == '__main__':
    student = Student('John', 3.5)
    print(student)
