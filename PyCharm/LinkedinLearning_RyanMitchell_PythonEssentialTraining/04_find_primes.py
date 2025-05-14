def allPrimesUpTo(num: int) -> list[int]:
    """
    Example:
        Prime numbers upto 53: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    # Your code goes here.
    result = []
    for i in range(2, num+1):
        for factor in range(2, int(i**0.5) + 1):
            if i % factor == 0:
                break
        else:
            result.append(i)
    return result

for i in [10, 53, 200]:
    print(allPrimesUpTo(i))
