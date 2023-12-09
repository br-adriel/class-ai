def smallest_opponent_win_options(values, oponent_symbol = 'x'):
    smallest_opponent_win = float('inf')
    smallest_opponent_win_keys = []

    for key, values in values.items():
        opponent_wins = values[oponent_symbol]
        if opponent_wins == smallest_opponent_win:
            smallest_opponent_win = opponent_wins
            smallest_opponent_win_keys.append(key)
        elif opponent_wins > smallest_opponent_win:
            smallest_opponent_win = opponent_wins
            smallest_opponent_win_keys = [key]

    return smallest_opponent_win_keys

def highest_win_options(values, lookup_keys, player_symbol = 'o'):
    highest_win = -1
    highest_win_keys = []

    for key in lookup_keys:
        wins = values[key][player_symbol]
        if wins == highest_win:
            highest_win = wins
            highest_win_keys.append(key)
        elif wins > highest_win:
            highest_win = wins
            highest_win_keys = [key]

    return highest_win_keys

def highest_tie_options(values, lookup_keys):
    highest_tie = -1
    highest_tie_keys = []

    for key in lookup_keys:
        ties = values[key]['?']
        if ties == highest_tie:
            highest_tie = ties
            highest_tie_keys.append(key)
        elif ties > highest_tie:
            highest_tie = ties
            highest_tie_keys = [key]

    return highest_tie_keys

