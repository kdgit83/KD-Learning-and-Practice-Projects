def merge_dicts_with_overlapping_keys(dicts: list[dict]) -> dict:
    """
    Merge Dictionaries with Common Keys
    Problem Description

    Merge Dictionaries with Overlapping Keys
    Design a Python function named merge_dicts_with_overlapping_keys that merges multiple dictionaries into a single
    dictionary. If a key appears in more than one dictionary, sum up their values.

    Parameters:
    dicts (list): A list of dictionaries where keys might overlap.

    Returns:
    A single dictionary where values for overlapping keys are summed.

    Example:
    Input: [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]
    Output: {'a': 1, 'b': 5, 'c': 9, 'd': 6}
    Input: [{'x': 10, 'y': 20}, {'y': 30, 'z': 40}, {'z': 50, 'x': 60}]
    Output: {'x': 70, 'y': 50, 'z': 90}
    """
    # Your code goes here
    out_dict = {}
    for dict_item in dicts:
        for key, value in dict_item.items():
            out_dict[key] = out_dict.get(key, 0) + value
    return out_dict

s1_d1 = {'a': 1, 'b': 2}
s1_d2 = {'b': 3, 'c': 4}
s1_d3 = {'c': 5, 'd': 6}
s2_d1 = {'x': 10, 'y': 20}
s2_d2 = {'y': 30, 'z': 40}
s2_d3 = {'z': 50, 'x': 60}

s1 = [s1_d1, s1_d2, s1_d3]
s2 = [s2_d1, s2_d2, s2_d3]

for s_dict in [s1, s2]:
    print(merge_dicts_with_overlapping_keys(s_dict))
