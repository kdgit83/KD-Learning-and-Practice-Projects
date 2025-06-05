def find_missing_number(nums):
    """
    Function to find the missing number in the array.
    :param nums: List[int] -> A list of distinct integers in the range [0, n]
    :return: int -> The missing number in the range

    Description:
    Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is
    missing from the array.

    Input Parameters:
    nums (List[int]): A list of integers where each integer is unique and in the range [0, n].

    Output:
    int: The missing number in the range [0, n].

    Example:
    Input: nums = [3, 0, 1]
    Output: 2

    Input: nums = [0, 1]
    Output: 2

    Input: nums = [8, 7, 6, 4, 3, 2, 0, 1]
    Output: 5
    """
    n = len(nums)
    # Calculate the expected sum of numbers from 0 to n
    expected_sum = n * (n + 1) // 2
    # Calculate the actual sum of the given numbers
    actual_sum = sum(nums)

    # The missing number is the difference between the expected sum and the actual sum
    return expected_sum - actual_sum

nums_1 = [3, 0, 1]
nums_2 = [0, 1]
nums_3 = [8, 7, 6, 4, 3, 2, 0, 1]
nums = [nums_1, nums_2, nums_3]

for num in nums:
    print(find_missing_number(num))
