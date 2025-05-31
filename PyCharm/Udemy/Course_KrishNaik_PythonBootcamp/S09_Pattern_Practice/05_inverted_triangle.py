def generate_inverted_triangle(n) -> list[str]:
    """
    Function to return an inverted right-angled triangle of '*' of side n as a list of strings.

    Parameters:
    n (int): The height and base of the triangle.

    Returns:
    list: A list of strings where each string represents a row of the triangle.

    Example:
    Input: 3
    Output: ['***', '**', '*']

    Input: 5
    Output: ['*****', '****', '***', '**', '*']
    """
    # Your code here
    triangle = []
    for i in range(n, 0, -1):
        triangle.append('*' * (i))
    return triangle

for i in [1, 2, 3, 5]:
    print(generate_inverted_triangle(i))
