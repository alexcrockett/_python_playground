# Input values
def value_input():
	no_1 = input("Enter a number: ")
	no_2 = input("Enter another number: ")
	# Directly pass the input values to the UI function
	return simple_calc_ui(no_1, no_2)


# For addition
def f_value_add(no_1, no_2):
	i_no_1 = int(no_1)
	i_no_2 = int(no_2)
	f_value_sum = i_no_1 + i_no_2
	return f_value_sum


# For subtraction
def f_value_subtract(no_1, no_2):
	i_no_1 = int(no_1)
	i_no_2 = int(no_2)
	f_value_sub = i_no_1 - i_no_2
	return f_value_sub


# For multiplication
def f_value_multiply(no_1, no_2):
	i_no_1 = int(no_1)
	i_no_2 = int(no_2)
	f_value_product = i_no_1 * i_no_2
	return f_value_product


# For division
def f_value_divide(no_1, no_2):
	i_no_1 = int(no_1)
	i_no_2 = int(no_2)
	# Check for division by zero
	if i_no_2 == 0:
		return "Error: Cannot divide by zero."
	f_value_div = i_no_1 / i_no_2
	return f_value_div


# Selecting the method and performing the calculation
def simple_calc_ui(no_1, no_2):
	select_method = input("A = add, B = subtract, C = multiply, D = divide, E = restart: ")

	if select_method.lower() == 'a':
		return f_value_add(no_1, no_2)
	elif select_method.lower() == 'b':
		return f_value_subtract(no_1, no_2)
	elif select_method.lower() == 'c':
		return f_value_multiply(no_1, no_2)
	elif select_method.lower() == 'd':
		return f_value_divide(no_1, no_2)
	elif select_method.lower() == 'e':
		# Restart the calculation process
		return value_input()
	else:
		print("Invalid input. Please try again.")
		return simple_calc_ui(no_1, no_2)


def main():
	while True:
		result = value_input()
		print(f"Result: {result}")

		# Ask the user if they want to perform another calculation
		user_choice = input("Do you want to perform another calculation? (yes/no): ")
		if user_choice.lower() != 'yes':
			print("Exiting program. Goodbye!")
			break  # Exit the loop, ending the program


if __name__ == "__main__":
	main()
