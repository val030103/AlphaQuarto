from src.game.rules import check_win_condition

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(4)] for _ in range(4)]
        self.is_full = False

    def place_piece(self, piece, row, col):
        """Places a piece on the board and checks for a win."""
        if self.grid[row][col] is not None:
            raise ValueError("Cell is already occupied")
        
        self.grid[row][col] = piece
        
        if all(cell is not None for row in self.grid for cell in row):
            self.is_full = True

        return check_win_condition(self.grid)

    def get_piece(self, row, col):
        return self.grid[row][col]