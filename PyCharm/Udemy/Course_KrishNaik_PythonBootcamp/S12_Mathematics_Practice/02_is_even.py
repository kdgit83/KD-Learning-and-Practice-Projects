def is_even(n: int) -> bool:
    """
    Function to check if a number is even.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if n is even, False otherwise.
    """
    # Your code here
    return n % 2 == 0

for i in [4, 7, 86]:
    print(is_even(i))
