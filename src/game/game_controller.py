from src.game.board import Board
from src.game.piece import get_all_pieces
from src.utils.helpers import STATE_SELECT_PIECE, STATE_PLACE_PIECE, STATE_GAME_OVER

class GameController:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.all_pieces = get_all_pieces()
        self.available_pieces = self.all_pieces.copy()
        
        self.current_player_idx = 0
        self.piece_to_place = None
        self.game_state = STATE_SELECT_PIECE
        self.winner = None

    def switch_player(self):
        self.current_player_idx = 1 - self.current_player_idx

    @property
    def current_player(self):
        return self.players[self.current_player_idx]

    @property
    def opponent_player(self):
        return self.players[1 - self.current_player_idx]

    def select_piece_for_opponent(self, piece_id):
        if self.game_state != STATE_SELECT_PIECE:
            return
        
        if piece_id not in self.available_pieces:
            raise ValueError("Piece is not available.")
            
        self.piece_to_place = self.available_pieces.pop(piece_id)
        self.switch_player() # The other player will place the piece
        self.game_state = STATE_PLACE_PIECE

    def place_selected_piece(self, row, col):
        if self.game_state != STATE_PLACE_PIECE:
            return

        is_win = self.board.place_piece(self.piece_to_place, row, col)
        self.piece_to_place = None

        if is_win:
            self.winner = self.current_player
            self.game_state = STATE_GAME_OVER
        elif self.board.is_full:
            self.game_state = STATE_GAME_OVER # It's a draw
        else:
            # The player who just placed the piece now selects for the other
            self.game_state = STATE_SELECT_PIECE

    def reset_game(self):
        self.board = Board()
        self.all_pieces = get_all_pieces()
        self.available_pieces = self.all_pieces.copy()
        self.current_player_idx = 0
        self.piece_to_place = None
        self.game_state = STATE_SELECT_PIECE
        self.winner = None