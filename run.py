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


def play_again():
    """Asks the user if they want to play again."""
    print("Thank you for playing, {}.".format(player_name))
    try_again = input("Do you want to play again? y or n? >: ").lower()
    return try_again == "y"


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


    while True:
        try:
            print_game_board(player_board, computer_board)
            try:
                row = int(input(f"{Fore.YELLOW}Enter a row 1 to 5: {Style.RESET_ALL}"))
            except ValueError:
                print(f"{Fore.CYAN}Only enter numbers!{Style.RESET_ALL}")
                continue
        
            # Validating user input for row
            if row not in range(1, 6):
                print(f"{Fore.CYAN}\nInvalid input for row. Please enter valid numbers between 1-5!\n{Style.RESET_ALL}")
                continue
        
            try:
                column = int(input(f"{Fore.YELLOW}Enter a column 1 to 5: {Style.RESET_ALL}"))
            except ValueError:
                print(f"{Fore.CYAN}Only enter numbers!{Style.RESET_ALL}")
                continue

            # Validating user input for column
            if column not in range(1, 6):
                print(f"{Fore.CYAN}\nInvalid input for column. Please enter valid numbers between 1-5!\n{Style.RESET_ALL}")
                continue

            row -= 1  # Reducing number to the desired index.
            column -= 1  # Reducing number to the desired index.

            # Handling player's moves and checking for hits or misses
            if player_board[row][column] == "-" or player_board[row][column] == "X":
                print(f"{Fore.CYAN}\nYou have already made a move in this position. Try again.\n{Style.RESET_ALL}")
                continue
            elif (row, column) == computer_ship1 or (row, column) == computer_ship2 or (row, column) == computer_ship3:
                print(f"{Fore.GREEN}\nBoom! You hit! A ship has exploded!\n{Style.RESET_ALL}")
                player_board[row][column] = "X"
                ships_left -= 1
                if ships_left == 0:
                    print(f"Your ships left: {ships_left}")
                    print(f"{Fore.GREEN}\nThe computer hit the ship at {computer_row+1}, {computer_column+1}!\n{Style.RESET_ALL}")
                    print(f"Computer's ships left: {computer_ships_left}")
                    print(f"{Fore.CYAN}Congratulations, you won!\n{Style.RESET_ALL}")
                    break
            else:
                print(f"{Fore.RED}\nYou missed!\n{Style.RESET_ALL}")
                player_board[row][column] = "-"

            print(f"Your ships left: {ships_left}")

            # Get computer's move by calling the computer_move function
            computer_row, computer_column = computer_move(used_computer_positions)
            # Check if the computer's chosen position on the board is either an empty space or already hit by the computer
            # If yes, continue to the next iteration of the loop
            if computer_board[computer_row][computer_column] == "-" or computer_board[computer_row][computer_column] == "X":
                continue 
            # If the computer's chosen position matches any of the player's ships' positions
            elif (computer_row, computer_column) == ship1 or (computer_row, computer_column) == ship2 or (computer_row, computer_column) == ship3:
                
                print(f"{Fore.GREEN}\nThe computer hit the ship at {computer_row+1}, {computer_column+1}!\n{Style.RESET_ALL}")
                computer_board[computer_row][computer_column] = "X"
                computer_ships_left -= 1

                # Check if the computer has sunk all the player's ships
                # If yes, prints a victory message and breaks out of the loop
                if computer_ships_left == 0:
                    print(f"Computer's ships left: {computer_ships_left}")
                    print(f"{Fore.CYAN}The computer won!\n{Style.RESET_ALL}")
                    break 
            # If the chosen position is neither empty nor a hit on the player's ships
            else:
                print(f"{Fore.RED}\nThe computer missed at {computer_row+1}, {computer_column+1}!\n{Style.RESET_ALL}")
                computer_board[computer_row][computer_column] = "-"

            print(f"Computer's ships left: {computer_ships_left}\n")

            if computer_ships_left == 0 and ships_left == 0:
                print("It's a tie!")
        
        except KeyboardInterrupt:
            # Handle keyboard interrupt
            print("\nGame interrupted.")
            break
   

while True:
        play_game()
        if not play_again():
            break