def linear_search(arr: list, target: int) -> int:
    """
    Title: Linear Search in a List
    Description: Implement a function linear_search that performs a linear search on a list to find a given value. The
    function should return the index of the first occurrence of the value in the list, or -1 if the value is not found.

    Parameters:
    arr: A list of elements (can be empty)
    target: The value to search for in the list

    Return:
    The index of the first occurrence of the target value (0-based), or -1 if not found

    Examples:
    linear_search([3, 7, 2, 5], 2) should return 2
    linear_search([1, 1, 2, 1], 1) should return 0
    linear_search([], 5) should return -1
    linear_search([4, 2, 8], 6) should return -1
    """
    # TODO: Implement this function
    for index, char in enumerate(arr):
        if char == target:
            return index
    return -1

print(linear_search([3, 7, 2, 5], 2))
print(linear_search([1, 1, 2, 1], 1))
print(linear_search([], 5))
print(linear_search([4, 2, 8], 6))
