def path_dict_to_list(path: dict[str, int | None]) -> list[int]:
    """
    Converts a path dictionary into a list of integers.

    Args:
        path (dict[str, int | None]): A dictionary where keys are strings and
        values are integers or None.

    Returns:
        list[int]: A list of integers representing a path extracted from the
        dictionary.
    """
    list_path = []
    list_path.append(list(path.keys())[-1])


    next_key = path.get(list_path[-1])
    while not next_key == list_path[-1]:
        list_path.append(next_key)
        next_key = path.get(list_path[-1])
    list_path = [int(i) for i in list_path]
    return list_path
