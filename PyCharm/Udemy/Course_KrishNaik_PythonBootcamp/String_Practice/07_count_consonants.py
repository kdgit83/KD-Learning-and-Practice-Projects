def count_consonants(s):
    """
    Function to count the number of consonants in the input string.

    Parameters:
    s (str): The input string to check for consonants.

    Returns:
    int: The count of consonants in the input string.
    """
    # Your code here
    count = 0
    vowels = 'aeiou'
    for char in s.lower():
        if char.isalpha() and char not in vowels:
            count += 1
    return count

for i in ["programming", "Hello, World!", "Python programming is fun."]:
    print(count_consonants(i))
