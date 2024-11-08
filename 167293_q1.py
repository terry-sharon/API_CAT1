class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        if not self.is_borrowed:  
            self.is_borrowed = True
            print(f"'{self.title}' has been borrowed.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not borrowed.")

class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is currently borrowed by someone else.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} has not borrowed '{book.title}'.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"{self.name} has not borrowed any books.")

# Interactive code
if __name__ == "__main__":
    # book and member data
    books = [
        Book("Quiet", "Susan Cain"),
        Book("Romeo and Juliet", "William Shakespeare"),
        Book("Pride and Prejudice", "Jane Austen"),
        Book("Psychology of Money" , "Morgan Housel"),
        Book("Atomic Habits" , "James Clear"),
    ]
    member = LibraryMember("Terry", 101)

    # Menu-driven program for borrowing and returning books
    while True:
        print("\nLibrary Management System")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. List borrowed books")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            # Borrow a book
            print("Available books:")
            for i, book in enumerate(books):
                if not book.is_borrowed:
                    print(f"{i + 1}. {book.title} by {book.author}")
            book_choice = input("Enter the number of the book to borrow: ")
            try:
                book_index = int(book_choice) - 1
                if 0 <= book_index < len(books):
                    member.borrow_book(books[book_index])
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '2':
            # Return a book
            if member.borrowed_books:
                print("Your borrowed books:")
                for i, book in enumerate(member.borrowed_books):
                    print(f"{i + 1}. {book.title} by {book.author}")
                book_choice = input("Enter the number of the book to return: ")
                try:
                    book_index = int(book_choice) - 1
                    if 0 <= book_index < len(member.borrowed_books):
                        member.return_book(member.borrowed_books[book_index])
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("You have no books to return.")

        elif choice == '3':
            # List borrowed books
            member.list_borrowed_books()

        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid option. Please try again.")           