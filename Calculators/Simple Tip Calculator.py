
# Collect data
def start():
	print("Let's calculate the tip you want to give")
	bill = float(input("How much was the meal?"))
	return tip_value(bill)

# Collected the tip amount
def tip_value(bill):
	tip_amount = input("How much would you like to give tip? a = 10%, b = 15%, c = 20%")
	if tip_amount.lower() == 'a':
		selected_tip = ((bill * 0.1) + bill)
		return div_by_person(selected_tip)
	elif tip_amount.lower() == 'b':
		selected_tip = ((bill * 0.15) + bill)
		return div_by_person(selected_tip)
	elif tip_amount.lower() == 'c':
		selected_tip = ((bill * 0.2) + bill)
		return div_by_person(selected_tip)
	else:
		print("Invalid input. Please try again.")
		return tip_amount

def div_by_person(selected_tip):
	no_peeps = input("How many people do you want to split with?")
	result = round(selected_tip / float(no_peeps), 2)
	return result

def main():
	while True:
		result = start()
		print(f"You should pay {result} each")

		# Ask the user if they want to perform another calculation
		user_choice = input("Do you want to perform another calculation? (yes/no): ")
		if user_choice.lower() != 'yes':
			print("Exiting program. Goodbye!")
			break  # Exit the loop, ending the program


if __name__ == "__main__":
	main()