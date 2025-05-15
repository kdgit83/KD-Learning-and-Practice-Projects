def merge_two_sorted_lists(list1: list[int], list2: list[int]) -> list[int]:
    """
    Merge Two Sorted Lists
    You are given two sorted lists of integers. Write a Python function to merge these two sorted lists into one sorted
    list. The resulting list should also be in non-decreasing order.

    Parameters:
    list1 (List of integers): The first sorted list.
    list2 (List of integers): The second sorted list.

    Returns:
    A single list of integers, containing all elements from list1 and list2, sorted in non-decreasing order.

    Example:
    Input: list1 = [1, 3, 5], list2 = [2, 4, 6]
    Output: [1, 2, 3, 4, 5, 6]
    Input: list1 = [1, 4, 7], list2 = [2, 3, 5, 8]
    Output: [1, 2, 3, 4, 5, 7, 8]
    """
    # Your code goes here
    merged_list = [*list1, *list2]
    return sorted(merged_list)

s1_l1 = [1, 3, 5]
s1_l2 = [2, 4, 6]
s2_l1 = [1, 4, 7]
s2_l2 = [2, 3, 5, 8]

s1 = [s1_l1, s1_l2]
s2 = [s2_l1, s2_l2]

for list1, list2 in [s1, s2]:
    print(merge_two_sorted_lists(list1, list2))
