def generate_sandglass(n: int) -> list[str]:
    """
    Function to return a sandglass pattern of '*' of side n as a list of strings.

    Parameters:
    n (int): The height of the sandglass.

    Returns:
    list: A list of strings where each string represents a row of the sandglass pattern.

    Output:
    A list of strings where each string represents a row in the sandglass pattern.

    Example:
    Input: 3
    Output: ['*****', ' *** ', '  *  ', ' *** ', '*****']

    Input: 4
    Output: ['*******', ' ***** ', '  ***  ', '   *   ', '  ***  ', ' ***** ', '*******']
    """
    # Your code here
    upper_half = []
    for i in range(n, 0, -1):
        stars = '*' * (2 * i - 1)
        spaces = ' ' * (n - i)
        upper_half.append(spaces + stars + spaces)

    lower_half = []
    for i in range(2, n + 1):
        stars = '*' * (2 * i - 1)
        spaces = ' ' * (n - i)
        lower_half.append(spaces + stars + spaces)

    sandglass = upper_half + lower_half
    return sandglass

for i in [1, 3, 4, 5]:
    print(generate_sandglass(i))
