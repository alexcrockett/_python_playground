# The purpose of this file is to manage schema for the graph
import csv_import
import pandas as pd
from neomodel import (StructuredNode, StringProperty, RelationshipFrom, IntegerProperty, RelationshipTo, StructuredRel, DateTimeProperty)


class Author(StructuredNode):
	name = StringProperty(unique_index=True, required=True)
	books = RelationshipTo('Book', 'AUTHORED')
	specialization = RelationshipTo('Genres', 'INTERESTED_IN')
	interests = RelationshipTo('Topics', 'INTERESTED_IN')


class Book(StructuredNode):
	title = StringProperty(unique_index=True, required=True)
	isbn = StringProperty(unique_index=True)
	publication_year = IntegerProperty()
	summary = StringProperty()
	topics = StringProperty()  # TODO Update to relationship
	genres = StringProperty()  # TODO Update to relationship
	authors = RelationshipTo(Author, 'AUTHORED_BY')
	additional_authors = RelationshipTo(Author, 'CONTRIBUTED_BY')
	publisher = RelationshipTo('Publisher', 'PUBLISHED')


class Publisher(StructuredNode):
	name = StringProperty(unique_index=True)
	books = RelationshipTo(Book, 'PUBLISHED')


class Genre(StructuredNode):
	name = StringProperty(unique_index=True)
	books = RelationshipTo(Book, 'IS_OF_GENRE')
	authors = RelationshipTo(Author, 'INTERESTED_IN')  # TODO Make sure these relations make sense
	additional_authors = RelationshipTo(Author, 'CONTRIBUTED_BY')  # TODO Make sure these relations make sense
	topics = RelationshipTo('Topics', 'EXAMPLE_OF')  # TODO Make sure these relations make sense


class Topics(StructuredNode):
	name = StringProperty(unique_index=True)
	books = RelationshipFrom(Book, 'CONTAINS_TOPIC')  # TODO Make sure these relations make sense
	authors = RelationshipFrom(Author, 'INTERESTED_IN')  # TODO Make sure these relations make sense
	genres = RelationshipFrom(Genre, 'CONTAINS_TOPIC')  # TODO Make sure these relations make sense
