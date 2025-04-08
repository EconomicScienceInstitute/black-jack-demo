"""Test suite for blackjack_slow implementation"""
from blackjack_slow import hit, reward, obs, bellman_equation, step, prob_winning

import pytest

@pytest.mark.parametrize("card, expected_player, expected_is_hard", [
    (2, 19, False),
    (10, 17, True),
    (5, 12, True),
    (11, 18, False),  # Ace case
    (10, 27, True),   # Bust case
])
def test_hit(card, expected_player, expected_is_hard):
    current_obs = obs(player=17, dealer_face=4, is_hard=False)
    next_obs = hit(current_obs, card)
    assert next_obs.player == expected_player
    assert next_obs.dealer_face == 4
    assert next_obs.is_hard == expected_is_hard

@pytest.mark.parametrize("current_obs, action, expected_reward", [
    (obs(player=17, dealer_face=4, is_hard=True), 1, 0),  # Hit action
    (obs(player=22, dealer_face=4, is_hard=True), 0, -1), # Bust case
    (obs(player=21, dealer_face=4, is_hard=True), 0, 1),  # Blackjack
    (obs(player=17, dealer_face=4, is_hard=True), 0, 0),  # Normal stay
])
def test_reward(current_obs, action, expected_reward):
    assert reward(current_obs, action) == expected_reward

def test_step():
    current_obs = obs(player=17, dealer_face=4, is_hard=True)
    
    # Test stay action
    stay_results = list(step(current_obs, 0))
    assert len(stay_results) == 1
    assert stay_results[0][0] == current_obs
    assert stay_results[0][1] == 1.0
    
    # Test hit action
    hit_results = list(step(current_obs, 1))
    assert len(hit_results) == 10  # Cards 2-11
    total_prob = sum(prob for _, prob in hit_results)
    assert abs(total_prob - 1.0) < 1e-6  # Probabilities should sum to 1

@pytest.mark.parametrize("current_obs, expected_prob", [
    (obs(player=17, dealer_face=4, is_hard=True), 1),  # Placeholder value
    (obs(player=21, dealer_face=4, is_hard=True), 1),  # Blackjack
    (obs(player=22, dealer_face=4, is_hard=True), 0),  # Bust
])
def test_prob_winning(current_obs, expected_prob):
    assert prob_winning(current_obs) == expected_prob

@pytest.mark.parametrize("start_obs, expected_value, expected_action", [
    (obs(player=21, dealer_face=4, is_hard=True), 1, 0),  # Blackjack - should stay
    (obs(player=17, dealer_face=4, is_hard=True), 0, 0),  # Normal case
    (obs(player=22, dealer_face=4, is_hard=True), -1, 0), # Bust case
])
def test_bellman_equation(start_obs, expected_value, expected_action):
    optimal_value, optimal_action = bellman_equation(start_obs)
    assert optimal_value == expected_value
    assert optimal_action == expected_action
