# Topic: Generators and Iterators

## Theory

- **Iterators:**
  - An iterator is an object that allows you to traverse through a sequence of data.
  - It implements the `__iter__()` and `__next__()` methods.
  - `__iter__()` returns the iterator object itself.
  - `__next__()` returns the next element in the sequence. When there are no more elements, it raises the `StopIteration` exception.

**Example:**

```python
# Iterator Example
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

my_list = [1, 2, 3]
my_iterator = MyIterator(my_list)

for item in my_iterator:
    print(item)
```

- **Generators:**
  - A generator is a special type of iterator that generates values on-the-fly.
  - It uses the `yield` keyword to produce values.
  - Generators are memory-efficient, as they don't store the entire sequence in memory.
  - Generator functions automatically implement the iterator protocol.

**Example:**

```python
# Generator Example
def my_generator(n):
    for i in range(n):
        yield i * 2

for item in my_generator(3):
    print(item)
```

## Exercises

### Easy

1. **Generate Squares:** Create a generator function that yields the squares of numbers from 0 to n.

### Medium

2. **Fibonacci Generator:** Create a generator function that yields the Fibonacci sequence up to a given limit.

### Hard

3. **Prime Number Generator:** Create a generator function that yields prime numbers indefinitely.
