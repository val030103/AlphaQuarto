import tkinter as tk
from src.utils.helpers import STATE_SELECT_PIECE, STATE_PLACE_PIECE, STATE_GAME_OVER

class GUIController:
    def __init__(self, game_controller, game_view):
        self.game_ctrl = game_controller
        self.view = game_view
        self.view.set_controller(self)
        self.update_view()

    def handle_piece_click(self, piece_id):
        if self.game_ctrl.game_state == STATE_SELECT_PIECE:
            try:
                self.game_ctrl.select_piece_for_opponent(piece_id)
                self.update_view()
            except ValueError as e:
                print(e) # Piece already used

    def handle_board_click(self, row, col):
        if self.game_ctrl.game_state == STATE_PLACE_PIECE:
            if self.game_ctrl.board.get_piece(row, col) is None:
                self.game_ctrl.place_selected_piece(row, col)
                self.update_view()

    def handle_reset_click(self):
        self.game_ctrl.reset_game()
        self.update_view()

    def update_view(self):
        self.view.draw_board(self.game_ctrl.board)
        self.view.draw_available_pieces(
            self.game_ctrl.available_pieces,
            self.game_ctrl.all_pieces
        )
        self.view.update_status_message(
            self.game_ctrl.game_state,
            self.game_ctrl.current_player,
            self.game_ctrl.piece_to_place,
            self.game_ctrl.winner
        )