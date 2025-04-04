# Control Flow in Python

## Theory

Control flow statements allow you to control the order in which code is executed, enabling you to make decisions, repeat blocks of code, and handle different scenarios.

1. `if` Statements:

   - if statements are used for conditional execution. They allow you to execute different blocks of code based on whether a condition is true or false.

   ```python
   x = 10

   if x > 5:
       print("x is greater than 5")
   elif x == 5:
       print("x is equal to 5")
   else:
       print("x is less than 5")
   ```

   - `if` condition: Executes the block if the condition is true.
   - `elif` condition: Optional, executes the block if the previous if or elif conditions are false and the current condition is true.
   - `else`: Optional, executes the block if all previous conditions are false.

2. `for` Loops:

   - `for` loops are used to iterate over a sequence (e.g., a list, tuple, string, or range).
   - `for variable in sequence`: Iterates over each item in the sequence.

   ```python
   my_list = [1, 2, 3, 4, 5]

   for item in my_list:
       print(item)

   for i in range(3):  # Iterate from 0 to 2
       print(i)

   my_string = "hello"

   for char in my_string:
       print(char)
   ```

3. while Loops:

- `while` loops are used to repeatedly execute a block of code as long as a condition is true.
- `while` condition: Executes the block as long as the condition is true.

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

4. `break` and `continue` Statements:

- `break`: Terminates the loop immediately.
- `continue`: Skips the rest of the current iteration and continues with the next iteration.

```python
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)

for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
```

5. `pass` Statement:

`pass`: A null operation; it does nothing. It can be used as a placeholder where a statement is syntactically required but you don't want any code to be executed.

```python
if True:
    pass  # Placeholder, do nothing
```
