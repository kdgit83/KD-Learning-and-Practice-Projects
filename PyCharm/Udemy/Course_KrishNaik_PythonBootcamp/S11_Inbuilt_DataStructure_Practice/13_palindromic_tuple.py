def is_palindromic_tuple(tup: tuple) -> bool:
    """
    Palindromic Tuple
    Check if Tuple is Palindromic
    Design a Python function named is_palindromic_tuple to check if a tuple is palindromic, meaning it reads
    the same forwards and backwards.

    Parameters:
    tup (tuple): The input tuple that you need to check for palindromic property.

    Returns:
    True if the tuple is palindromic, False otherwise.

    Example:
    Input: (1, 2, 3, 2, 1)
    Output: True
    Input: ('a', 'b', 'c', 'b', 'a')
    Output: True
    Input: (1, 2, 3, 4, 5)
    Output: False
    Input: ('x', 'y', 'z', 'x')
    Output: False
    Input: ('a',)
    Output: True
    """
    # Your code goes here
    start = 0
    end = len(tup) - 1
    while start <= end:
        if tup[start] != tup[end]:
            return False
        start += 1
        end -= 1
    return True

tup1 = (1, 2, 3, 2, 1)
tup2 = ('a', 'b', 'c', 'b', 'a')
tup3 = (1, 2, 3, 4, 5)
tup4 = ('x', 'y', 'z', 'x')
tup5 = ('a',)

for tup in [tup1, tup2, tup3, tup4, tup5]:
    print(is_palindromic_tuple(tup))
