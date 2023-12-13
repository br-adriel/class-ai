def smallest_opponent_win_options(values: list[str],
                                  oponent_symbol: str = 'x') -> list[str]:
    smallest_opponent_win: float = float('inf')
    smallest_opponent_win_keys: list[str] = []

    for key, values in values.items():
        opponent_wins = values[oponent_symbol]
        if opponent_wins == smallest_opponent_win:
            smallest_opponent_win = opponent_wins
            smallest_opponent_win_keys.append(key)
        elif opponent_wins < smallest_opponent_win:
            smallest_opponent_win = opponent_wins
            smallest_opponent_win_keys = [key]

    return smallest_opponent_win_keys


def highest_win_options(values: list[str],
                        lookup_keys: list[str],
                        player_symbol: str = 'o') -> list[str]:
    """Returns a list which contains the best keys for a win in the game"""

    highest_win: int = -1
    highest_win_keys: list[str] = []

    for key in lookup_keys:
        wins = values[key][player_symbol]
        if wins == highest_win:
            highest_win = wins
            highest_win_keys.append(key)
        elif wins > highest_win:
            highest_win = wins
            highest_win_keys = [key]

    return highest_win_keys


def highest_tie_options(values: list[str], lookup_keys: list[str]) -> list[str]:
    """Returns a list which contains the best keys for a tie in the game"""
    highest_tie: int = -1
    highest_tie_keys: list[str] = []

    for key in lookup_keys:
        ties = values[key]['?']
        if ties == highest_tie:
            highest_tie = ties
            highest_tie_keys.append(key)
        elif ties > highest_tie:
            highest_tie = ties
            highest_tie_keys = [key]

    return highest_tie_keys


def choose_next_position(values: list[str], player_symbol: str = 'o') -> str:
    """Chooses the next position based on loss/win/draw count for each position"""
    smallest_opponent_chances = smallest_opponent_win_options(
        values,
        'o' if player_symbol == 'x' else 'x'
    )
    highest_win_chances = highest_win_options(
        values,
        smallest_opponent_chances,
        player_symbol
    )
    preferabole_options = highest_tie_options(values, highest_win_chances)
    return preferabole_options[0]
