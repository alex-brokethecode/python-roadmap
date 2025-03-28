# Exception Handling

## Theory:

Exception handling allows you to gracefully manage errors that occur during the execution of your program. Python provides a `try...except` block to catch and handle exceptions.

- **`try` Block:** The code that might raise an exception is placed inside the `try` block.
- **`except` Block:** The code that handles the exception is placed inside the `except` block. You can specify the type of exception to catch.
- **`else` Block (Optional):** The code in the `else` block is executed if no exceptions are raised in the `try` block.
- **`finally` Block (Optional):** The code in the `finally` block is always executed, regardless of whether an exception was raised or not.
- **Raising Exceptions:** You can use the `raise` keyword to explicitly raise an exception.
- **Custom Exceptions:** You can define your own custom exceptions by creating new classes that inherit from the built-in `Exception` class.

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount, message="Insufficient funds."):
        self.balance = balance
        self.amount = amount
        super().__init__(message)

def withdraw(balance, amount):
    if balance < amount:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
    print(new_balance)
except InsufficientFundsError as e:
    print(f"Cannot withdraw {e.amount} from balance {e.balance}: {e}")
```

### Example

```python
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e: # Catch all other exceptions
    print(f"An error occurred: {e}")
else:
    print("No errors occurred.")
finally:
    print("This code will always run.")
```

## Exercises

### Easy

1. **Divide by Zero:** Write a Python program that takes two numbers as input and divides the first number by the second. Handle the ZeroDivisionError exception and print an appropriate message. [Solution](./Exercises/01.py)

### Medium

2. **File Input with Exception Handling:** Write a Python program that prompts the user for a filename, attempts to open the file, reads its content, and prints it. Handle both FileNotFoundError and IOError exceptions. [Solution](./Exercises/02.py)

### Hard

3. **Custom Exception for Invalid Input:** Create a custom exception class called InvalidInputError. Write a Python program that takes a number as input and raises InvalidInputError if the number is negative. [Solution](./Exercises/03.py)
