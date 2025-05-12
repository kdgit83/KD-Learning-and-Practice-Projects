def sum_list(numbers: list[int]) -> int:
    """
    Sum of List Elements
    Write a Python function that calculates the sum of all elements in a given list of integers.

    Parameters:
    numbers (List of integers): The input list containing integers.

    Returns:
    An integer representing the sum of all elements in the input list.

    Example:
    Input: numbers = [1, 2, 3, 4, 5]
    Output: 15
    Input: numbers = [10, -5, 7, 8, -2]
    Output: 18
    """
    # Your code goes here
    result = 0
    if isinstance(numbers, list):
        for num in numbers:
            result += num
    else:
        result = numbers
    return result

num_list1 = [1, 2, 3, 4, 5]
num_list2 = [10, -5, 7, 8, -2]
for num_list in [num_list1, num_list2]:
    print(sum_list(num_list))
