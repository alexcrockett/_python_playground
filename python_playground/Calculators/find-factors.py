"""
A program that finds the factors of a number.
Credit is due to Amit Saha author of 'Doing Math With Python', No Starch Press, whose book I am studying from.
I have taken the liberty of taking the idea of the code in his book and re-writing it in a slightly different way.
I've done this more for my own learning than for the efficiency of the code.
"""


def find_factors_input():
	users_query = input("Enter a whole number: ")
	if users_query.isnumeric():
		users_number = int(users_query)
		find_factors(users_number)  # Call find_factors directly with the user's number
	else:
		print("Invalid input, try again.")

def find_factors(users_number):
	print(f"Factors of {users_number}:")
	for i in range(1, users_number + 1):
		if users_number % i == 0:
			print(i)  # Just print the factor

def main():
	while True:
		find_factors_input()  # Get user input and find factors

		user_choice = input("Do you want to perform another calculation? (yes/no): ")
		if user_choice.lower() != 'yes':
			print("Exiting program. Goodbye!")
			break  # Exit the loop, thus ending the program

if __name__ == "__main__":
	main()
