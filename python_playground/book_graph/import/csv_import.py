class CSVIMPORTER:
	def __init__(self):
		self.source_path = '../databases/raw_library.csv'

	def read_csv(self):
		import pandas as pd
		df = pd.read_csv(self.source_path)


class CSVFRAME(CSVIMPORTER):
	def data_frame(self, df):
		new_frame = df[[
			'Title',
			'type',
			'Author',
			'Additional Authors',
			'ISBN',
			'ISBN13',
			'Publisher',
			'Number of Pages',
			'Original Publication Year',
			'Summary',
			'Tags',
			'Genres',
			'Text',
			'Linked Data'
		]].copy()
		return new_frame
