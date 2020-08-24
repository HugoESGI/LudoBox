import sys
from typing import List
from game import Game
from game.linq import Linq
from agents import RandomAgent, Agent


def run_step(agents: List[Agent], game_state: GameState) -> None:
    """Triggers one new step of an environment for the active player running with given agents.
    Then checks if this action ends the game fo rone of the agents.

    :param agents: List[Agent]
        List of the agents involved in the step.
    :param game_state:
        Environment on which the step is proceed.
    :return: None
    """
    # Error cases
    if not game_state.is_game_over():
        # Stashing the current score
        old_scores = game_state.get_scores().copy()

        # Get action
        active_player_index = game_state.get_active_player()
        action = agents[active_player_index].act(game_state)

        # Triggering next step
        game_state.step(active_player_index, action)
        new_scores = game_state.get_scores()
        rewards = new_scores + old_scores

        # Is game over for all agents
        for player_index, agents in enumerate(agents):
            agents.observe(rewards[player_index], player_index, game_state.is_game_over())


def run_to_the_end(agents: List[Agent], game_state: Game) -> None:
    """Runs as many step as possible until the game state comes to an end.

    :param agents: List[Agent]
        List of the agents involved.
    :param game_state: GameState
        Environment concerned.

    :return: None
    """
    display_mode = agents[game_state.get_active_player_index()].get_display_mode()

    if display_mode == 2:
        game_state.init_pygame()
    while True:
        if display_mode == 1:  # Terminal display
            print(game_state)
        elif display_mode == 2:  # Graphical display
            game_state.display()
        run_step(agents, game_state)
        display_mode = agents[game_state.get_active_player()].get_display_mode()

        if game_state.is_game_over():
            if display_mode == 1:  # Terminal display
                print(game_state)
            elif display_mode == 2:  # Graphical display
                game_state.display()
            break


if __name__ == "__main__":
    try:
        game = sys.argv[2]
        number_of_player = int(sys.argv[3])

        if game == "Linq":
            game = Linq(player_number=number_of_player, maximum_number_of_round=2)
            agents_list = [RandomAgent(number_of_player) for i in range(number_of_player)]
            run_to_the_end(agents=agents_list, game_state=game)
        else:
            raise ValueError("Unknown game")


    except IndexError as ie:
        raise IndexError("Missing argument : game")
