import os
import random
from colorama import Fore, Style


def clear_screen():
    """
    Clears the termina screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def colorize_cell(cell):
    """
    Colorizes the symbols.
    """
    colors = {
        '-': '\033[91m',  # Red for missed shots
        'X': '\033[92m',  # Green for hit ships
    }
    return f"{colors.get(cell, '')}{cell}\033[0m"



def print_game_board(player_board, computer_board):
    """
    Prints the game board for both the player and the computer.
    """
    print("    Your Board            Computer's Board")
    print("    1 2 3 4 5             1 2 3 4 5")
    for i, (player_row, computer_row) in enumerate(zip(player_board, computer_board), start=1):
        print(f"{i} | {' '.join(colorize_cell(cell) for cell in player_row)}    |    {i} | {' '.join(colorize_cell(cell) for cell in computer_row)}")


def create_random_ship(used_positions):
    """
    Creates a random ship position that is not used.
    It keeps track of ship positions already generated on the game board,
    and creates a random ship position that hasn't been used before.
    """
    while True:
        ship_position = (random.randint(0, 4), random.randint(0, 4))
        if ship_position not in used_positions:
            used_positions.add(ship_position)
            return ship_position


def play_game():
    """
    Plays the battleship game.
    """
    clear_screen()

    # Initializing game boards for the player and computer
    player_board = [["O" for _ in range(5)] for _ in range(5)]
    computer_board = [["O" for _ in range(5)] for _ in range(5)]


play_game()