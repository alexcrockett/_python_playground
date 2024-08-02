# CSV imports are managed here

import pandas as pd


# This class imports the CSV the uses Pandas dataframe to read it
# It then removes unwanted columns and creates a new frame with the desired columns
class CSV:
	def __init__(self):
		self.source_path = 'databases/raw_library.csv'
		self.df = pd.read_csv(self.source_path)

	def selected_data(self):
		data = self.df
		new_frame = data[[
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
		return new_frame.selected_data()

# TODO Need to make code more robust, e.g. error handling and other scenarios for the import.
# TODO Need to consider data integrity issues (missing values, empty rows etc.
