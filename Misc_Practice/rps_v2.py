# Incorporate the random library
import random

OPTIONS = ["r", "p", "s", "q"]

def is_valid(user_choice):
    return user_choice in OPTIONS
    
def show_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie!")  
    elif (
        (user_choice == "r" and computer_choice == "s")
        or (user_choice == "p" and computer_choice == "r")
        or (user_choice == "s" and computer_choice == "p")
    ):
        print("You win!")
    else:
        print("You lose!")
        
def get_input():
    
    message = "Make your Choice: (r)ock, (p)aper, (s)cissors? Press q to quit!"
    user_choice = input(message)
    
    while not is_valid(user_choice):
        user_choice = input(message)

    return user_choice
    
def main():
    
    while True:
        print("Let's Play Rock Paper Scissors!")
    
        user_choice = get_input()
        
        if user_choice == "q":
            break
            
        computer_choice = random.choice(OPTIONS)
        
        print(f"You chose {user_choice}")
        print(f"The computer chose {computer_choice}")
        
        show_winner(user_choice, computer_choice)
        
main()