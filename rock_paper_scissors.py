import random
import sys


def play():
    user = input("Enter your choice \n\
(Rock -> r, Paper -> p, Scissor -> s): \n").lower()

    if (user != 'r') and (user != 'p') and (user != 's'):
        print("Invalid input. You will automatically exit from this game!")
        sys.exit()
    
    
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print(f"You and computer both chose {user}. So this is a tie!")
    
    if is_win(user,computer):
        return f"You played {user} and computer played {computer}. So You won! 🎉"

    return f"You played {user} and computer played {computer}. So You lost! Better luck next time"


def is_win(user, computer):
    if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
        return True
    

print(play())