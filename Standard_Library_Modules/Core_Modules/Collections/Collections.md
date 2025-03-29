# collections Module

## Theory

The `collections` module provides specialized container datatypes that offer alternatives to Python's built-in containers like lists, tuples, and dictionaries. It's particularly useful for working with data structures that require specific properties or behaviors.

- `collections.Counter`: A dictionary subclass for counting hashable objects.
- `collections.defaultdict`: A dictionary subclass that calls a factory function to supply missing values.
- `collections.OrderedDict`: A dictionary subclass that remembers the order in which keys were first inserted.
- `collections.namedtuple`: A factory function for creating tuple subclasses with named fields.
- `collections.deque`: A list-like container with fast appends and pops on either end.

### Example

```python
import collections

# Counter
c = collections.Counter('hello world')
print(c) # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# defaultdict
d = collections.defaultdict(int) # int = default factory (function) that created a default value 0 for keys that doesn't exist
for char in 'hello world':
    d[char] += 1
print(d) # defaultdict(<class 'int'>, {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# OrderedDict
od = collections.OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od) # OrderedDict({'a': 1, 'b': 2, 'c': 3})

# namedtuple
Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p) # Point(x=1, y=2)
print(p.x, p.y) # 1 2

# deque
dq = collections.deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
print(dq) # deque([0, 1, 2, 3, 4])
```

## Exercises

### Easy

1. **Word Frequency:** Write a Python program that takes a sentence as input and uses collections.Counter to count the frequency of each word. [Solution](./Exercises/01.py)

## Medium

2. **Group by First Letter:** Write a Python program that takes a list of words as input and uses collections.defaultdict to group the words by their first letter. [Solution](./Exercises/02.py)

## Hard

3. **Ordered Word Counter:** Write a Python program that takes a sentence as input and uses collections.OrderedDict to count the frequency of each word, maintaining the order in which the words first appear in the sentence. [Solution](./Exercises/03.py)
