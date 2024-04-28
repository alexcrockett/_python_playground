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
		print(title + "  added successfully!")
	else:
		print("Book addition cancelled.")


def book_search():
	pass
