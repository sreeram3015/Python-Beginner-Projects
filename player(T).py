# player.py: This file contains the classes representing different players in the Tic-Tac-Toe game.

# Importing necessary modules
import random


# Player class: Represents a generic player in the Tic-Tac-Toe game.
class Player:
    def __init__(self, letter):
        # Each player has a letter ('X' or 'O') representing their moves on the board.
        self.letter = letter

    def get_move(self, game):
        # This method is meant to be overridden in subclasses.
        pass

# RandomComputerPlayer class: Represents a computer player that makes random moves on the board.
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        # Call the constructor of the parent class (Player) to set the letter for the computer player.
        super().__init__(letter)

    def get_move(self, game):
        # Get a random move from the available moves on the board.
        square = random.choice(game.get_available_moves())
        return square

# HumanPlayer class: Represents a human player that takes input from the user for moves on the board.
class HumanPlayer(Player):
    def __init__(self, letter):
        # Call the constructor of the parent class (Player) to set the letter for the human player.
        super().__init__(letter)

    def get_move(self, game):
        # Get a valid move from the user.
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn. Enter a move (0-8): ")

            try:
                val = int(square)
                # Check if the entered move is within the available moves on the board.
                if val not in game.get_available_moves():
                    raise ValueError
                
                valid_square = True
            except ValueError:
                print("Invalid move. Please try again.")
        
        return val
