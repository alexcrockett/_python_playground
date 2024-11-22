import random
rock = '''
                       888      
                       888      
                       888      
888d888 .d88b.  .d8888b888  888 
888P"  d88""88bd88P"   888 .88P 
888    888  888888     888888K  
888    Y88..88PY88b.   888 "88b 
888     "Y88P"  "Y8888P888  888 
'''

paper = '''
88888b.  8888b. 88888b.  .d88b. 888d888 
888 "88b    "88b888 "88bd8P  Y8b888P"   
888  888.d888888888  88888888888888     
888 d88P888  888888 d88PY8b.    888     
88888P" "Y88888888888P"  "Y8888 888     
888             888                     
888             888                     
888             888          
'''

scissors = '''
                d8b                                        
                Y8P                                        
                                                           
.d8888b  .d8888b888.d8888b .d8888b  .d88b. 888d888.d8888b  
88K     d88P"   88888K     88K     d88""88b888P"  88K      
"Y8888b.888     888"Y8888b."Y8888b.888  888888    "Y8888b. 
     X88Y88b.   888     X88     X88Y88..88P888         X88 
 88888P' "Y8888P888 88888P' 88888P' "Y88P" 888     88888P' 
'''

# Make a choice
prompt = input("Make a selection: rock, paper, or scissors \n")
if prompt == "rock":
	prompt = rock
elif prompt == "paper":
	prompt = paper
else:
	prompt = scissors

# Computer chooses
comp_choices = [rock, paper, scissors]
print(prompt)
comp_selection = random.choice(comp_choices)
print(comp_selection)

# Logic
final_selection = [prompt, comp_selection]
win = [[rock, scissors], [paper, rock], [scissors, paper]]

# Results
if comp_selection == prompt:
	print("Draw")
elif final_selection == win[0] or final_selection == win[1] or final_selection == win[2]:
	print("You won!")
else:
	print("You lost!")
