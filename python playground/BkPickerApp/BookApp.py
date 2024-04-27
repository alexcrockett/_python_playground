# We are going to need to reference the classes and submit to the list
import LibraryClasses
import BkList


# Here we are going to start the interactiion by asking what is required by the user
def lib_ui():
	welcome_msg = input("Welcome to the Library, press 1 to add a book and 2 search for a book")
	if welcome_msg == "1":
		return book_title()
	if welcome_msg == "2":
		return book_search()
	else:
		second_attempt()


# Here we will check to see if a mistake was made, or confirm continuing
def second_attempt():
	attempt_msg = input("Would you like to exit the Library, press q to quit and any other key to start again")
	if attempt_msg.lower() == "q":
		exit()
	else:
		lib_ui()


# The user starts the book submission process and adds a book title
def book_title():
	title = LibraryClasses.BOOK.title = input("Please enter a book title")
	# confirm the book title and then move to genre
	return title_check(title)


# We will check for typos
def title_check(title):
	check_title = input("You entered: " + title + ". Would you like to proceed? y for yes, n for no")
	if check_title.lower() == "y":
		return add_book_genre()
	else:
		print("Press 1 to start again and press q to quit")
		if check_title.lower() == "q":
			exit()
		else:
			book_title()


# We will now allow the user to add a genre to the book
def add_book_genre(new_genres):
	new_genres = LibraryClasses.BOOK.genres = input("Please enter the book's genre")
	return add_new_genre(new_genres)


# We will confirm the genre and check to see if an additional genre is needed
def add_new_genre(new_genres):
	print(new_genres)
	more_genres = input("Would you like to add an additional genre? y for yes, n for no")
	if more_genres.lower() == "y":
		return input("Enter the genre")  # TODO Need this to go somewhere
	if more_genres.lower() == "n":
		return book_author()


def book_author():
	pass


# TODO Complete author adding
# TODO View record being creted
# TODO Make edits
# TODO add to the library
# TODO Check for duplicates
# TODO Am I using the Class BOOK and LIBRARY correctly


def book_search():
	pass
# TODO Search/filter by title
# TODO Search/filter by Author
# TODO Search/filter by Genre
# TODO Search by regular expression
