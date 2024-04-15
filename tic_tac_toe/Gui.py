class Gui:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.selected_row = 0
        self.selected_column = 0
        self.board = [[" " for _ in range(5)] for _ in range(5)]

    def render(self, message):
        for i in range(self.grid_size):
            for i2 in range(0, self.grid_size):
                if i2 < self.grid_size - 1:
                    print(" " + self.board[i][i2] + " ", end="")

                    if i == self.selected_column and (i2 == self.selected_row - 1 or i2 == self.selected_row):
                        print("-", end="")
                    else:
                        print("|", end="")
                else:
                    print(" " + self.board[i][i2] + " ")

            if i < self.grid_size - 1:
                for i2 in range(0, self.grid_size):
                    if i2 < self.grid_size - 1:
                        print("-", end="")

                        if (i == self.selected_column or i == self.selected_column - 1) and i2 == self.selected_row:
                            print("|", end="")
                        else:
                            print("-", end="")

                        print("-+", end="")
                    else:
                        print("---")

        print('cell (' + str(self.selected_row + 1) + ' ' + str(self.selected_column + 1) + ') selected')
        print(message)