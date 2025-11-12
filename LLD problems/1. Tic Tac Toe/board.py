class Board:
    def __init__(self, size):
        self.size = size
        self.board = [['_' for _ in range(size)] for __ in range(size)]

    def display(self):
        for r in range(self.size):
            for c in range(self.size):
                print(self.board[r][c], end=" ")
            print()

    def make_move(self, x, y, player):
        if x >= self.size or y >= self.size or self.board[x][y] != "_":
            raise ValueError("Invalid Cell / Operation")
        self.board[x][y] = player.symbol    

    def check_winner(self, r, c, symbol):
        # row
        if all(self.board[i][c] == symbol for i in range(self.size)): return True
        
        # column
        if all(self.board[r][i] == symbol for i in range(self.size)): return True 

        # primary diagonal
        if all(self.board[i][i] == symbol for i in range(self.size)): return True

        # secondary diagonal
        if all(self.board[i][self.size - i - 1] == symbol for i in range(self.size)): return True

        return False

    def is_full(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == "_": return False
        return True