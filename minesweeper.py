# Import required libraries
import random
import re


# Board class to represent the Minesweeper game
class Board:
    # Constructor to initialize the board
    def __init__(self, dim_size, num_bombs):
        # Store the dimensions and number of bombs
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # Create a new board and plant the bombs
        self.board = self.make_new_board()
        self.assign_values_to_board()

        # Initialize a set to keep track of dug locations
        self.dug = set()

    # Function to create a new board with bombs planted
    def make_new_board(self):
        # Create an empty board with None values
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        # Plant the bombs randomly on the board
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1) # Randomly choose a location on the board
            row = loc // self.dim_size  # Calculate row index from location
            col = loc % self.dim_size   # Calculate column index from location

            # If the location already has a bomb, continue to find another location
            if board[row][col] == '*':
                continue

            # Plant the bomb at the location
            board[row][col] = '*'
            bombs_planted += 1

        return board

    # Function to assign numbers to each cell based on neighboring bombs
    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    # Function to count neighboring bombs for a given cell
    def get_num_neighboring_bombs(self, row, col):
        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1

        return num_neighboring_bombs

    # Function to dig at a specific cell
    def dig(self, row, col):
        # Add the cell to the set of dug locations
        self.dug.add((row, col))

        # If the cell has a bomb, return False indicating game over
        if self.board[row][col] == '*':
            return False
        # If the cell has neighboring bombs, return True (finish dig)
        elif self.board[row][col] > 0:
            return True

        # If the cell is empty, recursively dig neighboring cells until neighboring bombs are encountered
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)

        return True

    # Function to represent the board as a string
    def __str__(self):
        # Create a visible board to display to the player
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        # Fill the visible board based on dug locations and neighboring bomb values
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        # Create a string representation of the visible board
        string_rep = ''
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            string_rep += ' |'.join(row)
            string_rep += ' |\n'

        return string_rep

# Function to play the Minesweeper game
def play(dim_size=10, num_bombs=10):
    # Create the board and start playing
    board = Board(dim_size, num_bombs)
    safe = True 

    # Continue playing until the game is over or the player wins
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        # Ask the player for a location to dig
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))
        row, col = int(user_input[0]), int(user_input[-1])

        # Check if the input is valid
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Try again.")
            continue

        # Dig at the specified location and check if it's safe
        safe = board.dig(row, col)
        if not safe:
            break

    # Print game over message and reveal the whole board
    if safe:
        print("CONGRATULATIONS!!!! YOU ARE VICTORIOUS!")
    else:
        print("SORRY GAME OVER :(")
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

# Start the game
if __name__ == '__main__':
    play()
