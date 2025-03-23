# Object-Oriented Programming (OOP) in Python

## 1. Classes & Objects

### **Definition**
- **Class**: A blueprint for creating objects.
- **Object**: An instance of a class.

### **Basic Syntax**
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f'{self.brand} {self.model}'


# Creating an object
car1 = Car('Toyota', 'Corolla')
print(car1.display_info())  # Output: Toyota Corolla
```

---

## 2. Magic Methods (`__str__`, `__repr__`, `__len__`)

### **What are Magic Methods?**
- Special methods in Python (start & end with `__`).
- Used to define behavior for built-in operations.

### **Common Magic Methods**
| Magic Method  | Purpose |
|--------------|------------------------------------------------|
| `__init__`   | Constructor, initializes objects |
| `__str__`    | Defines a user-friendly string representation (`print()`) |
| `__repr__`   | Defines an unambiguous representation for debugging |
| `__len__`    | Defines behavior for `len()` |

### **Example**
```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{self.title} by {self.author}'

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"

    def __len__(self):
        return self.pages


book1 = Book('1984', 'George Orwell', 328)

print(str(book1))   # Output: 1984 by George Orwell
print(repr(book1))  # Output: Book('1984', 'George Orwell', 328)
print(len(book1))   # Output: 328
```

---

## 3. Encapsulation, Inheritance, Polymorphism, Abstraction

### **Encapsulation**
- **Hides internal details** of a class.
- Use **private attributes** (`_protected`, `__private`).

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount('Alice', 1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500

# print(account.__balance)  # AttributeError: private variable
```

---

### **Inheritance**
- **One class inherits from another** to reuse code.

```python
class Animal:
    def speak(self):
        return "I make a sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"


dog = Dog()
print(dog.speak())  # Output: Woof!
```

---

### **Polymorphism**
- **Same method name, different implementations**.

```python
class Cat:
    def speak(self):
        return "Meow!"

class Dog:
    def speak(self):
        return "Woof!"

animals = [Cat(), Dog()]

for animal in animals:
    print(animal.speak())

# Output:
# Meow!
# Woof!
```

---

### **Abstraction**
- **Hiding implementation details, only showing essential features**.
- Achieved using **abstract base classes (`ABC`)**.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass  # Must be implemented in subclasses

class Cat(Animal):
    def speak(self):
        return "Meow!"

cat = Cat()
print(cat.speak())  # Output: Meow!
```

---

# Exercises

## **Easy Level**
1. **Create a `Person` class** with attributes `name` and `age`. Add a method `greet()` that prints a greeting with the person's name. [Solution](./Exercises/01.py)
2. **Create a `Rectangle` class** with attributes `width` and `height`. Add a method `area()` to return the area of the rectangle. [Solution](./Exercises/02.py)
3. **Modify the `Rectangle` class** to include a `__str__` method that returns a string representation of the rectangle. [Solution](./Exercises/03.py)

## **Medium Level**
4. **Create a `Student` class** that inherits from `Person`. Add a new attribute `grade` and modify `greet()` to include the grade. [Solution](./Exercises/04.py)
5. **Create a `BankAccount` class** with a private attribute `_balance`. Add methods to deposit, withdraw, and get balance. [Solution](./Exercises/05.py) 
    - Note: Prevent overdraft (don't allow withdrawal if balance is insufficient) 
6. **Create a `Shape` abstract class** with an abstract method `area()`. Implement `Circle` and `Square` classes that inherit from `Shape`. [Solution](./Exercises/06.py)

## **Hard Level**
7. **Implement a `Company` class** that manages a list of `Employee` objects. [Solution](./Exercises/07.py)  
   - The `Employee` class should have `name` and `salary`.  
   - The `Company` class should have methods to add an employee, remove an employee, and calculate the total salary.
8. **Create a `Library` class** that manages a list of books. [Solution](./Exercises/08.py)
   - Books should be stored as a list of `Book` objects (created earlier).  
   - Implement methods to add books, remove books, and search books by title.
9. **Create a `Vehicle` class with a `fuel_efficiency()` abstract method.**  [Solution](./Exercises/09.py)
   - Implement `Car` and `Motorcycle` classes with different fuel efficiency calculations.
