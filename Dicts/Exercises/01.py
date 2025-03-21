# Create a dictionary representing a book with "title", "author", and "year" keys. Print the title.

# [ My Solution ]

book: dict[str, str] = {
    'title': 'The Call of the Wild',
    'author': 'Jack London',
    'year': '1903'
}

print(book.get('title', 'Unknown'))
