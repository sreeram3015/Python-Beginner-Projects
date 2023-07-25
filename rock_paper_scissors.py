import random
import sys


def play():
    user = input("Enter ypur choice \n\
(Rock -> r, Paper -> p, Scissor -> s): \n").lower

    if user != 'r' or user != 'p' or user != 's':
        print("Invalid input. You will automatically exit from this game!")
        sys.exit()
    
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print(f"You and computer both chose {user}. So this is a tie!")
    
