import LibraryClasses
import BkList


def lib_ui():
	welcome_msg = input("Welcome to the Library, press 1 to add a book and 2 search for a book")
	if welcome_msg == "1":
		return book_title()
	if welcome_msg == "2":
		return
	else:
		second_attempt()


def second_attempt():
	attempt_msg = input("Would you like to exit the Library, press q to quit and any other key to continue")
	if attempt_msg.lower() == "q":
		exit()
	else:
		lib_ui()


def book_title():
	title = LibraryClasses.BOOK.title = input("Please enter a book title")
	# confirm the book title and then move to genre
	return title_check(title)


def title_check(title):
	check_title = input("You entered: " + title + ". Would you like to proceed? y for yes, n for no")
	if check_title.lower() == "y":
		return book_genre()
	else:
		print("Press 1 to start again and press q to quit")
		if check_title.lower() == "q":
			exit()
		else:
			book_title()


def book_genre():
	genres = LibraryClasses.BOOK.genres = input("Please enter the book's genre")
	return add_genre

def add_genre(genres):
