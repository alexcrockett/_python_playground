"""
This program will store a user's reading list and make reading suggestions from it based on genres they supply with the
book titles.
"""


# The book class
class BOOK:
	def __init__(self, title, genre, author):
		self.title = title
		self.genre = genre
		self.author = author

	def __str__(self):
		return f"{self.title}', genre = '{self.genre}"
