class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

class Library:
    def __init__(self):
        self._books = list()

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book._is_checked_out:
                    book._is_checked_out = True
                    print(f"{book.title} has been checked out")
                else:
                    print(f"{book.title} is not currently available")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book._is_checked_out:
                    book._is_checked_out = False
                    print(f"{book.title} has been returned")
                else:
                    print(f"{book.title} wasn't checked out")
                

    def list_available_books(self):
        for book in self._books:
            if not book._is_checked_out:
                print(book.title)
