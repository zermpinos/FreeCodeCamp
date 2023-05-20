"""
the given code is a Rock-Paper-Scissors player that tries to predict the opponent's next move based on their history
and uses various strategies to counter it. it uses four main strategies named Quincy, Abbey, Kris, and Mrugesh.
the code also maintains a play order dictionary to keep track of the frequency of the opponent's moves.

global variables:
my_history: A list to store the history of our plays.
prev_play: A string to store the previous play.
opponent_list: A list of boolean values to keep track of which strategy the opponent is using.
ideal_response: A dictionary to store the ideal response to each move.
opponent_quincy_counter: A counter for the Quincy strategy.
play_order: A dictionary to store the frequency of opponent's moves for the Abbey strategy.
player(prev_opponent_play, opponent_history=[]) function:
Takes the previous opponent's play and the history of the opponent as input arguments.
appends the previous opponent's play and our previous play to their respective histories.
check for the Quincy strategy by looking for a specific pattern of moves in the opponent's history.
if the Quincy strategy is detected, it returns the corresponding move and resets the opponent_list
and opponent_history after 1000 plays.
check for the Abbey strategy by looking for another specific pattern of moves in the opponent's history.
if the Abbey strategy is detected, it calculates the most frequent move in the last two plays
and returns the ideal response. it also resets the opponent_list, opponent_history, and play_order after 1000 plays.
check for the Kris strategy by looking for yet another specific pattern of moves in the opponent's history.
if the Kris strategy is detected, it returns the ideal response to the previous play and resets the opponent_list
and opponent_history after 1000 plays.
check for the Mrugesh strategy by looking for a pattern of the same move repeated in the opponent's history.
if the Mrugesh strategy is detected, it calculates the most frequent move in the last ten plays
and returns the ideal response. it also resets the opponent_list and opponent_history after 1000 plays.
if none of the strategies are detected, it returns the default play 'S'.
"""

# Initialize global variables
my_history = []
prev_play = 'S'
opponent_list = [False] * 4
ideal_response = {'P': 'R', 'R': 'S', 'S': 'P'}
opponent_quincy_counter = -1
play_order = {"RR": 0, "RP": 0, "RS": 0, "PR": 0, "PP": 0, "PS": 0, "SR": 0, "SP": 0, "SS": 0}


def player(prev_opponent_play, opponent_history=[]):
    global my_history, prev_play, opponent_list, ideal_response, opponent_quincy_counter, play_order

    # Update histories
    opponent_history.append(prev_opponent_play)
    my_history.append(prev_play)

    # Check for Quincy strategy
    if len(set(opponent_list)) == 1 and opponent_history[-5:] == ['R', 'P', 'P', 'S', 'R']:
        opponent_list[0] = True

    # Reset opponent_list and opponent_history after 1000 plays
    if opponent_list[0]:
        if len(opponent_history) % 1000 == 0:
            opponent_list = [False] * 4
            opponent_history.clear()

        # Quincy's strategy moves
        opponent_quincy_list = ['P', 'S', 'S', 'R', 'P']
        opponent_quincy_counter = (opponent_quincy_counter + 1) % 5
        return opponent_quincy_list[opponent_quincy_counter]

    # Check for Abbey strategy
    if len(set(opponent_list)) == 1 and opponent_history[-5:] == ['P', 'P', 'R', 'R', 'R']:
        opponent_list[1] = True

    # Update play_order
    if opponent_list[1]:
        last_two = ''.join(my_history[-2:])
        if len(last_two) == 2:
            play_order[last_two] += 1

        # Determine the most frequent move in the last two plays
        potential_plays = [prev_play + 'R', prev_play + 'P', prev_play + 'S']
        sub_order = {k: play_order[k] for k in potential_plays if k in play_order}
        prediction = max(sub_order, key=sub_order.get)[-1:]

        # Reset opponent_list, opponent_history, and play_order after 1000 plays
        if len(opponent_history) % 1000 == 0:
            opponent_list = [False] * 4
            opponent_history.clear()
            play_order = {"RR": 0, "RP": 0, "RS": 0, "PR": 0, "PP": 0, "PS": 0, "SR": 0, "SP": 0, "SS": 0}

        prev_play = ideal_response[prediction]
        return prev_play

    # Check for Kris strategy
    if len(set(opponent_list)) == 1 and opponent_history[-5:] == ['P', 'R', 'R', 'R', 'R']:
        opponent_list[2] = True

    if opponent_list[2]:
        # Reset opponent_list and opponent_history after 1000 plays
        if len(opponent_history) % 1000 == 0:
            opponent_list = [False] * 4
            opponent_history.clear()

        prev_play = ideal_response[prev_play]
        return prev_play

    # Check for Mrugesh strategy
    if len(set(opponent_list)) == 1 and opponent_history[-5:] == ['R', 'R', 'R', 'R', 'R']:
        opponent_list[3] = True

    if opponent_list[3]:
        # Reset opponent_list and opponent_history after 1000 plays
        if len(opponent_history) == 1000:
            opponent_list = [False] * 4
            opponent_history.clear()

        # Determine the most frequent move in the last ten plays
        last_ten = my_history[-10:]
        most_frequent = max(set(last_ten), key=last_ten.count)
        prev_play = ideal_response[most_frequent]
        return prev_play

    prev_play = 'S'
    return prev_play
