import string

print(f"Punctuations are any of the following: {string.punctuation}")

def contains_punctuation(input_str):
    ''' Return True if the input_str contains punctuations.
    Return False otherwise'''
    return any(char in string.punctuation for char in input_str)

test_cases = [
   (1, "Readability counts."),
   (2, "If the implementation is hard to explain, it's a bad idea."),
   (3, "There should be one-- and preferably only one --obvious way to do it."),
   (4, "Errors should never pass silently"),
   (5, "Simple is better than complex")
]

for i, j in test_cases:
    print(i, contains_punctuation(j))
