from .cell_values import CellValue
class Board:
    def __init__(self, dim: int):
        self.dim = dim
        self.move_count = 0
        self._initialize_board(dim)
    
    """
    Helper method to initialize board
    """
    def _initialize_board(self, dim):
        self.grid = []
        for row in range(dim):
            self.grid.append([])
            for _ in range(dim):
                self.grid[row].append(CellValue.Empty)
    """
    Set a cell in grid
    """
    def set_cell(self, row: int, col: int, value: CellValue):
        self.grid[row][col] = value
        self.move_count += 1
    
    """
    Get value of a grid cell
    """
    def get_cell(self, row: int, col: int) -> CellValue:
        return self.grid[row][col]
    
    """
    Display Board
    """
    def display(self):
        for row in range(self.dim):
            for col in range(self.dim):
                print(f'| {self.grid[row][col].value} |', end = " ")
            print()
            print('-----------------')

    """
    Store as a tuple
    """
    def to_tuple(self):
        return tuple(self.get_cell(r, c).value for r in range(self.dim) for c in range(self.dim))
