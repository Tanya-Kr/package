def print_chess_board(height, width):
    for board_row in range(height):
        for board_column in range(width):
            if((board_row + board_column) % 2) == 0:
                print("*", end="")
            else:
                print(" ", end="")
        print("")


if __name__ == '__main__':
    print_chess_board(10, 10)