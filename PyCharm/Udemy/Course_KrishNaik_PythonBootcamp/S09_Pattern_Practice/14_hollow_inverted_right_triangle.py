def generate_hollow_inverted_right_angled_triangle(n: int) -> list[str]:
    """
    Function to return a hollow inverted right-angled triangle of '*' of side n as a list of strings.

    Parameters:
    n (int): The height of the triangle.

    Returns:
    list: A list of strings where each string represents a row of the triangle.

    Output:
    A list of strings where each string represents a row in the hollow inverted right-angled triangle.

    Example:
    Input: 4
    Output: ['****', '* *', '**', '*']

    Input: 5
    Output: ['*****', '*  *', '* *', '**', '*']
    """
    # Your code here
    triangle = []
    for i in range(n, 0, -1):
        if i == n or i == 1:
            row = '*' * i
        else:
            row = '*' + ' ' * (i - 2) + '*'
        triangle.append(row)
    return triangle

for i in [1, 3, 4, 5]:
    print(generate_hollow_inverted_right_angled_triangle(i))
