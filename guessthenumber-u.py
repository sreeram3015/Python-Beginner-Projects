import random
import sys

# Get the lower and upper limits for the random number range from the user
lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

# Inform the user to think of a number within the given range
print(f"Think of a number between {lower} and {upper}, and I'll try to guess it.")

# Initialize the variables to keep track of the range for guessing and the chances taken
min_guess = lower
max_guess = upper
chance = 1

# Start a loop to allow the computer to make guesses
while chance < 9:
    # Generate a random number within the current guess range (inclusive)
    computer_guess = random.randint(min_guess, max_guess)
    
    # Ask the user if the computer's guess is correct, smaller, or larger
    response = input(f"Is your number {computer_guess}? (Enter 'yes', 'smaller', or 'larger'): ").lower()
    
    # Check the user's response and update the guess range accordingly
    if response == "yes" or min_guess > max_guess:
        print(f"Congratulations! 🎉 I guessed your number, it's {computer_guess}.")
        break
    elif response == "smaller":
        max_guess = computer_guess - 1
    elif response == "larger":
        min_guess = computer_guess + 1
    else:
        print("Invalid response. Please enter 'yes', 'smaller', or 'larger'.")

    # Increment the chance counter
    chance += 1

# Check if the computer has run out of chances (reached the limit of possible guesses)
if chance >= 9:
    print("\nI've run out of chances.")
    sys.exit()
