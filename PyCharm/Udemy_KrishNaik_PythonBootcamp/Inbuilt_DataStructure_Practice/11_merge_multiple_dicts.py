def merge_three_dictionaries(dict1: dict, dict2: dict, dict3: dict) -> dict:
    """
    Merge Three Dictionaries
    Design a Python function named merge_three_dictionaries to merge exactly three dictionaries into one.

    Parameters:
    dict1 (Dictionary): The first dictionary to be merged.
    dict2 (Dictionary): The second dictionary to be merged.
    dict3 (Dictionary): The third dictionary to be merged.

    Returns:
    A single dictionary containing all key-value pairs from the three input dictionaries.

    Example:
    Input: ({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})
    Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
    Input: ({'x': 10, 'y': 20}, {'z': 30}, {'a': 40, 'b': 50})
    Output: {'x': 10, 'y': 20, 'z': 30, 'a': 40, 'b': 50}
    """
    # Your code goes here
    final_dict = {}
    input_dicts = [dict1, dict2, dict3]
    for dict_item in input_dicts:
        for key, value in dict_item.items():
            if key not in final_dict:
                final_dict[key] = value
    return final_dict

s1_d1 = {'a': 1, 'b': 2}
s1_d2 = {'c': 3, 'd': 4}
s1_d3 = {'e': 5, 'f': 6}
s2_d1 = {'x': 10, 'y': 20}
s2_d2 = {'z': 30}
s2_d3 = {'a': 40, 'b': 50}

s1 = [s1_d1, s1_d2, s1_d3]
s2 = [s2_d1, s2_d2, s2_d3]

for dict1, dict2, dict3 in [s1, s2]:
    print(merge_three_dictionaries(dict1, dict2, dict3))
