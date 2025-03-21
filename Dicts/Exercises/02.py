# Add a new key "genre" to the book dictionary and set its value to "fiction".

# [ My Solution ]

book: dict[str, str] = {
    'title': 'The Call of the Wild',
    'author': 'Jack London',
    'year': '1903',
}

book['genre'] = 'fiction'

print(book.get('genre', 'Unknown'))
