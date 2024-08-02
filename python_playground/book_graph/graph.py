# The purpose of this file is to manage schema for the graph
import pandas as pd
import csv_import
from neomodel import (StructuredNode, StringProperty, RelationshipFrom, IntegerProperty, RelationshipTo)


class CSVHandler:
	def __init__(self):
		# Assuming CSV class has a method or property to get the DataFrame
		self.csv_instance = csv_import.CSV()
		self.data_for_graph = self.csv_instance.get_data()  # Method to get data

	def content_parser(self):
		# Initialize lists to collect data
		titles = []
		authors = []
		additional_authors = []
		publication_years = []
		topics = []
		genres = []
		summaries = []
		publisher = []
		isbn = []
		isbn13 = []

		# Assuming self.data_for_graph is a DataFrame
		for index, row in self.data_for_graph.iterrows():
			titles.append(row['Title'])
			authors.append(row['Author'])
			additional_authors.append(row['Additional Authors'])
			publication_years.append(row['Publication Year'])
			topics.append(row['Topics'])
			genres.append(row['Genres'])
			summaries.append(row['Summary'])
			publisher.append(row['Publisher'])
			isbn.append(row['ISBN'])
			isbn13.append(row['ISBN13'])

		# Create a dictionary to return
		data = {
			'Title': titles,
			'Author': authors,
			'Additional Authors': additional_authors,
			'Publication Year': publication_years,
			'Topics': topics,
			'Genres': genres,
			'Summary': summaries,
			'Publisher': publisher,
			'ISBN': isbn,
			'ISBN13': isbn13
		}
		return data


class Author(StructuredNode):
	name = StringProperty(unique_index=True, required=True)
	books = RelationshipTo('Book', 'AUTHORED')
	focus = RelationshipTo('Genres', 'INTERESTED_IN')
	interests = RelationshipTo('Topics', 'INTERESTED_IN')
	writer_of = RelationshipFrom('Genres', 'EXAMPLE_OF')


class Book(StructuredNode):
	title = StringProperty(unique_index=True, required=True)
	isbn = StringProperty(unique_index=True)
	isbn13 = StringProperty(unique_index=True)
	publication_year = IntegerProperty()
	summary = StringProperty()
	topics = RelationshipTo('Topics', 'EXAMPLE_OF')
	genres = RelationshipFrom('Genre', 'EXAMPLE_OF')
	authors = RelationshipFrom(Author, 'AUTHORED')
	additional_authors = RelationshipFrom(Author, 'AUTHORED')  # TODO create additional authors
	publisher = RelationshipTo('Publisher', 'PUBLISHED')


class Publisher(StructuredNode):
	name = StringProperty(unique_index=True)
	books = RelationshipFrom(Book, 'PUBLISHED')


class Genre(StructuredNode):
	name = StringProperty(unique_index=True)
	books = RelationshipTo(Book, 'EXAMPLE_OF')
	authors = RelationshipFrom(Author, 'INTERESTED_IN')
	writers = RelationshipTo(Author, 'EXAMPLE_OF')
	additional_authors = RelationshipTo(Author, 'CONTRIBUTED_BY')
	topics = RelationshipTo('Topics', 'EXAMPLE_OF')


class Topics(StructuredNode):
	name = StringProperty(unique_index=True)
	books = RelationshipTo(Book, 'CONTAINS_TOPIC')
	examples = RelationshipTo(Book, 'EXAMPLE_OF')
	authors = RelationshipFrom(Author, 'INTERESTED_IN')
	genres = RelationshipFrom(Genre, 'EXAMPLE_OF')
