# Variables, Data Types, and Operators in Python

## Theory

In Python, variables are used to store data values. Data types define the kind of value a variable can hold, and operators are symbols that perform operations on variables and values.

## Variables

Variables are dynamically typed, meaning you don't need to declare their type explicitly.
Variable names must start with a letter or underscore, and can contain letters, numbers, and underscores.
Python is case-sensitive (e.g., `myVar` and `myvar` are different variables).

```python
x = 5
name = "John"
is_valid = True
```

## Data Types

Python has several built-in data types:

**Numeric Types:**

- `int`: Integers (e.g., 10, -5).
- `float`: Floating-point numbers (e.g., 3.14, -0.5).
- `complex`: Complex numbers (e.g., 2 + 3j).

**Text Type:**

- `str`: Strings (e.g., "Hello", 'World').

**Sequence Types:**

- `list`: Ordered, mutable collections (e.g., [1, 2, 3], ["apple", "banana"]).
- `tuple`: Ordered, immutable collections (e.g., (1, 2, 3), ("apple", "banana")).
- `range`: Sequence of numbers (e.g., range(5)).

**Mapping Type:**

- `dict`: Key-value pairs (e.g., {"name": "John", "age": 30}).

**Set Types:**

- `set`: Unordered, mutable collections of unique elements (e.g., {1, 2, 3}).
- `frozenset`: Unordered, immutable collections of unique elements.

**Boolean Type:**

- `bool`: True or False.

**Binary Types:**

- `bytes`: Immutable sequence of bytes.
- `bytearray`: Mutable sequence of bytes.
- `memoryview`: Memory view object.

**None Type:**

- `NoneType`: Represents the absence of a value (e.g., None).

```python
my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
my_dict = {"a": 1, "b": 2}
```

## Operators:

Operators are used to perform operations on variables and values:

**Arithmetic Operators:**

- `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division), `%` (modulo), `**` (exponentiation), `//` (floor division).

**Assignment Operators:**

- `=` (assignment), `+=` (add and assign), `-=` (subtract and assign), `*=` (multiply and assign), `/=` (divide and assign), `%=` (modulo and assign), `//=`, `**=`. `&=`, `|=`, `^=`, `>>=`, `<<=`.

**Comparison Operators:**

- `==` (equal), `!=` (not equal), `>` (greater than), `<` (less than), `>=` (greater than or equal), `<=` (less than or equal).

**Logical Operators:**

- `and`, `or`, `not`.

**Identity Operators:**

- `is`, `is not`.

**Membership Operators:**

- `in`, `not in`.

**Bitwise Operators:**

- `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (left shift), `>>` (right shift).
