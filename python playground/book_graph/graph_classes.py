# This file contains classes for the books knowledge graph
# If one query yields more than one result an edge should be created between them
# The LLM should determine the labels for these ad-hoc edges

class IMPORTER:
	def __init__(self):
		self.source_path = 'databases/raw_library.csv'

	def call_dataframe(self):
		import pandas as pd
		books_csv_data = pd.read_csv(self.source_path)
		return self.book_values(books_csv_data)

	def book_values(self, books_csv_data):
		books = []
		for index, row in books_csv_data.iterrows():
			book = self.parse_values(row)
			if book:
				books.append(book)
		return books

	def parse_values(self, row):
		if row['type'] == "book":
			return BOOK(title=row['title'], author=row['author'], genres=row['genres'].split(','))
		return None

	def import_from_api(self):
	pass

	def import_from_browser(self):
	pass

	def import_from_web(self):
	pass

class MANAGER:
	# This class assigns imported content via classes (books and bookmarks) to nodes
	def __init__(self):

class BOOK:
	# This is a class for books imported to the application from dataframe or API
	def __init__(self):

class BOOKMARK:
	# This class is the same as the book class, but for browser bookmarks
	def __init__(self):

class GRAPH:
	# This is the class of the graph, managing both nodes and edges
	def __init__(self):

class NODE:
	# The class for individual nodes in the graph
	def __init__(self):

class EDGE:
	# The class for edges in the graph
	def __init__(self):

class DATABASE:
	# This graph brings together all stored information and provides a point for queries to be directed
	def __init__(self):

class QUERIES:
	# This class manages queries to the system via an LLM (OpenAI API)
	def __init__(self):

