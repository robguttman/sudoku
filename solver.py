from copy import deepcopy

def solve(board):
    board.propagate()
    if board.is_solved():
        return board
    return _solve(board)
    
def _solve(board):
    cell = board.get_cell()
    for value in cell.values:
        cell.set(value)
        board2 = deepcopy(board)
        try:
            board2.propagate()
        except:
            continue # constraint violated
        if board2.is_solved():
            return board2
        solution = _solve(board2)
        if solution:
            return solution
    return False
