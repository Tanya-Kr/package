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


if __name__ == '__main__':
    continue_ = True
    while continue_:
        try:
            board_height = int(input("Enter board height: "))
            board_width = int(input("Enter board width: "))
            if board_height > 1 and board_width > 1:
                Chess_board(board_height, board_width).print_chess_board()
            else:
                raise ValueError
        except ValueError:
            print("Please enter integer numbers!")

        continue_ = input("Do you want add another board (y / n): ").lower() == "y"