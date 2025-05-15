def merge_lists_to_dictionary(keys: list[str], values: list[int]) -> dict[str, int]:
    """
    Merge 2 List into Dictionary
    Merge Lists to Dictionary
    Design a Python function named merge_lists_to_dictionary to merge two lists into a dictionary where elements from
    the first list act as keys and elements from the second list act as values.

    Parameters:
    keys (List): A list of keys.
    values (List): A list of values.

    Returns:
    A dictionary containing merged key-value pairs.

    Example:
    Input: keys = ['a', 'b', 'c'], values = [1, 2, 3]
    Output: {'a': 1, 'b': 2, 'c': 3}
    Input: keys = ['x', 'y', 'z'], values = [10, 20, 30]
    Output: {'x': 10, 'y': 20, 'z': 30}
    """
    # Your code goes here
    final_dict = {}
    if len(keys) != len(values):
        return False
    for idx in range(len(keys)):
        final_dict[keys[idx]] = values[idx]
    return final_dict

s1_l1 = ['a', 'b', 'c']
s1_l2 = [1, 2, 3]
s2_l1 = ['x', 'y', 'z']
s2_l2 = [10, 20, 30]

s1 = [s1_l1, s1_l2]
s2 = [s2_l1, s2_l2]

for list1, list2 in [s1, s2]:
    print(merge_lists_to_dictionary(list1, list2))
