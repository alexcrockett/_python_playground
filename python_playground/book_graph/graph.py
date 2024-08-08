# The purpose of this file is to manage schema for the graph
import pandas as pd
from docutils.core import Publisher
from neomodel import (RelationshipFrom, RelationshipTo)
from neomodel import (StringProperty, IntegerProperty)
from neomodel import (StructuredNode)

import import_data

gai_data = import_data.GAIDATA()
csv_data = gai_data.initial_csv_dataframe()       # Call the method to get DataFrame
dict_instance = import_data.DICTIONARY(csv_data)  # Initialize with data
dict_content = dict_instance.dataframe_to_dict()  # Convert to dict
container = import_data.CONTAINER(dict_content)   # Pass dictionary content


class HANDLER:
	def __init__(self):
		data_to_import = container.resource_dataframe()
		pd.DataFrame(data_to_import)

	def pass_to_book(self, data_to_import):
		for index, row in data_to_import.iterrows():
			try:
				book = Book(
					title=row['titles'],
					isbn=row['isbn'],
					isbn13=row['isbn13'],
					publication_year=row['publication_years'],
					summary=row['summaries']
				).save()
				print(f"Book created: {book.title}")
			except Exception as e:
				print(f"Failed to create book for row {index}: {e}")

	def pass_to_author(self, data_to_import):
		for index, row in data_to_import.iterrows():
			try:
				author = Author(
					name=row['authors'],
					book=row['titles'],
					topic=row['topics'],
					genre=row['genres'],
					publisher=row['publishers']
				).save()
				print(f"Book created: {index}")
			except Exception as e:
				print(f"Failed to create book for row {index}: {e}")

	def pass_to_publisher(self, data_to_import):
		for index, row in data_to_import.iterrows():
			try:
				publisher = Publisher(name=row['publisher']).save()
				print(f"Book created: {index}")
			except Exception as e:
				print(f"Failed to create book for row {index}: {e}")


class Book(StructuredNode):
	title = StringProperty(unique_index=True, required=True)
	isbn = StringProperty(unique_index=True)
	isbn13 = StringProperty(unique_index=True)
	publication_year = IntegerProperty()
	author = RelationshipFrom('Author', 'AUTHORED')
	additional_authors = RelationshipFrom('Author', 'AUTHORED')  # TODO create additional authors
	publisher = RelationshipTo('Publisher', 'PUBLISHED')


class Author(StructuredNode):
	name = StringProperty(unique_index=True, required=True)
	book = RelationshipTo('Book', 'AUTHORED')
	publisher = RelationshipFrom('Publisher', 'PUBLISHED')


class Publisher(StructuredNode):
	name = StringProperty(unique_index=True)
	book = RelationshipFrom(Book, 'PUBLISHED')
	author = RelationshipTo('Author', 'Published')


class CONNECTIONS:
	def __init__(self, book, author, publisher):
		self.Publisher = publisher
		self.Book = book
		self.Author = author

	def connections(self, book, author, publisher):
		author.book.connect(Book)
		publisher.book.connect(Book)
		book.author.connect(Author)
		book.publisher.connect(Publisher)

