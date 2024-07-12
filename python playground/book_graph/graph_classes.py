# This file contains classes for the books knowledge graph
# If one query yields more than one result an edge should be created between them
# The LLM should determine the labels for these ad-hoc edges

import _sources

class IMPORTER:
	# import the dataframe
	# Parse relevant fields (genres=tags, title, author, etc.)
	# Assign objects to the correct class
	def __init__(self):
	def call_dataframe(self, _sources):
		from _sources import books_csv_data
			return book_values(books_csv_data)

	def book_values(books_csv_data):
		pass

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

