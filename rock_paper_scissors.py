import random
import sys


def play():
    # Initialize the variable 'choice' to '1' to enter the loop for the first time
    choice = '1'
    
    # Define the set of allowed user inputs (Rock -> 'r', Paper -> 'p', Scissor -> 's')
    allowed_inputs = {'r', 'p', 's'}
    
    # Start a loop to allow the user to play multiple rounds until they choose to stop
    while choice == '1':
        # Get the user's choice (Rock, Paper, or Scissor) and convert it to lowercase
        user = input("Enter your choice (Rock -> r, Paper -> p, Scissor -> s): ").lower()
        
        # Check if the user's input is valid (in the allowed_inputs set)
        if user not in allowed_inputs:
            print("Invalid input! You will automatically exit from this game!")
            sys.exit()
        
        # Generate a random choice for the computer (Rock, Paper, or Scissor)
        computer = random.choice(['r', 'p', 's'])

        # Compare the user's choice with the computer's choice to determine the result
        if user == computer:
            print(f"You and computer both chose {user}. So this is a tie!")
        elif is_win(user, computer):
            print(f"You played {user} and computer played {computer}. So You won! 🎉")
        else:
            print(f"You played {user} and computer played {computer}. So You lost! Better luck next time")

        # Ask the user if they want to continue playing (Enter '1' to continue, any other key to stop)
        choice = input("Do you want to continue playing? (Yes -> 1, No -> any other key): ")


def is_win(user, computer):
    # Check if the user's choice beats the computer's choice
    return (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p')

# Start the game by calling the play() function
play()
