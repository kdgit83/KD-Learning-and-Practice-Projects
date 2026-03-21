def find_largest(strings: list[str]) -> int:
    """Given a list of strings, return the length of the longest string in the list."""
    # Your code goes here
    if len(strings) == 0:
        return 0
    else:
        num_list = [len(string) for string in strings]
        return max(num_list)

test_strings = [
    "Hello World!",
    "And how can this be? For he is the Kwisatz Haderach!",
    "Four score and seven years ago",
    "Life moves pretty fast. If you don’t stop and look around once in a while, you could miss it."
]

print(find_largest(test_strings))