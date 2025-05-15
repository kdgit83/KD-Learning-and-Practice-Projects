def generate_rectangle(n, m) -> list[str]:
    """
    Function to return a rectangle pattern of '*' with length n and breadth m as a list of strings.

    Parameters:
    n (int): The number of rows in the rectangle.
    m (int): The number of columns in the rectangle.

    Returns:
    list: A list of strings where each string represents a row of the rectangle pattern.

    Example:
    Input: n = 4, m = 5
    Output: ['*****', '*****', '*****', '*****']

    Input: n = 3, m = 2
    Output: ['**', '**', '**']
    """
    # Your code here
    return ['*' * m for i in range(n)]

for i, j in [(1, 1), (3, 2), (4, 5)]:
    print(generate_rectangle(i, j))
