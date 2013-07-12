import unittest

from sudoku.cell import Cell


class CellTests(unittest.TestCase):
    
    def test_init__no_value(self):
        cell = Cell()
        self.assertEquals(cell.values, range(1,10))
        self.assertEquals(cell.options, [])
        self.assertRaises(Exception, cell.value)

    def test_init__value(self):
        cell = Cell(2)
        self.assertEquals(cell.values, [2])
        self.assertEquals(cell.options, [])
        self.assertEquals(cell.value, 2)

    def test_propagate__has_value(self):
        cell = Cell(2)
        propagated = cell.propagate([0, 1])
        self.assertEquals(propagated, None)

    def test_propagate(self):
        cell = Cell()
        propagated = cell.propagate([1, 2])
        self.assertEquals(propagated, True)
        self.assertEquals(cell.values, range(3,10))

    def test_set__has_value(self):
        cell = Cell(2)
        self.assertRaises(Exception, cell.set, 1)

    def test_set(self):
        cell = Cell()
        cell.set(1)
        self.assertEquals(cell.values, [1])
        self.assertEquals(cell.options, range(1,10))

    def test_unset(self):
        cell = Cell()
        cell.set(1)
        cell.unset()
        self.assertEquals(cell.values, range(1,10))
        self.assertEquals(cell.options, [])


if __name__ == '__main__':
    unittest.main(argv=[__file__])
