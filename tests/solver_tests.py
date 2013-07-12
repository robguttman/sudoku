import time
import unittest

from solver import solve
from board import Board


class BoardTests(unittest.TestCase):
    
    def test_solve__easy(self):
        cells = """
            2 3 8 | 7 . . | . 1 9
            6 . . | . . . | 7 . .
            . . . | . . . | . . 5
            ------+-------+------
            . . 2 | . 5 . | . . 7
            . . . | 1 . 4 | . . .
            7 . . | . 6 . | 3 . .
            ------+-------+------
            1 . . | . . . | . . 6
            . . 4 | . . . | . . 1
            5 9 . | . . 7 | 8 3 4
        """
        self.solve(cells)
    
    def test_solve__moderate(self):
        cells = """
            . . . | 6 . 3 | . . .
            . 9 8 | . . . | 6 4 .
            . . 6 | 5 4 . | 8 . .
            ------+-------+------
            . . . | . . . | . 3 .
            3 . 2 | . . . | 1 . 6
            . 6 . | 1 . . | . . .
            ------+-------+------
            . . 4 | . 9 1 | 7 . .
            . 1 9 | . . . | 3 2 .
            . . . | 7 . 5 | . . .
        """
        self.solve(cells)
    
    def test_solve__diabolical(self):
        cells = """
            . . 7 | . . . | 2 . .
            . 9 3 | . 8 . | . 6 .
            . 4 . | . . 9 | . . .
            ------+-------+------
            8 . . | . . . | 4 . .
            . . . | . 7 . | 1 . .
            5 . 2 | . . . | . . 7
            ------+-------+------
            . . . | . 3 . | . 8 .
            . 8 . | . 6 . | 5 . .
            . . . | 4 . . | 6 . .
        """
        self.solve(cells)
    
#    def test_solve__impossible(self):
#        cells = """
#            . . . | . . 5 | . 8 . 
#            . . . | 6 . 1 | . 4 3 
#            . . . | . . . | . . . 
#            ------+-------+------
#            . 1 . | 5 . . | . . . 
#            . . . | 1 . 6 | . . . 
#            3 . . | . . . | . . 5 
#            ------+-------+------
#            5 3 . | . . . | . 6 1 
#            . . . | . . . | . . 4 
#            . . . | . . . | . . .
#        """
#        self.solve(cells)
    
    def solve(self, cells):
        board = Board(cells)
        print "\nOriginal board:\n"
        print board
        start = time.time()
        solution = solve(board)
        duration = time.time() - start
        self.assertTrue(solution)
        print "Solution in %.3f seconds:\n" % duration
        print solution


if __name__ == '__main__':
    unittest.main(argv=[__file__])
