# Given a list of dictionaries with name and age, use map() to extract only the names

# [ My Solution ]

people = [
    {
        'name': 'John',
        'age': 18
    },
    {
        'name': 'Megan',
        'age': 26
    },
    {
        'name': 'Luna',
        'age': 24
    },
]

names = list(map(lambda p: p.get('name', 'N/A'), people))
print(f'{names=}')

# [ Tip ]
names = [person.get('name', 'N/A') for person in people]
print(f'{names=}')
