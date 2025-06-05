def is_sorted(arr):
    """
    Function to check if the given array is sorted in non-decreasing order.
    :param arr: List[int] -> A list of integers
    :return: bool -> True if the array is sorted, False otherwise

    Description:
    Write a function that checks whether the given array is sorted in non-decreasing order. The array is considered
    sorted if every element is less than or equal to the next element.

    Input Parameters:
    arr (List[int]): A list of integers.

    Output:
    bool: True if the array is sorted in non-decreasing order, False otherwise.

    Example:
    Input: arr = [5, 4, 3, 2, 1]
    Output: False

    Input: arr = [1, 3, 2, 4, 5]
    Output: False

    Input: arr = [1, 2, 3, 4, 5]
    Output: True
    """
    n = len(arr)

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False

    return True

arr_1 = [5, 4, 3, 2, 1]
arr_2 = [1, 3, 2, 4, 5]
arr_3 = [1, 2, 3, 4, 5]
arrs = [arr_1, arr_2, arr_3]
for arr in arrs:
    print(is_sorted(arr))
