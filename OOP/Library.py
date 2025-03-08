class Library:
    def __init__(self, book_list):
        # Initialize library with a list of books
        self.books = book_list
    
    def display_books(self):
        # Display available books
        print("\nAvailable Books:")
        for book in self.books:
            print(f"- {book}")
    
    def borrow_book(self, book_name):
        # Borrow a book if available
        if book_name in self.books:
            print(f"\nYou have borrowed '{book_name}'. Please return it on time.")
            self.books.remove(book_name)
        else:
            print(f"\nSorry, '{book_name}' is not available or already borrowed.")
    
    def return_book(self, book_name):
        # Return a book
        self.books.append(book_name)
        print(f"\nThank you for returning '{book_name}'!")

class User:
    def __init__(self, library):
        self.library = library
    
    def menu(self):
        while True:
            print("""
            ====== Library Menu ======
            1. Display all books
            2. Borrow a book
            3. Return a book
            4. Exit
            """)
            choice = input("Enter your choice (1-4): ")
            
            if choice == "1":
                self.library.display_books()
            elif choice == "2":
                book_name = input("\nEnter the name of the book you want to borrow: ")
                self.library.borrow_book(book_name)
            elif choice == "3":
                book_name = input("\nEnter the name of the book you want to return: ")
                self.library.return_book(book_name)
            elif choice == "4":
                print("\nThank you for using the library! Goodbye!")
                break
            else:
                print("\nInvalid choice. Please try again.")

# List of books in the library
book_list = ["The Great Gatsby", "To Kill a Mockingbird", "1984", "Harry Potter", "The Hobbit"]

# Create Library and User objects
library = Library(book_list)
user = User(library)

# Start the program
user.menu()
