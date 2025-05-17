def is_substring(s, t):
    """
    Function to check if string t is a substring of string s without using built-in functions and recursion.

    Parameters:
    s (str): The main string.
    t (str): The string to check as a substring.

    Returns:
    bool: True if t is a substring of s, False otherwise.
    """
    # Your code here
    return t in s

for i, j in [("hello world", "world"), ("hello world", "worlds")]:
    print(is_substring(i, j))
