def check_win_condition(board_grid):
    """
    Checks if a winning line exists on the board.

    A winning line is 4 pieces in a row, column, or diagonal that share
    at least one common attribute.

    Args:
        board_grid (list of lists): The 4x4 grid containing Piece objects or None.

    Returns:
        bool: True if a winning condition is met, False otherwise.
    """
    lines = []
    # Rows
    for r in range(4):
        lines.append([board_grid[r][c] for c in range(4)])
    # Columns
    for c in range(4):
        lines.append([board_grid[r][c] for r in range(4)])
    # Diagonals
    lines.append([board_grid[i][i] for i in range(4)])
    lines.append([board_grid[i][3 - i] for i in range(4)])

    for line in lines:
        # A line must be full to be a winning line
        if None in line:
            continue

        # Check for shared attributes
        # Bitwise AND all attributes together. If result is non-zero, they share a "True" attribute.
        # Bitwise AND all NOT-attributes together. If result is non-zero, they share a "False" attribute.
        
        # Check for shared 'True' attributes
        tall_all = all(p.is_tall for p in line)
        dark_all = all(p.is_dark for p in line)
        square_all = all(p.is_square for p in line)
        solid_all = all(p.is_solid for p in line)

        # Check for shared 'False' attributes
        short_all = all(not p.is_tall for p in line)
        light_all = all(not p.is_dark for p in line)
        circle_all = all(not p.is_square for p in line)
        hollow_all = all(not p.is_solid for p in line)

        if any([tall_all, dark_all, square_all, solid_all, short_all, light_all, circle_all, hollow_all]):
            return True

    return False