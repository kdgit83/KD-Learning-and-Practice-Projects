import re


def remove_punctuation(words):
    """Helper function to return a string, removing all punctuations and spaces"""
    return re.sub('\\W+', '', words)

def is_palindrome(words):
    """Palindromes are case-insensitive, so both radar and Radar are valid"""
    clean_words = remove_punctuation(words.lower())
    rev_words = ''.join(reversed(clean_words))
    return clean_words == rev_words

test_cases = [
   (1, 'sagas'),
   (2, 'Radar'),
   (3, 'Was it a cat I saw?'),
   (4, 'Eva, can I see bees in a cave?'),
   (5, 'Red rum, sir, is MURDER!!'),
   (6, "This should not not work"),
   (7, 'radars')
]

for i, j in test_cases:
    print(i, is_palindrome(j))
