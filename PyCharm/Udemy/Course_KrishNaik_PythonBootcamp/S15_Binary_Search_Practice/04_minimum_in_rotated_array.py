def find_min(nums):
    """
    Find the minimum element in a rotated sorted array using binary search.

    Description:
    Given a sorted array that has been rotated, find the minimum element in the array. The array was originally sorted
    in ascending order and then rotated at some pivot.

    Parameters:
    nums (List[int]): A list of integers sorted in ascending order but rotated at an unknown pivot.
    Return Values:
    int: The minimum element in the rotated sorted array.

    Example:
    Input: nums = [4, 5, 6, 7, 0, 1, 2]
    Output: 0
    Explanation: The minimum element is 0.

    Input: nums = [11, 13, 15, 17]
    Output: 11
    Explanation: The array was not rotated, and the minimum element is the first element.
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # Compare middle element with the rightmost element
        if nums[mid] > nums[right]:
            # The minimum element is in the right half
            left = mid + 1
        else:
            # The minimum element is in the left half (including mid)
            right = mid

    # At the end of the loop, left == right and pointing to the minimum element
    return nums[left]

nums = [11, 13, 15, 17]
print(find_min(nums))
