from game import Game
import numpy as np


class Agent:
    def __init__(self):
        self.display_mode = 0
        self.name = None

    def act(self, game_state: Game) -> int:
        raise NotImplementedError

    def observe(self,
                reward: float,
                terminated: bool,
                player_index: int):
        raise NotImplementedError

    def update_display_mode(self, value: int):
        if 0 <= value <= 2:
            self.display_mode = value

    def get_display_mode(self):
        return self.display_mode

    def get_name(self):
        return self.name

    def save_model(self):
        raise NotImplementedError

    def load_model(self, path):
        raise NotImplementedError


class RandomAgent(Agent):
    def act(self, game_state: Game) -> int:
        available_actions = game_state.get_available_actions(game_state.get_active_player_index())
        return np.random.choice(available_actions)

    def observe(self, reward: float, player_index: int, terminated: bool):
        pass

    def get_name(self):
        return "RandomAgent"

    def save_model(self):
        pass

    def load_model(self, path):
        pass


class CommandLineAgent(Agent):
    """Command line agent.

    Allows to select an action for the given game state via command ligne terminal.
    """
    def act(self, game_state: Game) -> int:
        """Function retrieving the action

        :param game_state: GameState
             Concerned Game State.
        :return: int
            The value of the chosen action.
        """
        # Get list of available actions
        available_actions = game_state.get_available_actions(game_state.get_active_player_index())
        #
        print(f"Choose action index from : {available_actions}")

        while True:
            try:
                action_candidate = int(input("> "))
                if action_candidate in available_actions:
                    break
            except Exception as _:
                pass
            print(f"Unavailable action")
        return action_candidate

    def observe(self, reward: float, player_index: int, terminated: bool):
        pass

    def save_model(self):
        pass

    def load_model(self, path):
        pass

    def get_name(self):
        return ""