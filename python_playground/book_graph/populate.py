import pandas as pd
from neomodel import (config, install_all_labels)
import graph
import import_data

config.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'
config.DATABASE_NAME = 'gai'


def setup_database():
	# Setup initial data import and processing
	gai_data = import_data.GAIDATA()
	csv_data = gai_data.initial_csv_dataframe()
	dict_instance = import_data.DICTIONARY(csv_data)
	dict_content = dict_instance.dataframe_to_dict()
	container = import_data.CONTAINER(dict_content)
	data_to_import = container.resource_dataframe()
	process_books(data_to_import)
	install_all_labels()

	# Initialize and use handler
	handler = graph.HANDLER()
	handler.pass_to_book(data_to_import)
	handler.pass_to_author(data_to_import)
	handler.pass_to_publisher(data_to_import)


def process_books(data_to_import):
	for index, row in data_to_import.iterrows():
		try:
			book = graph.Book(
				title=row['title'],
				isbn=row['isbn'],
				isbn13=row['isbn13'],
				publication_year=row['publication_year'],
				# summary=row['summary']
			).save()
			if pd.notna(row['author']):
				author = graph.Author(name=row['author']).save()
				book.authors.connect(author)  # Connect book to author
			if pd.notna(row['publisher']):
				publisher = graph.Publisher(name=row['publisher']).save()
				publisher.books.connect(book)  # Connect publisher to book
			print(f"Book created: {book.title} with related nodes.")
		except Exception as e:
			print(f"Failed to create nodes or relationships for row {index}: {e}")


if __name__ == "__main__":
	setup_database()
