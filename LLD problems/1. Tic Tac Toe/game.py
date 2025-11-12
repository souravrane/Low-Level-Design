from player import Player
from board import Board

class Game:
    def __init__(self, player1_name, player2_name, size):
        self.players = [Player(player1_name, 'x'), Player(player2_name, "o")]
        self.size = size
        self.board = Board(size)
        self.current_index = 0

    def switch_players(self):
        self.current_index = (self.current_index + 1) % len(self.players)

    def start(self):
        self.board.display()
        while True:
            print()
            print(f"player {self.current_index}")
            current_player = self.players[self.current_index]
            print(f"{current_player.name}'s turn")
            row = int(input(f"Enter the row (0 to {self.size - 1}): "))
            col = int(input(f"Enter the col (0 to {self.size - 1}): "))
            
            try:
                self.board.make_move(row, col, current_player)

                if self.board.check_winner(row, col, current_player.symbol):
                    print(f"{current_player.name} is the WINNER !!")
                    break

                if self.board.is_full():
                    print(f"Its a DRAW")
                    break

                self.switch_players()
            except:
                print(f"Invalid move. Try again")
            
            self.board.display()




game = Game("sahana", "sourav", 3)
game.start()
