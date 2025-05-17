def count_words(s):
    """
    Function to count the number of words in the input string.

    Parameters:
    s (str): The input string to check for words.

    Returns:
    int: The count of words in the input string.
    """
    # Your code here
    return len(s.split())

for i in ["Hello, World!", "Python programming is fun."]:
    print(count_words(i))
