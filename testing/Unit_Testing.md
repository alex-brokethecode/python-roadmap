# Testing

## Theory

Testing is crucial for software quality. It ensures code functions as intended, reduces bugs, and facilitates maintenance. Python provides tools and frameworks for effective testing.

**Key Concepts:**

- **Unit Testing:** Testing individual code units (functions, classes).
- **Integration Testing:** Testing interactions between code units.
- **Test Cases:** Inputs and expected outputs for code verification.
- **Test Suites:** Collections of test cases.
- **Assertions:** Statements that verify conditions (pass/fail).

**Tools and Frameworks:**

[`unittest`](https://docs.python.org/3/library/unittest.html)

- Python's built-in unit testing framework.
- Class-based approach.
- Provides a structured way to organize tests.

[`pytest`](https://docs.pytest.org/en/stable/)

- Third-party framework, known for its simplicity and powerful features.
- Uses a more concise syntax.
- Offers test discovery, fixtures, and plugins.

`unittest` **Assertions (Examples):**

- `self.assertEqual(a, b)`: Checks if a equals b.
- `self.assertTrue(x)`: Checks if x is true.
- `self.assertFalse(x)`: Checks if x is false.
- `self.assertIs(a, b)`: Checks if a is the same object as b.
- `self.assertIsNone(x)`: Checks if x is None.
- `self.assertIn(a, b)`: Checks if a is in b.
- `self.assertRaises(exception, callable, \*args, \*\*kwargs)`: Checks if callable raises exception.

> [!NOTE]
> To run your test, use this command:
> `python -m unittest -v <path>`

`pytest` **Assertions (Examples):**

- `pip install -U pytest`
- `assert a == b`: Checks if a equals b.
- `assert x`: Checks if x is true.
- `assert a is b`: Checks if a is the same object as b.
- `assert x is None`: Checks if x is None.
- `assert a in b`: Checks if a is in b.
- `with pytest.raises(exception): ...`: Checks if the code block raises exception.

> [!NOTE]
> To run your test, use this command:
> `pytest -v <path>` or just `pytest -v`
> Also check packages, modules names (add `__init__.py` file in some cases) and make sure names start with `test_` prefix (for files and functions)

### Comparison and Use Cases:

`unittest`:

- Built-in, requires no external installation.
- Suitable for projects where strict adherence to class-based testing is preferred.
- Can be more verbose.

`pytest`:

- Simpler syntax, easier for beginners.
- Powerful features (fixtures, plugins) for complex testing scenarios.
- Widely used in the Python community.
- Good for rapid development.

## Exercises

```python
def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def reverse_string(s):
    return s[::-1]
```

1. Write unit tests for the multiply, divide, and reverse_string functions using either unittest ([Solution](./exercises/unitest_test.py)) or pytest ([Solution](./exercises/test_pytest.py)).
2. Include test cases for various scenarios, including edge cases (e.g., dividing by zero).
3. Use appropriate assertions to verify the expected behavior.
4. Run your tests and ensure they pass.
