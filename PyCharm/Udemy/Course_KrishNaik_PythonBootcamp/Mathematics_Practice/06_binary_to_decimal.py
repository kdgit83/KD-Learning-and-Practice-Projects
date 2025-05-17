def binary_to_decimal(binary_str):
    """
    Function to convert a binary string to its decimal integer representation.

    Parameters:
    binary_str (str): The binary string to convert.

    Returns:
    int: The decimal representation of the binary string.
    """
    # Your code here
    decimal_num = 0
    for idx, char in enumerate(binary_str):
        decimal_num += int(char) * (2 ** (len(binary_str) - 1 - idx))
    return decimal_num

for i in ["101", "1101"]:
    print(binary_to_decimal(i))
