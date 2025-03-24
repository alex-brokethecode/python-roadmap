# Use filter() to extract words longer than 5 characters from a list.

# [ My solution ]

words: list[str] = ['apple', 'banana', 'cherry', 'date', 'elderberry']

longer_than_5: list[str] = list(filter(lambda x: len(x) > 5, words))
print(f'{longer_than_5=}')

# [ Tip ]
# list comprehensions are generally preferred in Python because they are more readable and slightly faster.

longer_than_5 = [word for word in words if len(word) > 5]
print(f'{longer_than_5=}')
