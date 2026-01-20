"""
Program: eBook Store
Project: Bookstore’s catalog
Purpose: To create bookstore menu system and manipulate data (Add, Search, Remove, Display)
Revision History
    created by Myungjeong Han Oct 2025
"""
class BookNode:
    def __init__(self, isbn:str, title:str, author:str):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.next = None
        self.prev = None

    def __str__(self):
        return f"[ISBN: {self.isbn}, Title: {self.title}, Author: {self.author}]"


class BookCatalog:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_book(self, new_book:BookNode):
        # Case 1: Duplicate ISBN, cannot add(reject)
        if self.get_books_by_isbn(new_book.isbn) is not None:
            return False

        # Case 2: Empty catalog, add first book
        if self.head is None:
            self.head = self.tail = new_book
        else:
        # Case 3: Catalog not empty, find last book by the same author
            current = self.head
            last_book_by_author = None
            while current is not None:
                if current.author == new_book.author:
                    last_book_by_author = current
                current = current.next

        # Case 3-1: Same author exists, insert after last author's book
            if last_book_by_author is not None:
                new_book.next = last_book_by_author.next
                new_book.prev = last_book_by_author
                if last_book_by_author.next is not None:    # if it was not the tail
                    last_book_by_author.next.prev = new_book
                else:                                       # if it was tail, update tail
                    self.tail = new_book
                last_book_by_author.next = new_book
            else:
        # Case 3-2: Same author doesn't exist. add a book to end of catalog
                self.tail.next = new_book
                new_book.prev = self.tail
                self.tail = new_book
        return True

    def get_books_by_author(self, author):
        """
        Return all books by the given author.

        Assumption: The search is case-insensitive and ignores extra spaces.
        Example: "paulo coelho", "Paulo Coelho", and "PAULO COELHO" are treated as the same author.
        """
        author = author.lower()
        current = self.head
        results_by_author = []
        while current is not None:
            if current.author.lower() == author:
                results_by_author.append(current)
            current = current.next
        return results_by_author

    def get_books_by_title(self, title):
        """
        Return all books with the exact title given by the user.

        Assumption: The search is case-insensitive, ignores extra spaces, and partial matches are not considered.
        Example: If the user enters "Deep", it will NOT match "Deep Work".
        """
        title = title.lower()
        current = self.head
        results_by_title = []
        while current is not None:
            if current.title.lower() == title:
                results_by_title.append(current)
            current = current.next
        return results_by_title

    def get_books_by_isbn(self, isbn):
        """
        Return the book that matches the given ISBN, or None if not found.

        Assumption: The search ignores extra spaces.
        """
        current = self.head
        while current is not None:
            if current.isbn == isbn:
                return current
            current = current.next
        return None

    def remove_book_by_isbn(self, isbn):
        # Check if the given ISBN exists in the list
        book_to_remove = self.get_books_by_isbn(isbn)
        if book_to_remove is None:
            return None

        # Case 1: The list has only one book, and that book is being removed
        if self.head == self.tail and book_to_remove == self.head:
            self.head = self.tail = None
        # Case 2: The list has multiple books, and the book to remove is at the head
        elif book_to_remove == self.head:
            self.head = book_to_remove.next
            self.head.prev = None
        # Case 3: The list has multiple books, and the book to remove is at the tail
        elif book_to_remove == self.tail:
            self.tail = book_to_remove.prev
            self.tail.next = None
        # Case 4: The list has multiple books, and the book to remove is in the middle
        else:
            book_to_remove.prev.next = book_to_remove.next
            book_to_remove.next.prev = book_to_remove.prev
        return book_to_remove

    def __str__(self):
        current = self.head
        display_output = ""     # To Collect book info to print later
        while current is not None:
            display_output += f"[ISBN: {current.isbn}, Title: {current.title}, Author: {current.author}]"
            if current.next is not None:
                display_output += " <->\n "
            current = current.next
        return display_output


class StackNode:
    """
    Separate node class for the checkout cart (stack structure). Only stores title.
    """
    def __init__(self, title:str):
        self.title = title
        self.next = None


