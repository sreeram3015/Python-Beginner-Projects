import random
import string

from words import words  # Import the list of words for the game


def get_valid_word(words):
    """
    Get a valid word for the game by randomly selecting from the provided list of words.
    Ensure that the word does not contain any hyphens or spaces.
    Convert the selected word to uppercase and return it.
    """
    word = random.choice(words)

    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    """
    The main function to play the Hangman game.
    """
    word = get_valid_word(words)  # Get a valid word to guess
    word_letters = set(word)  # Convert the word into a set of its unique letters
    alphabets = set(string.ascii_uppercase)  # Create a set of all uppercase alphabets
    used_letters = set()  # Set to keep track of letters guessed by the user
    chances = 7  # Number of chances the player has to guess the word

    while len(word_letters) > 0 and chances > 0:
        print("═════════════════════════════")
        print(f"You have {chances} {'chance' if chances == 1 else 'chances'} left.")
        print(f"You've used these letters: {' '.join(used_letters)}")

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word:", ' '.join(word_list))  # Display the current state of the word with guessed letters

        user_letter = input("Guess a letter: ").upper()  # Prompt the user to guess a letter and convert it to uppercase

        if user_letter in alphabets - used_letters:
            used_letters.add(user_letter)  # Add the guessed letter to the set of used letters
            if user_letter in word_letters:
                word_letters.remove(user_letter)  # If the guessed letter is in the word, remove it from the set of word letters
            else:
                chances -= 1
                print("Oops! The letter is not in the word.")
        elif user_letter in used_letters:
            print("You've already guessed this letter!")  # If the letter has already been guessed, inform the player
        else:
            print("Invalid character! Please guess a valid letter.")  # If the input is not a valid letter, inform the player

    if chances == 0:
        print(f"Game Over! 😔 The word was '{word}'. Better luck next time!")  # Player ran out of chances, reveal the word
    else:
        print(f"Congratulations! 🎉 You've guessed the word '{word}'!")  # Player guessed the word successfully

hangman()
