import unittest
from board import Board

class GameTest(unittest.TestCase):
    def setUp(self):
        self.board = Board(size = 3)
        self.grid = self.board.grid
    
    def test_make_move_success(self):
        move = self.board.make_move(0, 0, "x")
        self.assertEqual(self.grid[0][0], "x")
    
    def test_make_move_invalid(self):
        self.assertRaises(ValueError, self.board.make_move, -1, -1, "x")

    def test_row_win(self):
        self.board.make_move(0, 0, "x")
        self.board.make_move(0, 1, "x")
        self.board.make_move(0, 2, "x")
        self.assertTrue(self.board.check_winner(0,2,"x"))


unittest.main()
