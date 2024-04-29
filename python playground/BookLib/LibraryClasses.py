import json
import LibraryFunctions

class BOOK:
	def __init__(self, title, genres, author):  # Assuming genres can be a list of genres
		self.title = title
		self.genres = genres  # Changed to list handling
		self.author = author

	def __str__(self):
		return f"{self.title}, genres = '{', '.join(self.genres)}', author = '{self.author}"

	def to_dict(self):
		return {'title': self.title, 'genres': self.genres, 'author': self.author}


class LIBRARIAN:
	def __init__(self, db_path='BookDatabase.json'):
		self.books = []
		self.db_path = db_path
		self.load_books()

	def add_book(self, title, genres, author):
		if not any(book.title == title and book.author == author for book in self.books):
			new_book = BOOK(title, genres, author)
			self.books.append(new_book)
			self.save_books()  # Save the updated books list to file
			print(title + "  added successfully!")
		else:
			print("This book is already in your library.")

	def save_books(self):
		with open(self.db_path, 'w') as f:
			json.dump([book.to_dict() for book in self.books], f, indent=4)

	def load_books(self):
		try:
			with open(self.db_path, 'r') as f:
				books_data = json.load(f)
				self.books = [BOOK(**book) for book in books_data]
		except FileNotFoundError:
			self.books = []

	def find_books_by_genre(self, genre): # TODO I will need to review this function
		# Find and print books by specific genre
		found_books = [book for book in self.books if genre in book.genres]
		for book in found_books:
			print(book)

	def find_books_by_title(self, title):
		# Find and print books by specific title
		found_books = [book for book in self.books if title in book.genres]
		for book in found_books:
			print(book)