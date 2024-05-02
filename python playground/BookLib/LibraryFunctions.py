import LibraryClasses
from LibraryClasses import LIBRARIAN

librarian = LIBRARIAN()


def main():
	LIBRARIAN()
	lib_ui()
	check_complete()


def check_complete():
	user_iteration = input(
		"Is there anything else I can help with? Press any key to start again or 'q' to exit the library:  ")
	if user_iteration.lower() != 'q':
		return lib_ui()
	else:
		exit()


# Here we are going to start the interaction by asking what is required by the user
def lib_ui():
	welcome_msg = input("Welcome to the Library, press 1 to add a book and 2 search for a book:  ")
	if welcome_msg == "1":
		return add_new_book()
	if welcome_msg == "2":
		return book_search()
	else:
		attempt_msg = input("I didn't get that. To exit the Library, press q, or any other key to start again:  ")
		if attempt_msg.lower() == "q":
			exit()
		else:
			lib_ui()


# Submission of a book record
def add_new_book():
	while True:
		title = input("Please enter the book title:  ")
		genres = input("Please enter book genres (comma-separated): ").split(',')
		author = input("Please enter the book's author:  ")

		confirmation = input(f"Add {title} by {author} to the library? (y/n): ")
		if confirmation.lower() == 'y':
			librarian.add_book(title=title, genres=genres, author=author)
		else:
			print("Book addition cancelled.")
		return check_complete()


def book_search():
	search_term = input(
		"For genre, press 1. To search titles, press 2. For author search, press 3:  ")
	if search_term.lower() == "1":
		return genre_search()
	elif search_term.lower() == "2":
		return title_search()
	elif search_term.lower() == "3":
		return author_search()
	else:
		try_again_msg = input("I didn't get that. To exit the Library, press q, or any other key to start again:  ")
		if try_again_msg.lower() == "q":
			exit()
		else:
			book_search()


def genre_search():
	genre_input = input("Please enter a genre: ")
	genre_results(genre_input)


def genre_results(genre_input):
	found_books = librarian.find_books_by_genre(genre_input)
	if found_books:
		for book in found_books:
			print(book)
	else:
		print("No books found in the genre:", genre_input)


def title_search():
	title_input = input("Please enter a title:  ")
	title_results(title_input)


def title_results(title_input):
	found_books = librarian.find_books_by_genre(title_input)
	if found_books:
		for book in found_books:
			print(book)
	else:
		print("No books found with the title:", title_input)


def author_search():
	author_input = input("Please enter an author:  ")
	author_results(author_input)


def author_results(author_input):
	found_books = librarian.find_books_by_genre(author_input)
	if found_books:
		for book in found_books:
			print(book)
	else:
		print("No books found with the title:", author_input)


if __name__ == "__main__":
	main()
