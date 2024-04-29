# We are going to need to reference the classes and submit to the list
import LibraryClasses


# Here we are going to start the interaction by asking what is required by the user
def lib_ui():
	welcome_msg = input("Welcome to the Library, press 1 to add a book and 2 search for a book")
	if welcome_msg == "1":
		return add_new_book()
	if welcome_msg == "2":
		return book_search()
	else:
		attempt_msg = input("I didn't get that. To exit the Library, press q, or any other key to start again")
		if attempt_msg.lower() == "q":
			exit()
		else:
			lib_ui()


# Submission of a book record
def add_new_book():
	title = input("Please enter the book title: ")
	genres = input("Please enter book genres (comma-separated): ").split(',')
	author = input("Please enter the book's author: ")

	new_book = LibraryClasses.BOOK(title, genres, author)
	confirmation = input(f"You entered: {new_book}. Add to library? (y/n): ")

	if confirmation.lower() == 'y':
		LibraryClasses.LIBRARIAN.add_book(title=title, genres=genres, author=author)
	else:
		print("Book addition cancelled.")


def book_search():
	search_term = input(
		"For genre, press 1. To search titles, press 2. For author search, press 3. For all books, press 'A'")
	if search_term.lower() == "1":
		return genre_search()
	if search_term.lower() == "2":
		return title_search()
	if search_term.lower() == "3":
		return author_search()
	if search_term.upper() == "A":
		return LibraryClasses.LIBRARIAN.load_books()
	else:
		try_again_msg = input("I didn't get that. To exit the Library, press q, or any other key to start again")
		if try_again_msg.lower() == "q":
			exit()
		else:
			book_search()


def genre_search():
	genre_input = input("Please enter a genre: ")
	return LibraryClasses.LIBRARIAN.find_books_by_genre(genre_input)


def title_search():
	title_input = input("Please enter a title: ")
	return LibraryClasses.LIBRARIAN.find_books_by_title(title_input)


def author_search():

	pass
