def intersection(nums1, nums2):
    """
    Function to find the intersection of two integer arrays.
    :param nums1: List[int] -> First array of integers
    :param nums2: List[int] -> Second array of integers
    :return: List[int] -> An array of unique integers present in both arrays

    Description:
    Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be
    unique, and you may return the result in any order.

    Input Parameters:
    nums1 (List[int]): An array of integers.
    nums2 (List[int]): An array of integers.

    Output:
    List[int]: An array of unique integers that are present in both nums1 and nums2.

    Example:
    Input: nums1 = [1, 2, 3], nums2 = [4, 5, 6]
    Output: []

    Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
    Output: [2]

    Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
    Output: [9, 4]
    """
    # Convert nums1 to a set to achieve O(1) average time complexity for lookups
    set1 = set(nums1)

    # Use a set to store the intersection
    intersection_set = set()

    # Traverse nums2 and check if the element is in set1
    for num in nums2:
        if num in set1:
            intersection_set.add(num)

    # Convert the set to a list and return it
    return list(intersection_set)

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersection(nums1, nums2))
