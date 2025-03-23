# Create a Library class that manages a list of books
# - Books should be stored as a list of Book objects (created earlier).
# - Implement methods to add books, remove books, and search books by title.

class Book:
    def __init__(self, title: str) -> None:
        self.title = title

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str) -> None:
        self.__title = title

    def __str__(self) -> str:
        return f'Book:\ntitle: {self.title}'


class Library:
    def __init__(self) -> None:
        self.__books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.__books.append(book)

    def remove_book(self, book: Book) -> None:
        if book in self.__books:
            self.__books.remove(book)
        else:
            print(f'Book "{book.title}" not found in library')

    def search_book(self, title: str) -> Book | None:
        title = title.lower()
        for book in self.__books:
            if book.title.lower() == title:
                return book
        return None


if __name__ == '__main__':
    library = Library()

    book1 = Book('The Call of the Wild')
    book2 = Book('The Great Gatsby')

    library.add_book(book1)
    library.add_book(book2)

    print(library.search_book('The Call of the Wild'))

    library.remove_book(book1)

    print(library.search_book('The Call of the Wild'))
