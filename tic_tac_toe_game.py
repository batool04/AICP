# -*- coding: utf-8 -*-
"""Tic_Tac_Toe_game.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FnJa72R1UphO4qpwqwx9Tqry6t9azlXj
"""

# Initialize the Tic-Tac-Toe board with empty spaces
board = [" "]*9

# Function to print the Tic-Tac-Toe board
def print_board():
    [print("|", *board[i:i+3], "|") for i in range(0, 9, 3)]
    print()

# Function for a player's move
def player_move(icon):
    print_board()
    while True:
        try:
            # Get the player's move input
            choice = int(input(f"Player {icon}'s turn. Enter your move (1-9): ").strip())

            # Check if the move is valid
            if 1 <= choice <= 9 and board[choice-1] == " ":
                board[choice-1] = icon
                break
            else:
                print("Invalid move. Please choose an empty space (1-9).")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to check if a player has won
def is_victory(icon):
    # Define winning combinations
    winning_combinations = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

    # Check if any winning combination is present
    return any(all(board[i] == icon for i in combo) for combo in winning_combinations)

# Function to check if the game is a draw
def is_draw():
    # Check if there are no empty spaces left on the board
    return " " not in board

# Main game loop
while True:
    player_move("X")
    if is_victory("X") or is_draw():
        break

    player_move("O")
    if is_victory("O") or is_draw():
        break

# Display the final state of the board
print_board()

# Display the result of the game
if is_victory("X"):
    print("X wins! Congratulations!")
elif is_victory("O"):
    print("O wins! Congratulations!")
else:
    print("It's a draw!")