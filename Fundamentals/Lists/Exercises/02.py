# Add the number 11 to the end of the list and remove the first number.

numbers: list[int] = [i for i in range(1, 11)]

numbers.append(11)
numbers.pop(0)

print(numbers)
