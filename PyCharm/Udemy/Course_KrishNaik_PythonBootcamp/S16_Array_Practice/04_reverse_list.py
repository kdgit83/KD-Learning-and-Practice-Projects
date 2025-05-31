def reverse_list(lst):
    """
    Function to reverse the order of elements in a list.
    :param lst: List[int] -> List of integers
    :return: List[int] -> The list with elements in reversed order
    """
    left = 0
    right = len(lst) - 1

    # Swap elements from start and end moving towards the center
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1

    return lst

# Helper function to display the result (for debugging)
def display_result(lst):
    print(reverse_list(lst))

lst = [1, 2, 3, 4, 5]
display_result(lst)  # Output should be [5, 4, 3, 2, 1]
