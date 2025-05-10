class Library:
    def __init__(self, books):
        self.available_books = books
        self.borrowed_books = {}  # book_name: student_name

    def display_books(self):
        print("\nAvailable Books:")
        if not self.available_books:
            print("No books available at the moment.")
        else:
            for book in self.available_books:
                print(f" - {book}")
            print(f"\nTotal available books: {len(self.available_books)}")

    def borrow_book(self, book_name, student_name):
        book_name_lower = book_name.lower()
        for book in self.available_books:
            if book.lower() == book_name_lower:
                self.available_books.remove(book)
                self.borrowed_books[book] = student_name
                print(f"\n'{book}' has been borrowed by {student_name}")
                return
        print(f"\nSorry, '{book_name}' is not available right now.")

    def return_book(self, book_name, student_name):
        book_name_lower = book_name.lower()
        for book, borrower in list(self.borrowed_books.items()):
            if book.lower() == book_name_lower:
                if borrower == student_name:
                    self.available_books.append(book)
                    del self.borrowed_books[book]
                    print(f"\n{student_name} has returned '{book}'")
                    return
                else:
                    print(f"\n'{book}' was borrowed by {borrower}, not {student_name}")
                    return
        print(f"\n'{book_name}' is not in the borrowed list.")

    def show_borrowed_books(self):
        print("\nBorrowed Books:")
        if not self.borrowed_books:
            print("No books are currently borrowed.")
        else:
            for book, borrower in self.borrowed_books.items():
                print(f" - '{book}' borrowed by {borrower}")

class Student:
    def request_book(self):
        name = input("Enter your name: ")
        book = input("Enter the name of the book to borrow: ")
        return book, name

    def return_book(self):
        name = input("Enter your name: ")
        book = input("Enter the name of the book to return: ")
        return book, name

# Main Program
library = Library(["C++", "Python", "Data Structures", "Java", "Machine Learning"])
student = Student()

while True:
    print("\n--- Library Menu ---")
    print("1. Display Books")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. Exit")
    print("5. Show Borrowed Books")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        library.display_books()
    elif choice == '2':
        book, name = student.request_book()
        library.borrow_book(book, name)
    elif choice == '3':
        book, name = student.return_book()
        library.return_book(book, name)
    elif choice == '4':
        print("\nThanks for using the Library Management System!")
        break
    elif choice == '5':
        library.show_borrowed_books()
    else:
        print("\nInvalid choice. Please try again.")