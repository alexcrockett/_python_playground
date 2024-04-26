"""
This program will store a user's reading list and make reading suggestions from it based on genres they supply with the
book titles.
"""


# The book class
class BOOK:
	def __init__(self, title, genre, author):
		self.title = title
		self.genre = genre
		self.author = author

	def __str__(self):
		return f"{self.title}', genre = '{self.genre}', author = '{self.author}"


class Library:
	def __init__(self):
		self.books = []  # This will store instances of BOOK

	def add_book(self, title, genre, author):
		# Create a new BOOK instance and append it to the list
		new_book = BOOK(title, genre, author)
		self.books.append(new_book)

	def list_books(self):
		# Print all books in the library
		for book in self.books:
			print(book)

	def find_books_by_genre(self, genre):
		# Find and print books by specific genre
		found_books = [book for book in self.books if genre in book.genre]
		for book in found_books:
			print(book)
