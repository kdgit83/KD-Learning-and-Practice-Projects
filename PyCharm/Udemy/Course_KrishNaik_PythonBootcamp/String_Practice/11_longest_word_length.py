def longest_word_length(s):
    """
    Function to find the length of the longest word in a string without using built-in functions.

    Parameters:
    s (str): The input string.

    Returns:
    int: The length of the longest word.
    """
    # Your code here
    word_len = 0
    max_len = 0
    for char in s:
        if char != ' ':
            word_len += 1
        else:
            if word_len > max_len:
                max_len = word_len
            word_len = 0
    # Check for last word:
    if word_len > max_len:
        max_len = word_len

    return max_len

for i in ["The quick brown fox jumps over the lazy dog", "Hello World"]:
    print(longest_word_length(i))
