def remove_duplicates(s):
    """
    Function to remove duplicate characters from the input string.

    Parameters:
    s (str): The input string from which duplicates need to be removed.

    Returns:
    str: The modified string with duplicates removed.
    """
    # Your code here
    clean_s = ''
    for char in s:
        if char not in clean_s:
            clean_s += char
    return clean_s

for i in ["programming", "Hello, World!"]:
    print(remove_duplicates(i))
