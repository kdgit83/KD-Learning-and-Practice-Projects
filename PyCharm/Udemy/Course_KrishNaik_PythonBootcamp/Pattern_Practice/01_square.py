def generate_square(n) -> list[str]:
    """
    Function to return a square pattern of '*' of side n as a list of strings.

    Parameters:
    n (int): The size of the square.

    Returns:
    list: A list of strings where each string represents a row of the square.

    Example:
    Input: 3
    Output: ['***', '***', '***']

    Input: 5
    Output: ['*****', '*****', '*****', '*****', '*****']
    """
    # Your code here
    return ['*' * n for i in range(n)]

for i in [1, 2, 3, 5]:
    print(generate_square(i))
