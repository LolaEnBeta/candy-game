import random
board_size = 5

def create_board(board_size):
    board = []
    for row in range(board_size):
        row = []
        for column in range(board_size):
            row.append("-")
        board.append(row)
    return board

def print_board(board):
    for row in board:
        for column in row:
            print(column, "", end="")
        print("")

def generate_rune(board):
    for row_index in range(len(board)):
        for column_index in range(len(board)):
            board[row_index][column_index] = random.choice(["X", "O", "H"])

candy_game = create_board(board_size)

generate_rune(candy_game)

print_board(candy_game)
