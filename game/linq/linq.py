from game import Game
from typing import List

class Linq(Game):
    def __init__(self, player_number: int, maximum_number_of_round: int = 2):
        super().__init__()
        self.game_over = False
        self.player_number = player_number
        self.maximum_number_of_round = maximum_number_of_round * player_number
        self.scores = [0 for i in range(player_number)]
        self.active_player_index = 0
        self.winner_index = None
        self.name = "Linq"

    """ --- GETTERS --- """
    def get_game_over(self) -> bool:
        return self.game_over

    def get_player_number(self) -> int:
        return self.player_number

    def get_maximum_number_of_round(self) -> int:
        return self.maximum_number_of_round

    def get_scores(self) -> list:
        return self.scores

    def get_active_player_index(self) -> List[int]:
        return self.active_players_indexes

    def get_winner_index(self) -> List[int]:
        return self.winner_index

    def get_name(self) -> str:
        return self.name

    """ --- SETTERS --- """
    def set_game_over(self, value):
        self.game_over = value

    def set_player_number(self, value):
        self.player_number = value

    def set_maximum_number_of_round(self, value):
        self.maximum_number_of_round = value

    def set_scores(self, value):
        self.scores = value

    def set_active_player_index(self, value):
        self.active_players_indexes = value

    def set_winner_index(self, value):
        self.winner_index = value

    def set_name(self, value):
        self.name = value

    """ --- METHODS --- """
    def start_of_round_procedure(self):
        raise NotImplementedError

    def end_of_round_procedure(self):
        raise NotImplementedError

    def end_of_game_procedure(self):
        raise NotImplementedError

    def step(self):
        raise NotImplementedError

    def get_available_actions(self, player_index: int):
        raise NotImplementedError
