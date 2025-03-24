# Advanced Functions in Python: Lambda, Map, Filter, Reduce

## 1. Lambda Functions
Lambda functions are anonymous, single-expression functions in Python. They are useful when you need a small function for a short period.

### Syntax:
```python
lambda arguments: expression
```

### Example:
```python
square = lambda x: x ** 2
print(square(5))  # Output: 25
```

## 2. The `map()` Function
The `map()` function applies a given function to all items in an iterable.

### Syntax:
```python
map(function, iterable)
```

### Example:
```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

## 3. The `filter()` Function
The `filter()` function filters elements of an iterable based on a condition.

### Syntax:
```python
filter(function, iterable)
```

### Example:
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8]
```

## 4. The `reduce()` Function
The `reduce()` function applies a function cumulatively to the elements of an iterable. It is part of the `functools` module.

### Syntax:
```python
from functools import reduce
reduce(function, iterable)
```

### Example:
```python
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers)  # Output: 15
```

---

# Exercises

## Easy
1. Write a lambda function that takes a number and returns its cube. [Solution](./Exercises/01.py)
2. Use `map()` to convert a list of temperatures in Celsius to Fahrenheit. [Solution](./Exercises/02.py)
3. Use `filter()` to extract words longer than 5 characters from a list. [Solution](./Exercises/03.py)
4. Use `reduce()` to multiply all numbers in a list. [Solution](./Exercises/04.py)

## Medium
5. Given a list of dictionaries with `name` and `age`, use `map()` to extract only the names. [Solution](./Exercises/05.py)
6. Use `filter()` to keep only palindromic words from a list. [Solution](./Exercises/06.py)
7. Use `reduce()` to find the longest word in a list of strings. [Solution](./Exercises/07.py)

## Hard
8. Given a list of numbers, use `map()`, `filter()`, and `reduce()` together to: [Solution](./Exercises/08.py)
   - Square each number
   - Filter out even numbers
   - Find the sum of the remaining numbers
9. Implement a custom version of `map()`, `filter()`, and `reduce()` using loops and list comprehensions. [Solution](./Exercises/09.py)


