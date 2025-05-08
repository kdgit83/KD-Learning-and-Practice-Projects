def generate_diamond(n: int) -> list[str]:
    """
    Function to return a diamond pattern of '*' of side n as a list of strings.

    Parameters:
    n (int): The number of rows for the upper part of the diamond.

    Returns:
    list: A list of strings where each string represents a row of the diamond.

    Problem Description:
    You are given an integer n. Your task is to return a diamond pattern of '*' with n rows for the upper part (the
    widest row will have 2n - 1 stars), and the lower part is the mirrored version of the upper part. Each row should
    be centered with appropriate spaces.

    Example:
    Input: 3
    Output: ['  *  ', ' *** ', '*****', ' *** ', '  *  ']

    Input: 5
    Output: ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********', ' ******* ', '  *****  ', '   ***   ', '    *    ']
    """
    # Your code here
    upper_half = []
    for i in range(1, n + 1):
        stars = '*' * (2 * i - 1)
        spaces = ' ' * (n - i)
        upper_half.append(spaces + stars + spaces)

    lower_half = []
    for i in range(n - 1, 0, -1):
        stars = '*' * (2 * i - 1)
        spaces = ' ' * (n - i)
        lower_half.append(spaces + stars + spaces)

    diamond = upper_half + lower_half
    return diamond

for i in [1, 3, 5]:
    print(generate_diamond(i))
