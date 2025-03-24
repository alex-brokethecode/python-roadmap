# Given a tuple with duplicate values (10, 20, 30, 10, 20, 40), remove duplicates while maintaining the order.

numbers = (10, 20, 30, 10, 20, 40)

# [ My Solution ]

seen = set()
unique_numbers = []

for number in numbers:
    if number not in seen:
        unique_numbers.append(number)
        seen.add(number)

print(unique_numbers)
