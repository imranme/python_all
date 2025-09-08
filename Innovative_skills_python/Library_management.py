# - Library Management
# A library has books, and each book has a title, author, and availability status. Users can borrow and return books. Write classes to model this system. 

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True # in this stage chek free book

    def borrow(self):
        if self.available:
            self.available = False
            return f"{self.title} borrowed."
        return f"{self.title} not available."
    
    def return_book(self):
        self.available = True
        return f"{self.title} returned."

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for b in self.books:
            status = "Available" if b.available  else "Not Available"
            print(f"{b.title} by {b.author} → {status}")

class User:
    def __init__(self, name):
        self.name = name

    def borrow_book(self, book):
        print(f"{self.name} tries to borrow {book.title} → {book.borrow()}")

    def return_book(self, book):
        print(f"{self.name} returns {book.title} → {book.return_book()}")      

b1 = Book("Python Basics", "Rahim")
b2 = Book("OOP in Python", "Karim")

lib = Library()
lib.add_book(b1)
lib.add_book(b2)

u1 = User("Tushar")

lib.show_books()
u1.borrow_book(b1)
lib.show_books()
u1.return_book(b1)
lib.show_books()
