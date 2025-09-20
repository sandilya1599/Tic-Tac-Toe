from .cell_values import CellValue
class Board:
    def __init__(self, dim: int):
        self.rows = dim
        self.cols = dim
        self.dim = dim
        self.move_count = 0
        self.__initialize_board__(dim)
    
    """
    Helper method to initialize board
    """
    def __initialize_board__(self, dim):
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
        # TODO: marked for improvement
        for row in range(self.rows):
            for col in range(self.cols):
                print(f'| {self.grid[row][col].value} |', end = " ")
            print()
            print('-----------------')