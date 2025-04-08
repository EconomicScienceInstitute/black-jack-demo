from collections import namedtuple
from typing import Generator

obs = namedtuple('obs', ['player', 'dealer_face', 'is_hard'])

def hit(current_obs: obs, card: int) -> obs:
    new_player = current_obs.player + card
    if new_player < 21:
        if card == 11:
            new_is_hard = False
        else:
            new_is_hard = current_obs.is_hard
    elif not current_obs.is_hard: # if we have an ace, we can count it as 1 when we bust
        new_player = new_player - 10
        new_is_hard = True
    else:
        new_is_hard = current_obs.is_hard
    return obs(player=new_player, dealer_face=current_obs.dealer_face, is_hard=new_is_hard)

def step(current_obs: obs, action: int) -> Generator[tuple[obs, float], None, None]:
    """_summary_

    Args:
        current_obs (obs): _description_
        action (int): _description_

    Returns:
        tuple[obs, float]: _description_
    """
    if action == 0: # stay
        yield current_obs, 1
    else: # hit 
        for card in range(2,12):
            prob = 1/13 if card != 10 else 4/13
            next_obs = hit(current_obs, card)
            yield next_obs, prob

def prob_winning(current_obs: obs) -> float:
    """Returns the probability of winning the game given the current state. 
    Which includes the player's hand value and the dealer's face up card

    Args:
        current_obs (obs): 

    Returns:
        float: probability of winning the game
    """
    player_value = current_obs.player
    dealer_face = current_obs.dealer_face
    # todo lookup the probability of winning given the player's hand value and the dealer's face up card
    return 1

def reward(current_obs: obs, action: int) -> float:
    if action == 1: # hit
        return 0
    else: # stay
        if current_obs.player > 21:
            return -1
        elif current_obs.player == 21:
            return 1
        else: # check against dealer
            return 0

cache = {}
def bellman_equation(start_obs: obs) -> [float, int]:
    """_summary_

    Args:
        start_obs (obs): _description_
    """
    max_value = -float('inf')
    optimal_action = None
    if start_obs in cache:
        return cache[start_obs]
    for action in [0, 1]:
        curr_value = 0
        for next_obs, prob in step(start_obs, action):
            curr_value += prob * reward(next_obs, action) + prob * bellman_equation(next_obs)[0]
        if curr_value > max_value:
            max_value = curr_value
            optimal_action = action
    cache[start_obs] = max_value, optimal_action
    return max_value, optimal_action

