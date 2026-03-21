def is_palindrome(teststr: str) -> bool:
    """Given a string, return whether it is a palindrome or not."""
    # Your code goes here.
    reverse_str = ''
    lower_str = teststr.lower()
    raw_str = ''
    for c in lower_str:
        if c.isalnum():
            raw_str += c
    raw_len = len(raw_str)
    for i in range(raw_len):
        reverse_str += raw_str[raw_len - 1 - i]
    return True if reverse_str == raw_str else False

list_of_strings = ["Radar?",
                   "Race car!",
                   "Madam, I'm Adam!",
                   "Hello World",
                   "A man, a plan, a canal Panama!"]

for string in list_of_strings:
    print(is_palindrome(string))
