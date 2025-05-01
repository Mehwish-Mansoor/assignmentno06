# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added

class Book:
    # Class variable to keep track of the total number of books
    total_books = 0

    def __init__(self, title):
        self.title = title
        # Increment the book count when a new book is added
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        # Class method to increment the total_books count
        cls.total_books += 1

# Example usage
if __name__ == "__main__":
    book1 = Book("Python Crash Course by Eric Matthes") 
    book2 = Book("Automate the Boring Stuff with Python by AI Sweigart")
    book3 = Book("Learning Python by Mark Lutz")

    print(f"Total books: {Book.total_books}")  # Output: Total books: 3