class CheckoutCart:
    def __init__(self):
        self.first = None   #Top of the stack
        self.last = None
        self.size = 0

    def add_to_cart(self, title):
        new_book = StackNode(title)
        if self.size == 0:
            self.first = self.last = new_book
        else:   # Insert new book at the top of the stack
            new_book.next = self.first
            self.first = new_book
        self.size += 1

    def remove_from_cart(self):
        if self.is_cart_empty():
            return None
        else:   # Remove the top book from the stack
            book_to_remove = self.first
            self.first = self.first.next
            book_to_remove.next = None
            self.size -= 1
            if self.size == 0:  # If the cart is now empty, update last pointer
                self.last = None
            return book_to_remove.title

    def peek_cart(self):
        if self.is_cart_empty():
            return None
        return self.first.title

    def cart_size(self):
        return self.size

    def is_cart_empty(self):
        if self.size == 0:
            return True
        return False


def get_validated_menu_input():
    while True:
        try:
            user_choice = int(input("Select an option (1–11): ").strip())
            if 1 <= user_choice <= 11:
                return user_choice
            else:
                print("Invalid option. Please enter a number between 1 and 11.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_input_non_empty(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Input cannot be empty. Please try again.")


def display_catalog(catalog):
    if catalog.head is None:
        print("Your catalog is empty. Add a book to get started!")
    else:
        print("------------- Book Catalog -------------")
        print(catalog)


def main_menu():
    """
       Create a menu system and repeat until the user decides to exit
    """
    catalog = BookCatalog()
    cart = CheckoutCart()

    while True:
        print("\n Welcome to MJ Bookstore")
        print("======= Catalog Menu =======")
        print("1. Add a new Book to Catalog")
        print("2. Show All Books")
        print("3. Find Books by Author")
        print("4. Find Books by Title")
        print("5. Look up Book by ISBN")
        print("6. Remove Book by ISBN")
        print("7. Add Book to Checkout Cart")
        print("8. Remove Book from Cart")
        print("9. Peek Cart(Last Added Book)")
        print("10. Display Cart Size")
        print("11. Exit the Program")
        print("============================")

        user_choice = get_validated_menu_input()

        if user_choice == 1:
            isbn = get_input_non_empty("Please enter ISBN: ")
            title = get_input_non_empty("Please enter Title: ")
            author = get_input_non_empty("Please enter Author: ")
            if catalog.add_book(BookNode(isbn,title,author)):
                print(f"Book '{title}' by {author} added successfully.")
            else:
                print(f"Error: ISBN '{isbn}' already exists.")

        elif user_choice == 2:
            display_catalog(catalog)

        elif user_choice == 3:
            author = get_input_non_empty("Please enter Author: ")
            results = catalog.get_books_by_author(author)
            if results: # Check if the results is not None and not empty
                print(f"Books by {author}: ")
                for book in results:
                    print(book)
            else:
                print("No books were found for that author.")

        elif user_choice == 4:
            title = get_input_non_empty("Please enter Title: ")
            results = catalog.get_books_by_title(title)
            if results: # Check if the results is not None and not empty
                print(f"Books titled '{title}': ")
                for book in results:
                    print(book)
            else:
                print("No books were found with that title.")

        elif user_choice == 5:
            isbn = get_input_non_empty("Please enter ISBN: ")
            book = catalog.get_books_by_isbn(isbn)
            if book:
                print(f"Book found: {book}")
            else:
                print("No book was found with that ISBN.")

        elif user_choice == 6:
            isbn = get_input_non_empty("Please enter ISBN: ")
            removed = catalog.remove_book_by_isbn(isbn)
            if removed:
                print(f"Book removed → ISBN: {removed.isbn}, Title: {removed.title}, Author: {removed.author}")
            else:
                print("No book was found with that ISBN to remove.")

        elif user_choice == 7:
            title = get_input_non_empty("Please enter book title: ")
            cart.add_to_cart(title)
            print(f"Book '{title}' added to cart.")

        elif user_choice == 8:
            removed = cart.remove_from_cart()
            if removed:
                print(f"Removed '{removed}' from cart")
            else:
                print("Cart is empty. There are no books to remove.")

        elif user_choice == 9:
            last_book = cart.peek_cart()
            if last_book:
                print(f"Top of cart: '{last_book}'")
            else:
                print("Cart is empty. There are no books to show.")

        elif user_choice == 10:
            cart_size = cart.cart_size()
            print(f"Cart contains {cart_size} book(s).")

        elif user_choice == 11:
            print("Exiting Bookstore System. Goodbye!")
            break


main_menu()

