from math import sqrt


def is_perfect_square(num):
    """
    Function to check if a number is a perfect square.

    Parameters:
    num (int): The number to check.

    Returns:
    bool: True if num is a perfect square, False otherwise.
    """
    # Your code here
    if num < 1:
        return False
    return int(str(sqrt(num)).split('.')[1]) == 0

for i in [16, 24, 121]:
    print(is_perfect_square(i))
