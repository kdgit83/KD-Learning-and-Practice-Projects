def remove_duplicates(lst: list[int]) -> list[int]:
    """
    Remove Duplicates from a List
    You are given a list of integers. Write a Python program that removes any duplicate elements from the list and
    returns a new list with only unique elements. The order of elements in the list should be maintained.

    Parameters:
    lst (List of integers): The list of integers from which duplicates should be removed.

    Returns:
    A list of integers where all duplicates have been removed, preserving the original order.

    Example:
    Input: lst = [1, 2, 2, 3, 4, 4, 5]
    Output: [1, 2, 3, 4, 5]
    Input: lst = [4, 5, 5, 4, 6, 7]
    Output: [4, 5, 6, 7]
    """
    # Your code goes here
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

num_list1 = [1, 2, 2, 3, 4, 4, 5]
num_list2 = [4, 5, 5, 4, 6, 7]
for num_list in [num_list1, num_list2]:
    print(remove_duplicates(num_list))
