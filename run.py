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