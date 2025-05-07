def generate_pyramid(n) -> list[str]:
    """
    Function to return a pyramid pattern of '*' of side n as a list of strings.

    Parameters:
    n (int): The number of rows in the pyramid.

    Returns:
    list: A list of strings where each string represents a row of the pyramid.

    Problem Description:
    You are given an integer n. Your task is to return a pyramid pattern of '*' where each side has n rows,
    represented as a list of strings. The pyramid is centered, with 1 star in the first row, 3 stars in the second row,
    and so on, increasing by 2 stars per row until the base row has 2n - 1 stars.

    Example:
    Input: 3
    Output: ['  *  ', ' *** ', '*****']

    Input: 5
    Output: ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********']
    """
    # Your code here
    # Initialize an empty list to store the rows of the pyramid
    pyramid = []
    # Loop through each row from 1 to n
    for i in range(1, n + 1):
        # Number of stars in the current row is 2 * i - 1
        stars = '*' * (2 * i - 1)
        # Number of leading spaces to center the stars is n - i
        spaces = ' ' * (n - i)
        # Add the centered row to the list
        pyramid.append(spaces + stars + spaces)
    return pyramid

for i in [1, 3, 5]:
    print(generate_pyramid(i))
