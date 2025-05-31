def find_max_element(lst: list[int]) -> int:
    """
    Function to find the maximum element in a list.
    :param lst: List[int] -> List of integers
    :return: int -> The maximum element in the list
    """
    # Initialize the maximum element as the first element of the list
    max_element = lst[0]

    # Traverse the list to find the maximum element
    for num in lst:
        if num > max_element:
            max_element = num

    return max_element


# Helper function to display the result (for debugging)
def display_result(lst):
    print(find_max_element(lst))

lst = [3, 5, 2, 9, 6]
display_result(lst)  # Output should be 9
