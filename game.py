# game.py: This file contains the main Tic-Tac-Toe game logic.

# Importing necessary modules
import time

from player import HumanPlayer, RandomComputerPlayer


# TicTacToe class: Represents the Tic-Tac-Toe game.
class TicTacToe:
    def __init__(self):
        # Initialize the game board as a list of empty spaces (' ') to represent an empty board.
        self.board = [' ' for _ in range(9)]
        # Initialize the current_winner to None, indicating that no player has won yet.
        self.current_winner = None

    def print_board(self):
        # Print the Tic-Tac-Toe board with current moves.
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums():
        # Print the board with the numbers representing each position on the Tic-Tac-Toe board.
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def get_available_moves(self):
        # Get a list of available moves (positions) on the board.
        moves = []
        for (i, spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
        return moves

    def is_board_full(self):
        # Check if the board is full (no more available moves).
        return ' ' not in self.board

    def make_move(self, position, letter):
        # Make a move on the board at the specified position with the given letter (player's letter).
        if self.board[position] == ' ':
            self.board[position] = letter
            # Check if the player who made the move has won the game.
            if self.is_winner(position, letter):
                self.current_winner = letter
            return True
        return False  

    def is_winner(self, position, letter):
        # Check if the player who made the move at the specified position has won the game.
        row_index = position // 3
        row = self.board[row_index * 3: (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        col_index = position % 3
        column = [self.board[col_index + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # Check diagonals if the position is on an even index (0, 2, 4, 6, or 8).
        if position % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

# play function: This function starts and manages the Tic-Tac-Toe game between two players.
def play(game, x_player, o_player, print_game=True):
    # Print the board numbers if specified to make it easier for the players to choose their moves.
    if print_game:
        game.print_board_nums()

    letter = 'X'

    while game.get_available_moves():
        # Get the move from the current player based on their letter ('X' or 'O').
        if letter == 'O':
            position = o_player.get_move(game)
        else:
            position = x_player.get_move(game)
        
        # Make the move on the board and display it.
        if game.make_move(position, letter):
            if print_game:
                print(letter + f" makes a move to square {position}")
                game.print_board()
                print(' ')

            # Check if the current player has won the game.
            if game.current_winner:
                if print_game:
                    print(letter + " wins the game!")
                return letter
            
            # Switch the player's turn ('X' -> 'O' or 'O' -> 'X').
            letter = 'O' if letter == 'X' else 'X'
    time.sleep(1)

    if print_game:
        print("It's a tie! The game is over.")

# The main section where the game is initialized and played.
if __name__ == '__main__':
    # Create instances of players ('X' as HumanPlayer and 'O' as RandomComputerPlayer).
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    # Create an instance of the TicTacToe game.
    tictactoe_game = TicTacToe()
    # Start the game with the specified players.
    play(tictactoe_game, x_player, o_player, print_game=True)
