def sum_of_elements(lst: list[int]) -> int:
    """
    Function to find the sum of all elements in the list.
    :param lst: List[int] -> List of integers
    :return: int -> The sum of all elements in the list
    """
    # Initialize sum variable
    total_sum = 0

    # Traverse the list and compute the sum
    for num in lst:
        total_sum += num

    return total_sum


# Helper function to display the result (for debugging)
def display_result(lst):
    print(sum_of_elements(lst))

lst = [1, 2, 3, 4, 5]
display_result(lst)  # Output should be 15
