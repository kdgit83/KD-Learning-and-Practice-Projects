hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum: str) -> int | None:
    """
    Example:
        Hex Num 'CAB' = (C * (16**2)) + (A * (16**1)) + (B * (16**0)) = 3243
    """
    result = 0
    char_len = len(str(hexNum))
    if char_len > 3:
        return None
    for char in str(hexNum):
        if char not in hexNumbers:
            return None
    for i, c in enumerate(str(hexNum)):
        result += hexNumbers[c] * (16 ** (char_len - 1 - i))
    return result

for i in ['ABC', 'Not a Number', '54FD', '5Aog', 'DE', 'B', '86', 'F9E']:
    print(hexToDec(i))
