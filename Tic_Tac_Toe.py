# -------------------------------
# Tic-Tac-Toe Game
# -------------------------------

def create_board():
    #Creates a 3x3 game board."
    return [[" " for _ in range(3)] for _ in range(3)]


def display_board(board):
    #Displays the game board with row and column numbers.
    print("\n    0   1   2")
    print("  -------------")
    for i, row in enumerate(board):
        print(f"{i} | {' | '.join(row)} |")
        print("  -------------")
    print()


def player_move(board, player):
    #Handles a player's move.
    while True:
        try:
            row = int(input(f"Player {player}, enter the row (0-2): "))
            col = int(input(f"Player {player}, enter the column (0-2): "))

            if row not in range(3) or col not in range(3):
                print("Invalid input! Row and column must be between 0 and 2.")
                continue

            if board[row][col] != " ":
                print("That cell is already taken! Try again.")
                continue

            board[row][col] = player
            break

        except ValueError:
            print("Please enter a valid number!")


def check_winner(board, player):
    #Checks if a player has won.

    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_draw(board):
    #Checks if the game is a draw.
    return all(cell != " " for row in board for cell in row)


def main():
    #Main game loop.
    board = create_board()
    current_player = "X"

    print("Welcome to Tic-Tac-Toe Game!\n")
    display_board(board)

    while True:
        player_move(board, current_player)
        display_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"


# Run the game
if __name__ == "__main__":
    main()