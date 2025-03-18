from collections import namedtuple
import numpy as np

hand = namedtuple('hand', ['has_ace', 'value'])

def get_index(hand):
    if hand.value > 21:
        return 42
    if not hand.has_ace:
        return hand.value
    else:
        return hand.value + 22

# define  probabilities for a dealer's ending value.

# each index in the transition matrix maps to a hand.
# the value at each index is the probability of transitioning to the next hand.
# transition_matrix[i,j] is the probability of transitioning from hand i to hand j.
transition_matrix = np.zeros((43, 43))

for val in range(0,21):
    for has_ace in [True, False]:
        index = get_index(hand(has_ace, val))
        # update the values in transition matrix from one hand to another hand.
        
        # the probability of getting any card value from 2-9 is 1/13
        # TODO handle the case for number cards

        # probability of getting a card valued at 10 is 4/13
        # TODO handle the case for 10s

        # probability of getting an ace is 1/13
        # TODO handle the case for aces
        
        # if we have an ace, we can choose to treat it as a 1 or an 11.

        # if we bust then we assign the probability to the 42nd index.

        # if we don't bust, then we assign the probability to the index of the new hand value.

        # we do this for all possible starting hands.
        
        