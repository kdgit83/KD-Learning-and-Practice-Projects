def is_anagram(s, t):
    """
    Function to check if t is an anagram of s.

    Parameters:
    s (str): The first input string.
    t (str): The second input string.

    Returns:
    bool: True if t is an anagram of s, False otherwise.
    """
    # Your code here
    if len(s) != len(t):
        return False

    dict_s = {}
    for char in s.lower():
        dict_s[char] = dict_s.get(char, 0) + 1

    dict_t = {}
    for char in t.lower():
        dict_t[char] = dict_t.get(char, 0) + 1

    for key in dict_s:
        if dict_s[key] != dict_t.get(key, 0):
            return False
    return True

for i, j in [("anagram", "nagaram"), ("rat", "car")]:
    print(is_anagram(i, j))
