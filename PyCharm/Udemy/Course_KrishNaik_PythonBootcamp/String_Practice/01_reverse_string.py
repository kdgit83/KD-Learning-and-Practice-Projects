def reverse_string(s):
    """
    Function to return the reversed version of the input string.

    Parameters:
    s (str): The input string to be reversed.

    Returns:
    str: The reversed string.
    """
    # Your code here
    rev_s = ''
    for char in s:
        rev_s = char + rev_s
    return rev_s

for i in ["hello", "python", "level"]:
    print(reverse_string(i))
