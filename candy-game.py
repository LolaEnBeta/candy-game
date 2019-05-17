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

def delete_runes(board, row, column, choosen_rune):
    for row_index in range(row - 1, row + 2):
        if row_index == row:
            for column_index in range(column - 1, column +2):
                if board[row_index][column_index] == board[row][column]:
                    board[row_index][column_index] = "-"
                else:
                    if board[row_index][column_index] == choosen_rune:
                        board[row_index][column_index] = "-"
        else:
            if board[row_index][column] == choosen_rune:
                board[row_index][column] = "-"

candy_game = create_board(board_size)

generate_rune(candy_game)

print_board(candy_game)

row = int(input("Choose one row: "))
column = int(input("Choose one column: "))
choosen_rune = candy_game[row][column]

delete_runes(candy_game, row, column, choosen_rune)

print_board(candy_game)
