class CSVIMPORTER:
	def __init__(self):
		self.source_path = '../databases/raw_library.csv'

	def read_csv(self):
		import pandas as pd
		df = pd.read_csv(self.source_path)
		return df

	def id_books(self, df):
		result_list = [row for index, row in df.iterrows() if row['Book Id'] is not None]
		return result_list

	def parse_entry(self, result_list):
		book_ref = []
		for row in result_list:
			if row['Title'] is not None:
				Book_Title = row['Title'] = row['Title'].strip()
				return book_ref.append(Book_Title)
			elif row['Author'] is not None:
				Book_Author = row['Author'] = row['Author'].strip()
				return book_ref.append(Book_Author)


	def define_book():
		pass

	def define_attribute():
		pass

	def missing_attribute():
		pass

	def parse_values(self, row):
		if row['type'] == "book":
			return BOOK(
				title=row['title'],
				author=row['author'],
				authors2=row['authors2'],
				texttype=row['texttype'],
				content=row['content'],
				summary=row['summary'],
				tags=row['tags'],
				genres=row['genres'].split(','),
				category=row['category'],
				ISBN=row['ISBN'],
				ISBN13=row['ISBN13'],
				rating=row['rating'],
				publisher=row['publisher'],
				binding=row['binding'],
				pages=row['pages'],
				date=row['date'],
			)
		return None
