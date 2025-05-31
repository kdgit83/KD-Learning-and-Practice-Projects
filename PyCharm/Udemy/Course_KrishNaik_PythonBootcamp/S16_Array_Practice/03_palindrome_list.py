def is_palindrome(lst):
    """
    Function to check if a list is a palindrome.
    :param lst: List[int] -> List of integers
    :return: bool -> True if the list is a palindrome, False otherwise
    """
    # Initialize two pointers
    left = 0
    right = len(lst) - 1

    # Compare elements from the start and end of the list
    while left < right:
        if lst[left] != lst[right]:
            return False
        left += 1
        right -= 1

    return True

# Helper function to display the result (for debugging)
def display_result(lst):
    print(is_palindrome(lst))

lst = [1, 2, 3, 2, 1]
display_result(lst)  # Output should be True
