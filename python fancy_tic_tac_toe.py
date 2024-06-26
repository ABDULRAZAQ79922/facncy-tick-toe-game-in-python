import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Fancy Tic-Tac-Toe")

# Initialize the game board
board = [" " for _ in range(9)]
current_player = "X"

# Create buttons for the game
buttons = []

# Function to check if a player has won
def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Function to handle a player's move
def make_move(index):
    global current_player
    if board[index] == " ":
        board[index] = current_player
        buttons[index].config(text=current_player, state="disabled")
        
        if check_winner(current_player):
            messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")
            reset_board()
        elif " " not in board:
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"
            label.config(text=f"Player {current_player}'s turn")

# Function to reset the game board
def reset_board():
    global board, current_player
    board = [" " for _ in range(9)]
    current_player = "X"
    for button in buttons:
        button.config(text=" ", state="normal")
    label.config(text=f"Player {current_player}'s turn")

# Create a frame for the game board
frame = tk.Frame(root)
frame.pack()

# Create and place buttons on the frame
for i in range(9):
    button = tk.Button(frame, text=" ", font=("Arial", 24), width=5, height=2, command=lambda i=i: make_move(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Create a label to show the current player
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("Arial", 18))
label.pack()

# Start the main loop
root.mainloop()
