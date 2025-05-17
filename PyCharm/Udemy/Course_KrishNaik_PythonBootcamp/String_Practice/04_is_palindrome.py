def is_palindrome(s):
    """
    Function to check if the input string is a palindrome.

    Parameters:
    s (str): The input string to check.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Your code here
    formatted_s = ''
    for char in s.lower():
        if char.isalpha():
            formatted_s += char

    return formatted_s == formatted_s[::-1]

for i in ["A man a plan a canal Panama", "Hello, World!"]:
    print(is_palindrome(i))
