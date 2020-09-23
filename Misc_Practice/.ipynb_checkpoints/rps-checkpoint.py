# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Print both selections
print(f"You chose {user_choice} and the computer chose {computer_choice}")

# Run Conditionals
if computer_choice == user_choice:
    print("Tie")
elif (computer_choice == "r" or user_choice == "r") and (computer_choice == "s" or user_choice == "s"):
    print( "Rock Wins!")
elif (computer_choice == "p" or user_choice == "p") and (computer_choice == "r" or user_choice == "r"):
    print( "Paper Wins!")
elif (computer_choice == "s" or user_choice == "s") and (computer_choice == "p" or user_choice == "p"):
    print( "Scissors Wins!")
else: 
    print("IDK!")


