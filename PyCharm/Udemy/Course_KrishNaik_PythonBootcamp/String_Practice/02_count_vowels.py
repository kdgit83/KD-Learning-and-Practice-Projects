def count_vowels(s):
    """
    Function to count the number of vowels in the input string.

    Parameters:
    s (str): The input string to check for vowels.

    Returns:
    int: The count of vowels in the input string.
    """
    # Your code here
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in s:
        if char.lower() in vowels:
            count += 1
    return count

for i in ["Hello, World!", "Python Programming", "A level - five!"]:
    print(count_vowels(i))
