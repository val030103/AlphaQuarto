from src.players.base_player import BasePlayer

class HumanPlayer(BasePlayer):
    def __init__(self, name):
        super().__init__(name)

    def get_move(self, game_state):
        # For a human player, moves are determined by GUI clicks,
        # so this method might not be directly used in the same way
        # as it would for an AI player.
        pass