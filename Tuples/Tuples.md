# 📂 Topic 3: Tuples in Python

## 📚 Theory

A **tuple** in Python is an **ordered, immutable** collection that can store different data types. Unlike lists, tuples **cannot be modified** (no adding, removing, or changing elements after creation). Tuples are useful when you need **read-only data**.

---

### 🔹 **Creating Tuples**

```python
# Empty tuple
empty_tuple = ()

# Tuple with elements
days = ("Monday", "Tuesday", "Wednesday")

# Mixed data types
person = ("Alice", 25, True)

# Tuple with a single element (comma needed)
single_element = (42,)  # NOT (42) -> That would be an int
```

---

### 🔹 **Accessing Elements**

```python
tuple1 = (10, 20, 30, 40, 50)

print(tuple1[0])    # First element -> 10
print(tuple1[-1])   # Last element -> 50
print(tuple1[1:4])  # Slice -> (20, 30, 40)
```

---

### 🔹 **Tuple Packing & Unpacking**

```python
# Packing
tuple2 = "Python", 3.9, "Programming"

# Unpacking
lang, version, category = tuple2
print(lang)    # Python
print(version) # 3.9
print(category) # Programming
```

---

### 🔹 **Tuple Methods**

```python
tuple3 = (1, 2, 3, 2, 2, 4)

print(tuple3.count(2))  # Count occurrences of 2 -> 3
print(tuple3.index(3))  # First index of 3 -> 2
```

---

## 📝 Exercises

### 🛠️ Easy Level

1. Create a tuple with numbers from **1 to 5** and print the **third** element. [Solution](./Exercises/01.py)
2. Convert the list `["apple", "banana", "cherry"]` into a **tuple**. [Solution](./Exercises/02.py)
3. Create a tuple with a **single element** (`42`) and print its type. [Solution](./Exercises/03.py)

### 🛠️ Medium Level

4. Given a tuple `(10, 20, 30, 40, 50)`, **reverse** it without using slicing (`[::-1]`). [Solution](./Exercises/04.py)
5. Write a program that **unpacks** the tuple `("Alice", 25, "Engineer")` into separate variables and prints them. [Solution](./Exercises/05.py)
6. Given `tuple1 = (1, 2, 3, 2, 4, 2, 5)`, count how many times `2` appears **without using `.count()`**. [Solution](./Exercises/06.py)

### 🛠️ Hard Level

7. Merge two tuples `(1, 2, 3)` and `(4, 5, 6)` **without using `+`**. [Solution](./Exercises/07.py)
8. Given a tuple with duplicate values `(10, 20, 30, 10, 20, 40)`, remove duplicates while maintaining the order. [Solution](./Exercises/08.py)
9. Write a program that finds the **largest number** in a tuple **without using `max()`**.
   [Solution](./Exercises/09.py)
