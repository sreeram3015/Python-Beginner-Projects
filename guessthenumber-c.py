import random
import sys

# Input the lower and upper limits for the random number range
lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

# Generate a random number within the given range (inclusive)
random_num = random.randint(lower, upper)

# Inform the user to guess the random number and provide 8 chances to guess
print("Now guess the number chosen by the system between", lower, "and", upper)
print("You have 8 chances!")

# Initialize the variable to keep track of the user's chances
chances = 0

# Start a loop to allow the user to make guesses
for chances in range(8):
    while True:
        # Ask the user to enter their guess
        guess = int(input("Enter your guess: "))

        # Compare the user's guess with the random number
        if random_num == guess:
            print("Congratulations!🎉 You are correct. The number was", random_num)
            sys.exit()
        elif guess < random_num:
            print("You guessed a smaller number. Try again.")
        elif guess > random_num:
            print("You guessed a larger number. Try again.")

        # Check if the user has run out of chances
        if chances == 7:
            print("\nYou've run out of chances")
            print("The number was", random_num)
            print("Better luck next time.")
            sys.exit()

        print("\n")
        break
