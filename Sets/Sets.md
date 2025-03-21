# Topic 4: Sets in Python

## Theory

A **set** in Python is an **unordered**, **mutable** collection of unique elements.  
Unlike lists and tuples, **sets do not allow duplicate values** and do not maintain any specific order.  
Sets are useful for **removing duplicates, performing mathematical operations (union, intersection, difference), and fast lookups**.

---

### **Creating Sets**

```python
# Empty set (must use set(), NOT {})
my_set = set()

# Set with elements
fruits = {"apple", "banana", "cherry"}

# Set with mixed data types
mixed_set = {1, "hello", 3.14, True}

# Creating a set from a list (removes duplicates)
numbers = set([1, 2, 2, 3, 4, 4, 5])
print(numbers)  # Output: {1, 2, 3, 4, 5}
```

---

### 🔹 **Adding and Removing Elements**

```python
fruits = {"apple", "banana"}

# Adding elements
fruits.add("orange")

# Removing elements
fruits.remove("banana")  # Raises an error if not found
fruits.discard("banana") # No error if not found

# Removing a random element
fruits.pop()

# Clearing all elements
fruits.clear()

print(fruits)
```

---

### 🔹 **Set Operations**

```python
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union (elements from both sets)
print(set_a | set_b)  # {1, 2, 3, 4, 5, 6}

# Intersection (common elements)
print(set_a & set_b)  # {3, 4}

# Difference (elements in A but not in B)
print(set_a - set_b)  # {1, 2}

# Symmetric Difference (elements in either A or B, but not both)
print(set_a ^ set_b)  # {1, 2, 5, 6}
```

---

### 🔹 **Checking Membership and Subsets**

```python
numbers = {1, 2, 3, 4, 5}

# Check if an element exists in a set
print(3 in numbers)  # True

# Check if a set is a subset of another
small_set = {2, 3}
print(small_set.issubset(numbers))  # True

# Check if a set is a superset of another
print(numbers.issuperset(small_set))  # True
```

---

## **Exercises**

### **Easy Level**

1. Create a set with numbers from 1 to 5 and print it. [Solution](./Exercises/01.py)
2. Add the number 6 to the set, then remove the number 2.
3. Check if the number 3 is in the set and print the result.

---

### **Medium Level**

4. Merge two sets `{1, 2, 3}` and `{3, 4, 5}` using a set operation.
5. Find the common elements between `{10, 20, 30, 40}` and `{30, 40, 50, 60}`.
6. Remove duplicates from the list `[5, 10, 10, 15, 20, 20, 25]` and return a set.

---

### **Hard Level**

7. Given two sets `{1, 2, 3, 4, 5}` and `{4, 5, 6, 7, 8}`, find:

   - Elements present in the first set but not in the second.
   - Elements present in either of the sets but not both.

8. Count how many times each word appears in `"apple banana apple orange banana apple"` and store the result in a set.
9. Find the most common element in `{1, 2, 3, 2, 4, 3, 2, 5, 3, 3, 3, 4}`.
