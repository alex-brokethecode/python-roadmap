# Modules and Packages

## Theory

### Modules

- A module is a file containing Python definitions and statements.
- Modules allow you to organize your code into logical units.
- You can import modules into other Python scripts to reuse their code.
- To import a module, you use the `import` statement.
- Example: `import math`

### Packages

- A package is a collection of modules organized into directories.
- Packages allow you to create a hierarchical structure for your modules.
- A package must contain an `__init__.py` file (which can be empty) to be recognized as a Python package.
- To import a module from a package, you use the dot notation.
- Example: `import my_package.my_module`

### Importing Modules and Packages:

- `import module_name`: Imports the entire module.
- `from module_name import function_name`: Imports a specific function from a module.
- `from module_name import *`: Imports all names from a module (not recommended).
- `import module_name as alias`: Imports a module with an alias.
- `from package_name import module_name`: Imports a module from a package.
- `from package_name.module_name import function_name`: Imports a specific function from a module within a package.

### `__name__` Variable:

- The `__name__` variable is a special variable that is set to `"__main__"` when a script is executed directly.
- It is set to the module's name when the script is imported as a module.
- You can use the `__name__ == '__main__'` condition to determine whether a script is being executed directly or imported.

### Example

```python
# my_module.py
def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet("Alice")
```

```python
# main.py
import my_module

my_module.greet("Bob")
```

## Exercises:

### Easy

1. **Create and Import a Module:** Create a module named my_utils.py with a function that calculates the square of a number. Then, create a script that imports this module and uses the function. [Solution](./Exercises/01.py)

### Medium

2. _Create a Package_: Create a package named `my_math` with two modules: `addition.py` and `subtraction.py`. Each module should contain a function that performs the corresponding operation. Then, create a script that imports and uses these modules. [Solution](./Exercises/02.py)

### Hard

3. **`__name__` Variable Usage:** Create a module named `calculator.py` with functions for addition, subtraction, multiplication, and division. Add a conditional statement that prints the results of some calculations only when the module is executed directly (not when it's imported). [Solution](./Exercises/03.py)
