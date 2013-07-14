import time
import unittest

from solver import solve
from board import Board


class SolverTests(unittest.TestCase):
    
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
        self.solve(cells, "easy")
    
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
        self.solve(cells, "moderate")
    
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
        self.solve(cells, "diabolical")
    
    def test_solve__norvig_example(self):
        cells = """
            4 . . | . . . | 8 . 5 
            . 3 . | . . . | . . . 
            . . . | 7 . . | . . . 
            ------+-------+-------
            . 2 . | . . . | . 6 . 
            . . . | . 8 . | 4 . . 
            . . . | . 1 . | . . . 
            ------+-------+-------
            . . . | 6 . 3 | . 7 . 
            5 . . | 2 . . | . . . 
            1 . 4 | . . . | . . . 
        """
        self.solve(cells, "norvig")
    
    def test_solve__inkala1(self):
        cells = """
            8 5 . |. . 2 |4 . . 
            7 2 . |. . . |. . 9 
            . . 4 |. . . |. . . 
            ------+------+------
            . . . |1 . 7 |. . 2 
            3 . 5 |. . . |9 . . 
            . 4 . |. . . |. . . 
            ------+------+------
            . . . |. 8 . |. 7 . 
            . 1 7 |. . . |. . . 
            . . . |. 3 6 |. 4 . 
        """
        self.solve(cells, "inkala1")
    
    def test_solve__inkala2(self):
        cells = """
            . . 5 |3 . . |. . . 
            8 . . |. . . |. 2 . 
            . 7 . |. 1 . |5 . . 
            ------+------+------
            4 . . |. . 5 |3 . . 
            . 1 . |. 7 . |. . 6 
            . . 3 |2 . . |. 8 . 
            ------+------+------
            . 6 . |5 . . |. . 9 
            . . 4 |. . . |. 3 . 
            . . . |. . 9 |7 . . 
        """
        self.solve(cells, "inkala2")
        
#    def test_solve__hard1(self): # took 1.7 hours to solve this one on MacBook Air
#        cells = """
#            . . . |. . 6 |. . . 
#            . 5 9 |. . . |. . 8 
#            2 . . |. . 8 |. . . 
#            ------+------+------
#            . 4 5 |. . . |. . . 
#            . . 3 |. . . |. . . 
#            . . 6 |. . 3 |. 5 4 
#            ------+------+------
#            . . . |3 2 5 |. . 6 
#            . . . |. . . |. . . 
#            . . . |. . . |. . . 
#        """
#        self.solve(cells, "hard1")
    
    def solve(self, cells, name=''):
        board = Board(cells)
        print "\nOriginal board (%s):\n" % name
        print board
        start = time.time()
        solution = solve(board)
        duration = time.time() - start
        self.assertTrue(solution)
        print "Solution in %.3f seconds:\n" % duration
        print solution


if __name__ == '__main__':
    unittest.main(argv=[__file__])
