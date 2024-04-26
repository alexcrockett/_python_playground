"""
Classes used in the application.
"""


class BOOK:
	def __init__(self, title, genres, author):  # Assuming genres can be a list of genres
		self.title = title
		self.genres = genres  # Changed to list handling
		self.author = author

	def __str__(self):
		return f"{self.title}, genres = '{', '.join(self.genres)}', author = '{self.author}"


class LIBRARY:
	def __init__(self):
		self.books = []  # This will store instances of BOOK

	def add_book(self, title, genres, author):
		# Check for duplicates
		if not any(book.title == title and book.author == author for book in self.books):
			new_book = BOOK(title, genres, author)
			self.books.append(new_book)
		else:
			print("This book is already in your library.")

	def list_books(self):
		# Print all books in the library
		for book in self.books:
			print(book)

	def find_books_by_genre(self, genre):
		# Find and print books by specific genre
		found_books = [book for book in self.books if genre in book.genres]
		for book in found_books:
			print(book)
