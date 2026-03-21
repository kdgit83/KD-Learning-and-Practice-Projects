def factorial(num: int) -> int | None:
    """
    Example: Factorial(5) -> 5 * 4 * 3 * 2 * 1 = 120
    """
    # Your code goes here.
    if not isinstance(num, int):
        return None
    elif num < 0:
        return None
    elif num == 0:
        return 1
    else:
        return num * factorial(num - 1)

for i in [3, 5, 8, 10]:
    print(factorial(i))
