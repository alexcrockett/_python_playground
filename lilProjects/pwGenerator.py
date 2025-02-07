
# Define all the necessary elements to pull from
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
		   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
		   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
		   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
pw_list = []

# Start the generator
print("Let's create a strong password")
nr_letters = int(input("How many letters?\n"))
nr_symbols = int(input(f"How many symbols?\n"))
nr_numbers = int(input(f"How many numbers?\n"))

# import the necessary library
import random

# Select random elements
for i in letters:
	r_letters = random.sample(letters, nr_letters)
for i in numbers:
	r_numbers = random.sample(numbers, nr_numbers)
for j in symbols:
	r_symbols = random.sample(symbols, nr_symbols)

# Create a new master list and randomize it
for i in r_letters:
	pw_list.append(i)
for i in r_numbers:
	pw_list.append(i)
for i in r_symbols:
	pw_list.append(i)

random.shuffle(pw_list)

# Extract all the elements from the list and format as a pw
password = "".join(pw_list)

# Print the password
print(f"Your password is: {password}")
