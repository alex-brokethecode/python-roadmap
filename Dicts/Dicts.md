# 📌 Topic 2: Dictionaries in Python

## 📖 Theory

A **dictionary** in Python is an **unordered**, **mutable** collection that stores **key-value pairs**.  
Keys must be **unique** and **immutable** (e.g., strings, numbers, or tuples), while values can be of any type.

---

### 🔹 **Creating Dictionaries**

```python
# Empty dictionary
my_dict = {}

# Dictionary with values
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
```

---

### 🔹 **Accessing Values**

```python
print(person["name"])  # Output: Alice
print(person.get("age"))  # Output: 25

# Using .get() avoids KeyError if the key doesn't exist
print(person.get("country", "Not found"))  # Output: Not found
```

---

### 🔹 **Modifying Dictionaries**

```python
# Add or update key-value pairs
person["age"] = 26  # Update value
person["job"] = "Engineer"  # Add new key

# Delete a key
del person["city"]

# Using .pop() to remove and return a value
age = person.pop("age")  # Returns 26
```

---

### 🔹 **Looping Through Dictionaries**

```python
for key in person:
    print(key, "->", person[key])

# Using .items() for key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
```

---

### 🔹 **Dictionary Methods**

```python
person.keys()  # Returns a list of keys
person.values()  # Returns a list of values
person.items()  # Returns key-value pairs
```

---

### 🔹 **Dictionary Comprehensions**

```python
# Create a dictionary with squares of numbers 1 to 5
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

## 🏆 **Exercises**

### 🟢 Easy Level

1. **Create a dictionary representing a book with "title", "author", and "year" keys. Print the title.** [Solution](./Exercises/01.py)
2. **Add a new key "genre" to the book dictionary and set its value to "fiction".** [Solution](./Exercises/02.py)
3. **Check if the key "publisher" exists in the book dictionary. Print "Exists" or "Does not exist".** [Solution](./Exercises/03.py)

---

### 🔵 Medium Level

4. **Merge two dictionaries into one. Example:**
   ```python
   dict1 = {"a": 1, "b": 2}
   dict2 = {"c": 3, "d": 4}
   ```
   **Expected Output: `{'a': 1, 'b': 2, 'c': 3, 'd': 4}`**
5. **Remove all key-value pairs where the value is `None` from a dictionary.**
6. **Find the key with the maximum value in a dictionary. Example:**
   ```python
   scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
   ```
   **Expected Output: `'Bob'` (since 92 is the highest value).**

---

### 🔴 Hard Level

7. **Invert a dictionary (keys become values and values become keys).**
   ```python
   original = {"a": 1, "b": 2, "c": 3}
   ```
   **Expected Output: `{1: "a", 2: "b", 3: "c"}`**
8. **Count the frequency of words in a sentence and store the result in a dictionary.**

   ```python
   sentence = "apple banana apple orange banana apple"
   ```

   **Expected Output: `{'apple': 3, 'banana': 2, 'orange': 1}`**

9. **Write a function that finds the most common value in a dictionary. Example:**
   ```python
   data = {"a": 2, "b": 3, "c": 2, "d": 4, "e": 3, "f": 3}
   ```
   **Expected Output: `3` (since it appears 3 times).**
