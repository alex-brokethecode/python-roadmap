# Check if the key "publisher" exists in the book dictionary. Print "Exists" or "Does not exist".

# [ My Solution ]

book: dict[str, str] = {
    'title': 'The Call of the Wild',
    'author': 'Jack London',
    'year': '1903',
}

# Use book.keys() is not necessary
print('Exists' if 'publisher' in book else 'Does not exist')
