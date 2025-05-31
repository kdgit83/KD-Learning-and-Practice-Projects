def generate_inverted_pyramid(n: int) -> list[str]:
    """
    Function to return an inverted pyramid pattern of '*' of side n as a list of strings.

    Parameters:
    n (int): The number of rows in the inverted pyramid.

    Returns:
    list: A list of strings where each string represents a row of the inverted pyramid.

    Problem Description
    You are given an integer n. Your task is to return an inverted pyramid pattern of '*', where each side has n rows,
    represented as a list of strings. The first row has 2n - 1 stars, the second row has 2n - 3 stars, and so on, until
    the last row has 1 star, with each row centered using spaces.

    Example:
    Input: 3
    Output: ['*****', ' *** ', '  *  ']

    Input: 5
    Output: ['*********', ' ******* ', '  *****  ', '   ***   ', '    *    ']
    """
    # Your code here
    pyramid = []
    # Loop through each row from 1 to n
    for i in range(n, 0, -1):
        # Number of stars in the current row is 2 * i - 1
        stars = '*' * (2 * i - 1)
        # Number of leading spaces to center the stars is n - i
        spaces = ' ' * (n - i)
        # Add the centered row to the list
        pyramid.append(spaces + stars + spaces)
    return pyramid

for i in [1, 3, 5]:
    print(generate_inverted_pyramid(i))
