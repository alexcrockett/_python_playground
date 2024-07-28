# CSV imports are managed here

# This class imports the CSV the uses Pandas dataframe to read it
class CSVIMPORTER:
	def __init__(self):
		self.source_path = '../databases/raw_library.csv'
		self.df = None

	def read_csv(self):
		import pandas as pd
		self.df = pd.read_csv(self.source_path)


# This class checks the CSV is not empty and then creates a data-frame
class CSVFRAME(CSVIMPORTER):
	def data_frame(self):
		if self.df is not None:
			# List columns to select
			columns_to_select = [
				'Title', 'type', 'Author', 'Additional Authors', 'ISBN',
				'ISBN13', 'Publisher', 'Number of Pages', 'Original Publication Year',
				'Summary', 'Tags', 'Genres', 'Text', 'Linked Data'
			]
			# Use the list to select columns directly
			new_frame = self.df[columns_to_select].copy()
			return new_frame
		else:
			print("Data not loaded. Check CSV and try again.")
			return None
