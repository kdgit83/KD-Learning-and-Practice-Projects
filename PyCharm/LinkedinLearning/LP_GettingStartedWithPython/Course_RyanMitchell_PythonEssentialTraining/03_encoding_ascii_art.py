def encodeString(stringVal: str) -> list[tuple[str, int]]:
    """
    Run-length encoding
    https://en.wikipedia.org/wiki/Run-length_encoding
    Example:
        "AAAAABBBBAAA" -> [('A', 5), ('B', 4), ('A', 3)]
    """
    # Your code goes here.
    encodedList = []
    prevChar = stringVal[0]
    count = 0
    for char in stringVal:
        if prevChar != char:
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
        count += 1
    encodedList.append((prevChar, count))
    return encodedList


def decodeString(encodedList: list) -> str:
    # Your code goes here.
    decodedStr = ''
    for item in encodedList:
        decodedStr = decodedStr + (item[0] * item[1])
    return decodedStr

for i in ['AAAAABBBBAAA', 'Bookkeeping']:
    print(encodeString(i))

print(decodeString([('W', 5), ('1', 2), ('G', 3)]))
