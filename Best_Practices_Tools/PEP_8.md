# PEP 8 Style Guide

## Theory

PEP 8 is the style guide for Python code. It provides a set of conventions for writing Python code that is consistent, readable, and maintainable. Following PEP 8 makes your code easier to understand and collaborate on with other Python developers.

### Key Concepts

- Indentation:

  - Use 4 spaces per indentation level.
  - Avoid tabs.

- Line Length:

  - Limit lines to 79 characters.

- Blank Lines:

  - Separate top-level function and class definitions with two blank lines.
  - Separate method definitions inside a class with one blank line.

- Imports:

  - Imports should usually be on separate lines.
  - Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants.
  - Imports should be grouped in the following order: standard library imports, related third party imports, local application/library specific imports.

- Whitespace:

  - Avoid extraneous whitespace in the following situations:
    - Immediately inside parentheses, brackets or braces.
    - Immediately before a comma, semicolon, or colon.
    - Immediately before the open parenthesis that starts the argument list of a function call.
    - Immediately before the open square bracket that starts an index or slice.
    - More than one space around an assignment (or other) operator to align it with another.

- Naming Conventions:

  - snake_case for functions, variables, and modules.
  - PascalCase for classes.
  - UPPER_CASE for constants.

- Comments:

  - Use complete sentences, starting with a capital letter.
  - Block comments generally apply to some (or all) code that follows them, and are indented to the same level as that code.
  - Inline comments are comments on the same line of code.

- Docstrings:
  - Write docstrings for all public modules, functions, classes, and methods.
  - Use triple double quotes (""") for docstrings.

## Example (PEP 8 Compliant):

```python
def calculate_area(width, height):
    """Calculate the area of a rectangle."""
    area = width * height
    return area

class Rectangle:
    """A class representing a rectangle."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        """Return the area of the rectangle."""
        return calculate_area(self.width, self.height)

# Example usage
rectangle = Rectangle(5, 10)
area = rectangle.get_area()
print(f"Area: {area}")
```

## Tools

- [`pep8`](https://peps.python.org/pep-0008/) (now [`pycodestyle`](https://pycodestyle.pycqa.org/en/latest/)): A tool to check for PEP 8 compliance.
- [`autopep8`](https://pypi.org/project/autopep8/): A tool to automatically fix PEP 8 violations.
- [`black`](https://black.readthedocs.io/en/stable/getting_started.html): An uncompromising Python code formatter.
- Linters ([pylint](https://pypi.org/project/pylint/), [flake8](https://flake8.pycqa.org/en/latest/)): Tools that analyze code for potential errors and style violations.
