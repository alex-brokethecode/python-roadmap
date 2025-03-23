# Implement a Company class that manages a list of Employee objects
# - The Employee class should have name and salary.
# - The Company class should have methods to add an employee, remove an employee, and calculate the total salary.

class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, salary: float) -> None:
        if salary < 0:
            raise ValueError('Salary cannot be negative')
        self.__salary = salary

    def __str__(self) -> str:
        return f"Employee(name: {self.name}, salary: {self.salary})"


class Company:
    def __init__(self) -> None:
        self.__employees: list[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        self.__employees.append(employee)

    def remove_employee(self, employee: Employee) -> None:
        if employee in self.__employees:
            self.__employees.remove(employee)
        else:
            print(f'Employee {employee.name} not found')

    def calc_total_salary(self) -> float:
        return sum(employee.salary for employee in self.__employees)


if __name__ == '__main__':
    employee1 = Employee('John Doe', 5000)
    employee2 = Employee('Megan Bayne', 4500)

    company = Company()
    company.add_employee(employee1)
    company.add_employee(employee2)

    print(f'Total salary: {company.calc_total_salary()}')

    company.remove_employee(employee1)

    print(f'Total salary: {company.calc_total_salary()}')
