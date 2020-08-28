# Incorporate the random library
import random

# Specify the three options
OPTIONS = ["r", "p", "s"]

def is_valid(user_choice):
    return user_choice in OPTIONS

def show_winner(user_choice, computer_choice):
    if computer_choice == user_choice:
        print("Tie")
    elif (computer_choice == "r" and user_choice == 's') or (computer_choice == "s" and user_choice == 'p') or (computer_choice == "p" and user_choice == 'r'):
        print("You Lose!")
    else:
        print("You Win!")

        
def get_input():
    user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")
    
    if not is_valid(user_choice):
        raise Exception("Invalid: enter r, p, or s!")
    
    return user_choice


def main():
    print("Let's Play Rock Paper Scissors!")

    user_choice = get_input()
    computer_choice = random.choice(OPTIONS)
     
    print(f"You chose {user_choice} and the computer chose {computer_choice}")

    show_winner(user_choice, computer_choice)

    
main()