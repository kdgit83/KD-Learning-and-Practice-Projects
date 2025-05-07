def generate_hollow_square(n) -> list[str]:
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.

    Parameters:
    n (int): The size of the square.

    Returns:
    list: A list of strings where each string represents a row of the hollow square.

    Example:
    Input: 3
    Output: ['***', '* *', '***']

    Input: 5
    Output: ['*****', '*   *', '*   *', '*   *', '*****']
    """
    # Your code here
    hollow_square = []

    # Handle the case when n is 1 separately
    if n == 1:
        return ['*']

    # The first and last rows are full of '*'
    hollow_square.append('*' * n)  # First row
    # For the middle rows, the first and last characters are '*', rest are spaces
    for i in range(n - 2):
        hollow_square.append('*' + ' ' * (n - 2) + '*')

    # The last row is also full of '*'
    hollow_square.append('*' * n)  # Last row

    # Return the list of rows
    return hollow_square

for i in [1, 2, 3, 5]:
    print(generate_hollow_square(i))
