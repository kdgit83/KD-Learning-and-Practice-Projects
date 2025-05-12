def check_unique(lst: list[int]) -> bool:
    """
    Check if All Elements in a List are Unique
    You are given a list of integers. Write a Python program that checks if all elements in the list are unique.
    If all elements are unique, return True; otherwise, return False.

    Parameters:
    lst (List of integers): The list of integers to check for uniqueness.

    Returns:
    A boolean value True if all elements in the list are unique, False otherwise.

    Example:
    Input: lst = [1, 2, 3, 4, 5]
    Output: True
    Input: lst = [1, 2, 3, 3, 4, 5]
    Output: False
    """
    # Your code goes here
    is_unique = True
    for item in lst:
        if lst.count(item) > 1:
            is_unique = False
    return is_unique

num_list1 = [1, 2, 3, 4, 5]
num_list2 = [1, 2, 3, 3, 4, 5]
for num_list in [num_list1, num_list2]:
    print(check_unique(num_list))
