import unittest

from cell import Cell
from board import Board


class BoardTests(unittest.TestCase):
    
    def setUp(self):
        cells = "2 3 8 | 7 . . | . 1 9\n" +\
                "6 . . | . . . | 7 . .\n" +\
                ". . . | . . . | . . 5\n" +\
                "------+-------+------\n" +\
                ". . 2 | . 5 . | . . 7\n" +\
                ". . . | 1 . 4 | . . .\n" +\
                "7 . . | . 6 . | 3 . .\n" +\
                "------+-------+------\n" +\
                "1 . . | . . . | . . 6\n" +\
                ". . 4 | . . . | . . 1\n" +\
                "5 9 . | . . 7 | 8 3 4\n"
        self.display = cells
        self.board = Board(cells)
        
    def test_init__no_value(self):
        board = Board()
        for i in range(9):
            for j in range(9):
                self.assertEquals(board.cells[i][j].values, range(1,10))
                self.assertEquals(board.cells[i][j].value, None)
    
    def test_init__value(self):
        cells = [[Cell() for _ in range(9)] for _ in range(9)]
        cells[0][0] = Cell(2)
        board = Board(cells)
        self.assertEquals(board.cells[0][0].values, [2])
        self.assertEquals(board.cells[0][0].value, 2)
        self.assertEquals(board.cells[0][1].values, range(1,10))
        self.assertEquals(board.cells[0][1].value, None)
        self.assertEquals(board.peers[0][0][0], board.cells[1][0]) # col peers first
    
    def test_propagate(self):
        self.assertTrue(self.board.propagate())
    
    def test_is_solved(self):
        self.assertFalse(self.board.is_solved())
    
    def test_get_cell(self):
        cell = self.board.get_cell()
        self.assertEquals(len(cell.values), 9)
    
    def test_get_cell__post_propagate(self):
        self.board.propagate()
        cell = self.board.get_cell()
        self.assertEquals(len(cell.values), 2)
    
    def test_str(self):
        self.assertEquals(str(self.board), self.display)
                          

if __name__ == '__main__':
    unittest.main(argv=[__file__])
