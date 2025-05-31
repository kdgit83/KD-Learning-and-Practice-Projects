def are_equal_strings(s, t):
    """
    Function to check if two strings are equal without using built-in functions.

    Parameters:
    s (str): The first string.
    t (str): The second string.

    Returns:
    bool: True if the strings are equal, False otherwise.
    """
    # Your code here
    if len(s) != len(t):
        return False

    for i in range(len(s)):
        if s[i] != t[i]:
            return False
    return True

for i, j in [("hello", "hello"), ("hello", "world")]:
    print(are_equal_strings(i, j))
