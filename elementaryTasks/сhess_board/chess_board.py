class Chess_board:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def print_chess_board(self):
        for board_row in range(self.height):
            for board_column in range(self.width):
                if ((board_row + board_column) % 2) == 0:
                    print("*", end="")
                else:
                    print(" ", end="")
            print("")


board_1 = Chess_board(10, 15)

if __name__ == '__main__':
    board_1.print_chess_board()