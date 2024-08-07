import pandas as pd
from pkgutil import get_data

# Initialize data collection for csv data
class GAIDATA:
	def __init__(self):
		self.csv_source_path = 'databases/raw_library.csv'
		self.df_csv = pd.read_csv(self.csv_source_path)

# Initial dataframe to parse out unwanted columns
	def initial_csv_dataframe(self):
		csv_data = self.df_csv[[
			'Title',
			'type',
			'Author',
			'Additional Authors',
			'ISBN',
			'ISBN13',
			'Publisher',
			'Original Publication Year',
			'Summary',
			'Topics',
			'Genres',
		]].copy()
		return csv_data


# Build dictionary to abstract from initial dataframe
# We want to do this to add data sources later on
class DICTIONARY:
	def __init__(self, csv_data):
		self.csv_data_for_graph = csv_data

	def dataframe_to_dict(self):
		dict_content = {
			"titles": self.csv_data_for_graph['Title'],
			"authors": self.csv_data_for_graph['Author'],
			"additional_authors": self.csv_data_for_graph['Additional Authors'],
			"summaries": self.csv_data_for_graph['Summary'],
			"genres": self.csv_data_for_graph['Genres'],
			"topics": self.csv_data_for_graph['Topics'],
			"publisher": self.csv_data_for_graph['Publisher'],
			"publication_years": self.csv_data_for_graph['Original Publication Year'],
			"isbn": self.csv_data_for_graph["ISBN"],
			"isbn13": self.csv_data_for_graph["ISBN13"]
		}
		return dict_content


# Collect data in dataframe that will be used to populate nodes
class CONTAINER:
	def __init__(self, dict_content):
		self.book_dataf = pd.DataFrame(dict_content)

	def resource_dataframe(self):
		return self.book_dataf

