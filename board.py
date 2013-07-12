import re

from sudoku.cell import Cell


class Board:
    
    def __init__(self, cells=None):
        # rows of cols
        self.cells = self._read(cells) if cells else [[Cell() for _ in range(9)] for _ in range(9)]
        self.peers = [[self._peers(row, col) for col in range(9)] for row in range(9)]
    
    def _read(self, cells):
        if isinstance(cells, list):
            return cells
        cells = re.sub(r"[^0-9\.]", '', cells)
        rows = []
        i = 0
        for _ in range(9):
            row = []
            for _ in range(9):
                c = cells[i]
                i += 1
                cell = Cell() if c == '.' else Cell(int(c))
                row.append(cell)
            rows.append(row)
        return rows
    
    def _peers(self, row, col):
        row_peers = [self.cells[row][c] for c in range(9) if c != col]
        col_peers = [self.cells[r][col] for r in range(9) if r != row]
        box = ((row / 3) * 3) + (col / 3)
        box_row = (box / 3) * 3 # starting row
        box_col = (box % 3) * 3 # starting col
        box_peers = [self.cells[r][c] for r in range(box_row, box_row+3) \
                for c in range(box_col, box_col+3) if r != row and c != col]
        return col_peers + row_peers + box_peers
    
    def __str__(self):
        s = ''
        for row in range(9):
            if row % 3 == 0 and row != 0:
                s += '------+-------+------\n'
            for col in range(9):
                value = self.cells[row][col].value
                sep = ' | ' if (col+1) % 3 == 0 else ' '
                s += (str(value) if value else '.') + (sep if col != 8 else '') 
            s += '\n'
        return s
    
    def is_solved(self):
        return all([self.cells[row][col].value for col in range(9) for row in range(9)])
    
    def propagate(self):
        propagated = False
        for row in range(9):
            for col in range(9):
                cell = self.cells[row][col]
                if cell.value:
                    continue
                peers = self.peers[row][col]
                values = [c.value for c in peers if c.value]
                if cell.propagate(set(values)):
                    propagated = True
        if propagated:
            self.propagate()
        return propagated
    
    def get_cell(self):
        """ Return the cell that doesn't yet have a value and has the fewest value options. """
        best = None
        for row in range(9):
            for col in range(9):
                cell = self.cells[row][col]
                if not cell.value and (best is None or (len(cell.values) < len(best.values))):
                    best = cell
        return best
