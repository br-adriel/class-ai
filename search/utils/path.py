from typing import Union

def path_dict_to_list(path: dict[str, Union[int, None]]) -> list[int]:
    """
    Converts a path dictionary into a list of integers.
    """
    list_path = []
    list_path.append(list(path.keys())[-1])


    next_key = path.get(list_path[-1])
    while not next_key == list_path[-1]:
        list_path.append(next_key)
        next_key = path.get(list_path[-1])
    list_path = [int(i) for i in list_path]
    return list_path
