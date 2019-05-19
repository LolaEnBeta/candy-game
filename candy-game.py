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

def get_limits(row, column):
    row_initial_limit = row - 1
    row_end_limit = row + 1
    column_initial_limit = column - 1
    column_end_limit = column + 1

    if row == 0:
        row_initial_limit = row
    elif row == board_size - 1:
        row_end_limit = row

    if column == 0:
        column_initial_limit = column
    elif column == board_size -1:
        column_end_limit = column

    return row_initial_limit, row_end_limit, column_initial_limit, column_end_limit

def delete_runes(board, row, column, choosen_rune):

    row_init, row_end, col_init, col_end = get_limits(row, column)

    for row_index in range(row_init, row_end + 1):
        if row_index == row:
            for column_index in range(col_init, col_end + 1):
                if board[row_index][column_index] == choosen_rune:
                    board[row_index][column_index] = "-"
        else:
            if board[row_index][column] == choosen_rune:
                board[row_index][column] = "-"

# def move_runes_down(board):
#     for row_index in reversed(range(len(board))):
#         for column_index in range(len(board)):
#             if board[row_index][column_index] == "-" and row_index != 0:
#                 board[row_index][column_index] = board[row_index-1][column_index]
#                 board[row_index-1][column_index] = "-"

candy_game = create_board(board_size)

generate_rune(candy_game)

print_board(candy_game)

life = 5
while life > 0:
    row = int(input("Choose one row: "))
    column = int(input("Choose one column: "))
    choosen_rune = candy_game[row][column]

    delete_runes(candy_game, row, column, choosen_rune)
    # move_runes_down(candy_game)
    print_board(candy_game)
    life -=1
