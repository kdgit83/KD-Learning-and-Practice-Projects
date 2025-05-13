def is_subset(lst1: list[int], lst2: list[int]) -> bool:
    """
    Check if List is Subset of another List
    Check if a List is a Subset of Another List (Brute Force Approach)
    You are given two lists of integers. Write a Python program that checks whether the first list is a subset of the
    second list using a brute-force approach, without using the in keyword. A list is considered a subset if all
    elements of the first list are present in the second list.

    Parameters:
    lst1 (List of integers): The first list, which is being checked as a subset.
    lst2 (List of integers): The second list, which is the list to compare against.

    Returns:
    A boolean value True if lst1 is a subset of lst2, otherwise False.

    Example:
    Input: lst1 = [1, 2, 3], lst2 = [1, 2, 3, 4, 5]
    Output: True
    All elements in lst1 are present in lst2.

    Input: lst1 = [1, 6], lst2 = [1, 2, 3, 4, 5]
    Output: False
    The element 6 is not present in lst2.
    """
    # Your code goes here
    n, m = len(lst1), len(lst2)
    for i in range(m - n + 1):
        if lst2[i:i + n] == lst1:
            return True
    return False

list1 = [2, 3, 5]
list2 = [1, 5, 8, 2, 3, 6]
print(is_subset(list1, list2))
