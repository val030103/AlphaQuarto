from typing import NamedTuple

class Piece(NamedTuple):
    """
    Represents a Quarto piece with 4 binary attributes.
    - is_tall: True for tall, False for short
    - is_dark: True for dark, False for light
    - is_square: True for square, False for circle
    - is_solid: True for solid-top, False for hollow-top
    """
    id: int
    is_tall: bool
    is_dark: bool
    is_square: bool
    is_solid: bool

def get_all_pieces():
    """Generates all 16 unique Quarto pieces."""
    pieces = {}
    for i in range(16):
        is_tall = (i >> 3) & 1 == 1
        is_dark = (i >> 2) & 1 == 1
        is_square = (i >> 1) & 1 == 1
        is_solid = i & 1 == 1
        pieces[i] = Piece(id=i, is_tall=is_tall, is_dark=is_dark, is_square=is_square, is_solid=is_solid)
    return pieces