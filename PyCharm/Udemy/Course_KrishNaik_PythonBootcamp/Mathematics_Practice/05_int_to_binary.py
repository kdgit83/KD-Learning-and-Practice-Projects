def int_to_binary(n):
    """
    Function to convert an integer to its binary representation.

    Parameters:
    n (int): The integer to convert.

    Returns:
    str: The binary representation of the integer.
    """
    # Your code here
    is_negative = False
    binary_str = ""
    if n == 0:
        return "0"
    elif n < 0:
        is_negative = True
        n = -n

    while n > 0:
        remainder = n % 2
        binary_str = str(remainder) + binary_str
        n = n // 2

    return "-" + binary_str if is_negative else binary_str

for i in [5, -5, 8]:
    print(int_to_binary(i))
