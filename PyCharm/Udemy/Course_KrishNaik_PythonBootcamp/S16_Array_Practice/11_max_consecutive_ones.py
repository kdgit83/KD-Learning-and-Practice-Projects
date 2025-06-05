def find_max_consecutive_ones(nums):
    """
    Function to find the maximum number of consecutive 1's in a binary array.
    :param nums: List[int] -> A binary array where each element is either 0 or 1
    :return: int -> The maximum number of consecutive 1's

    Description:
    Given a binary array nums, return the maximum number of consecutive 1s in the array.

    Input Parameters:
    nums (List[int]): A binary array where each element is either 0 or 1.

    Output:
    int: The maximum number of consecutive 1s in the array.

    Example:
    Input: nums = [0, 0, 0, 0]
    Output: 0

    Input: nums = [1, 0, 1, 1, 0, 1, 1, 1, 1]
    Output: 4

    Input: nums = [1, 1, 0, 1, 1, 1]
    Output: 3
    """
    max_count = 0
    current_count = 0

    for num in nums:
        if num == 1:
            # Increment count of consecutive 1's
            current_count += 1
        else:
            # Update max_count if needed and reset current_count
            max_count = max(max_count, current_count)
            current_count = 0

    # Final check to update max_count after the loop
    return max(max_count, current_count)

nums = [1, 0, 1, 1, 0, 1, 1, 1, 1]
print(find_max_consecutive_ones(nums))
