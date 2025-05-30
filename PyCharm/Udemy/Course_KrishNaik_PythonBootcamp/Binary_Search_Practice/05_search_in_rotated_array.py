def search(nums, target):
    """
    Search for a target value in a rotated sorted array using binary search.

    Description:
    Given a sorted array that has been rotated, find the index of a given target value. The array was originally sorted
    in ascending order and then rotated at some pivot.

    Parameters:
    nums (List[int]): A list of integers sorted in ascending order but rotated at an unknown pivot.
    target (int): The integer value to search for in the array.

    Return Values:
    int: The index of the target value in the array, or -1 if the target is not in the array.

    Example:
    Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
    Output: 4
    Explanation: The target value 0 is at index 4 in the rotated array.

    Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
    Output: -1
    Explanation: The target value 3 is not present in the array.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Determine which side is sorted
        if nums[left] <= nums[mid]:
            # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
print(search(nums, target))
