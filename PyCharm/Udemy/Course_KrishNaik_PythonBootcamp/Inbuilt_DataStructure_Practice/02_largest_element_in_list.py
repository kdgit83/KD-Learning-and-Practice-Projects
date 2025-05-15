def find_largest(numbers: list[int]) -> int:
    """
    Find the Largest Element in a List
    Write a Python function that finds and returns the largest element in a given list of integers.

    Parameters:
    numbers (List of integers): The input list containing integers.

    Returns:
    An integer representing the largest element in the input list.

    Example:
    Input: numbers = [3, 8, 2, 10, 5]
    Output: 10
    Input: numbers = [-5, -10, -2, -1, -7]
    Output: -1
    """
    # Your code goes here
    if isinstance(numbers, list):
        largest = numbers[0]
        if not numbers:
            return None
        for num in numbers[1:]:
            if num > largest:
                largest = num
    else:
        largest = numbers
    return largest

num_list1 = [3, 8, 2, 10, 5]
num_list2 = [-5, -10, -2, -1, -7]
for num_list in [num_list1, num_list2]:
    print(find_largest(num_list))
