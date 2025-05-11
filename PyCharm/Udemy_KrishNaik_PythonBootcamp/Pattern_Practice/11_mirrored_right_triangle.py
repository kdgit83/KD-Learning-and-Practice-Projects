def generate_right_angled_triangle(n: int) -> list[str]:
    """
    Function to return a right-angled triangle of '*' of side n as a list of strings.

    Parameters:
    n (int): The height of the triangle.

    Returns:
    list: A list of strings where each string represents a row of the triangle.

    Output:
    A list of strings where each string represents a row in the right-angled triangle, right-aligned.

    Example:
    Input: 4
    Output: ['   *', '  **', ' ***', '****']

    Input: 3
    Output: ['  *', ' **', '***']
    """
    # Your code here
    triangle = []
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        stars = '*' * (i + 1)
        row = spaces + stars
        triangle.append(row)
    return triangle

for i in [1, 2, 3, 5]:
    print(generate_right_angled_triangle(i))
