import json


class BOOK:
	def __init__(self, title, genres, author):
		self.title = title
		self.genres = genres
		self.author = author

	def to_dict(self):
		return {
			'title': self.title,
			'genres': self.genres,
			'author': self.author
		}

	def __str__(self):
		return f"{self.title}, genres = '{', '.join(self.genres)}', author = '{self.author}"


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
			print(f"No existing book database found at {self.db_path}, starting with an empty library.")
		except json.JSONDecodeError:
			self.books = []
			print(f"Corrupted or empty JSON in {self.db_path}, starting with an empty library.")

	def find_books_by_genre(self, genre):
		# Find and print books by specific genre
		found_books = [book for book in self.books if genre in book.genres]
		for book in found_books:
			return [book for book in self.books if genre.lower() in book.genres]

	def find_books_by_title(self, title):
		# Find and print books by specific title
		found_books = [book for book in self.books if title in book.genres]
		for book in found_books:
			print(book)

	def find_books_by_author(self, author):
		found_books = [book for book in self.books if author in book.author]
		for book in found_books:
			print(book)
