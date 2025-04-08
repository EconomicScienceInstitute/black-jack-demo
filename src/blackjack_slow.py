from collections import namedtuple

obs = namedtuple('obs', ['player', 'dealer', 'is_hard'])

def hit(current_obs, card):
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
    return obs(player=new_player, dealer=current_obs.dealer, is_hard=new_is_hard)


def reward(current_obs):
    return 0
