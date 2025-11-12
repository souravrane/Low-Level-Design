class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [['_' for _ in range(size)] for __ in range(size)]

    def display(self):
        for r in range(self.size):
            for c in range(self.size):
                print(self.grid[r][c], end=" ")
            print()

    def make_move(self, x, y, symbol):
        if x < 0 or y < 0 or x >= self.size or y >= self.size or self.grid[x][y] != "_":
            raise ValueError("Invalid Cell / Operation")
        self.grid[x][y] = symbol    

    def check_winner(self, r, c, symbol):
        # row
        if all(self.grid[i][c] == symbol for i in range(self.size)): return True
        
        # column
        if all(self.grid[r][i] == symbol for i in range(self.size)): return True 

        # primary diagonal
        if all(self.grid[i][i] == symbol for i in range(self.size)): return True

        # secondary diagonal
        if all(self.grid[i][self.size - i - 1] == symbol for i in range(self.size)): return True

        return False

    def is_full(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == "_": return False
        return True