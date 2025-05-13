def rotate_list(lst: list[int], k: int) -> list[int]:
    """
    Rotate a List (Without Slicing)
    You are given a list of integers and an integer k. Write a Python function to rotate the list to the right by k
    positions without using slicing. A rotation shifts elements from the end of the list to the front.

    Parameters:
    lst (List of integers): The list to be rotated.
    k (Integer): The number of positions to rotate the list.

    Returns:
    A list of integers rotated by k positions.

    Example:
    Input: lst = [1, 2, 3, 4, 5], k = 2
    Output: [4, 5, 1, 2, 3]
    Input: lst = [10, 20, 30, 40, 50], k = 3
    Output: [30, 40, 50, 10, 20]
    """
    # Your code goes here
    # Handling the case where the list is empty
    if not lst:
        return []
    # Modulo to handle the case where k is greater than the length of the list
    k = k % len(lst)
    # Brute force approach using loops
    for _ in range(k):
        last_element = lst.pop()  # Remove the last element
        lst.insert(0, last_element)  # Insert it at the front
    return lst

s1_lst = [1, 2, 3, 4, 5]
s1_k = 2
s2_lst = [10, 20, 30, 40, 50]
s2_k = 3

s1 = [s1_lst, s1_k]
s2 = [s2_lst, s2_k]

for lst, k in [s1, s2]:
    print(rotate_list(lst, k))
