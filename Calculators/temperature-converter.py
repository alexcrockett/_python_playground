# Ask temperature
def what_temperature():
	your_temperature = input("What temperature do you have, please enter a number: ")
	if your_temperature.isnumeric():  # Checking to see a numeric value is given
		return t_input(your_temperature)  # passes the value onto the next function
	else:
		print("Invalid input. Please enter a numeric value.")  # Indicate there is an error
		return what_temperature()  # Start again


# Here we want to find out what output scale the user wants
def t_input(your_temperature):
	while True:  # The while loop is used for error validation
		ask_units = input("What measurement do you want? Press 1 for Celsius, 2 for Fahrenheit: ")
		if ask_units == '1':
			return fahrenheit_to_celsius(your_temperature)  # We pass the user to the correct function with the argument
		elif ask_units == '2':
			return celsius_to_fahrenheit(your_temperature)  # We pass the user to the correct function with the argument
		else:
			print("Invalid input. Please enter 1 for Celsius or 2 for Fahrenheit.")  # We try again


# Here we will ask Fahrenheit and convert to Celsius
def fahrenheit_to_celsius(your_temperature):
	f_value_i = float(your_temperature)  # f_value_i is the initial value
	c_value_f = (f_value_i - 32) * 5 / 9  # °C = (°F − 32) x 5/9
	print(c_value_f)  # We print the result


# Here we will ask Celsius and convert to Fahrenheit
def celsius_to_fahrenheit(your_temperature):
	c_value_i = float(your_temperature)  # c_value_i is the initial value
	f_value_c = (c_value_i * 9 / 5) + 32  # °F = (°C × 9/5) + 32
	print(f_value_c)  # We print the result


def main():
	while True:
		what_temperature()  # Ask for temperature and validate, then proceed to conversion

		# Ask the user if they want to perform another conversion
		user_choice = input("Do you want to perform another conversion? (yes/no): ")
		if user_choice.lower() != 'yes':
			print("Exiting program. Goodbye!")
			break  # Exit the loop, thus ending the program


if __name__ == "__main__":
	main()
