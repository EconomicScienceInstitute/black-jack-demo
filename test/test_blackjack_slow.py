from blackjack_slow import hit, reward, obs

import pytest

@pytest.mark.parametrize("card, expected_player, expected_is_hard", [
    (2, 19, False),
    (10, 17, True),
    (5, 12, True),
])
def test_step(card, expected_player, expected_is_hard):
    current_obs = obs(player=17, dealer=4, is_hard=False)
    next_obs = hit(current_obs, card)
    assert next_obs.player == expected_player
    assert next_obs.dealer == 4
    assert next_obs.is_hard == expected_is_hard
    

def test_reward():
    current_obs = obs(player=17, dealer=4, is_hard=True)
    assert reward(current_obs) == 0
    