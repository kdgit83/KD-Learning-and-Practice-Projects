def reverse_list(lst: list[int]) -> list:
    """
    Reverse a List (Non-Slicing Approach)
    You are given a list of integers. Write a Python program that reverses the list without using slicing (lst[::-1]).
    The program should return the reversed list.

    Parameters:
    lst (List of integers): The list of integers to be reversed.

    Returns:
    A list of integers where the order of elements is reversed from the input list.

    Example:
    Input: lst = [1, 2, 3, 4, 5]
    Output: [5, 4, 3, 2, 1]
    """
    # Your code goes here
    rev_list = []
    for i in lst:
        rev_list.insert(0, i)
    return rev_list

num_list1 = [1, 2, 3, 4, 5]
num_list2 = [1, 2, 3, 3, 4, 5]
for num_list in [num_list1, num_list2]:
    print(reverse_list(num_list))
