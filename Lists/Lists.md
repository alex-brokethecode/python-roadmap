# Topic 1: Lists in Python

## Theory

A **list** in Python is an **ordered, mutable** collection that can store different data types (numbers, strings, objects, etc.).

### Creating Lists

```python
# Empty list
my_list = []

# List with elements
numbers = [1, 2, 3, 4, 5]
words = ["hello", "world"]
mixed = [10, "Python", 3.14, True]
```

### Accessing Elements

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0])   # First element -> 10
print(numbers[-1])  # Last element -> 50
print(numbers[1:4]) # Sublist -> [20, 30, 40]
```

### Modifying Lists

```python
numbers[2] = 100  # Change an element
print(numbers)  # [10, 20, 100, 40, 50]
```

### Useful List Methods

```python
my_list = [3, 1, 4, 1, 5]

my_list.append(9)      # Add an element at the end
my_list.insert(2, 10)  # Insert at a specific position
my_list.remove(1)      # Remove the first occurrence of "1"
my_list.pop()          # Remove the last element
my_list.sort()         # Sort the list
my_list.reverse()      # Reverse the list

print(my_list)
```

### List Comprehension

A compact way to create lists in a single line.

```python
squares = [x**2 for x in range(10)]  # [0, 1, 4, 9, ..., 81]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

# **Practice Exercises - Lists in Python**

## Easy Level

1. Create a list with numbers from 1 to 10 and print the third element. [Solution](./Exercises/01.py)
2. Add the number 11 to the end of the list and remove the first number. [Solution](./Exercises/02.py)
3. Create a list of squares for numbers from 1 to 10 using list comprehension. [Solution](./Exercises/03.py)

## Medium Level

4. Given a list of names, remove duplicates while keeping the original order. [Solution](./Exercises/04.py)
5. Reverse a list without using the `.reverse()` method. [Solution](./Exercises/05.py)
6. Find the largest and smallest number in a list without using `max()` or `min()`. [Solution](./Exercises/06.py)

## Hard Level

7. Write a program that **merges two lists of the same length by alternating elements**. [Solution](./Exercises/07.py)

   **Example:**

```python
list1 = [1, 3, 5]
list2 = [2, 4, 6]
output = [1, 2, 3, 4, 5, 6]
```

8. Implement a function that **removes duplicates without using `set()`** and maintains the original order. [Solution](./Exercises/08.py)
