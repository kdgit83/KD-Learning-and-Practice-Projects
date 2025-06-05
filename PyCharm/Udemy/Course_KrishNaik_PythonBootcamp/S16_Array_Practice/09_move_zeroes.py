def move_zeroes(nums):
    """
    Function to move all 0's to the end of the array while maintaining the order of non-zero elements.
    :param nums: List[int] -> A list of integers
    :return: None -> The list is modified in place
    Description:
    Given an integer array nums, write a function to move all 0s to the end of the array while maintaining the relative
    order of the non-zero elements.

    Input Parameters:
    nums (List[int]): A list of integers.

    Output:
    The list nums with all 0s moved to the end, preserving the order of non-zero elements.

    Example:
    Input: nums = [0, 1, 0, 3, 12]
    Output: [1, 3, 12, 0, 0]

    Input: nums = [0, 0, 1]
    Output: [1, 0, 0]

    Input: nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
    Output: [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]
    """
    non_zero_index = 0  # Pointer to track the position of the next non-zero element

    # Move non-zero elements to the front of the list
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index] = nums[i]
            non_zero_index += 1

    # Fill the remaining positions with zeros
    while non_zero_index < len(nums):
        nums[non_zero_index] = 0
        non_zero_index += 1

    return nums

nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
print(move_zeroes(nums))
