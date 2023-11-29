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


def computer_move(used_positions):
    """
    Generates a random move for the computer.
    Prevents the computer from making duplicate moves on the same position.
    """
    while True:
        move = (random.randint(0, 4), random.randint(0, 4))
        if move not in used_positions:
            used_positions.add(move)
            return move

def play_game():
    """
    Plays the battleship game.
    """
    clear_screen()
    print(Fore.CYAN + "Welcome to the BATTLESHIP GAME!" + Style.RESET_ALL)
    player_name = input("Enter your name: ")
    print(f"Greetings, {Fore.CYAN}{player_name}{Style.RESET_ALL}! Let's start the BATTLESHIP GAME!"
          "\nSink all of the ships before the opponent sinks them.\n")
    print("Missed shots are marked with '-', and hit ships are marked with 'X'.")
    input(f"{Fore.YELLOW}Press Enter to start the game...{Style.RESET_ALL}")

    # Sets to store used positions for player and computer ships
    used_ship_positions = set()
    used_computer_positions = set()

    # Placing player's ships randomly on the board
    ship1 = create_random_ship(used_ship_positions)
    ship2 = create_random_ship(used_ship_positions)
    ship3 = create_random_ship(used_ship_positions)

    # Placing computer's ships randomly on the board
    computer_ship1 = create_random_ship(used_computer_positions)
    computer_ship2 = create_random_ship(used_computer_positions)
    computer_ship3 = create_random_ship(used_computer_positions)

    # Initializing game boards for the player and computer
    player_board = [["O" for _ in range(5)] for _ in range(5)]
    computer_board = [["O" for _ in range(5)] for _ in range(5)]

    # Initializing ship counts for player and computer
    ships_left = 3
    computer_ships_left = 3


play_game()