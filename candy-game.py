
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

candy_game = create_board(board_size)

print_board(candy_game)
