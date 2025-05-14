def triangle(num: int) -> int:
    """
    Example:
        triangle(3) = 3 + 2 + 1 = 6
        triangle(4) = 4 + 3 + 2 + 1 = 10

    HINT 1: Two triangles, when added together, make a square
    HINT 2: Your two triangles will be of different sizes
    HINT 3: Here are some examples for you:

    triangle(2) + triangle(3) = 3 + 6 = 9
    triangle(3) + triangle(4) = 6 + 10 = 16
    """
    if num == 1:
        return num
    return num + triangle(num - 1)

def square(num: int) -> int:
    return triangle(num) + triangle(num - 1)
