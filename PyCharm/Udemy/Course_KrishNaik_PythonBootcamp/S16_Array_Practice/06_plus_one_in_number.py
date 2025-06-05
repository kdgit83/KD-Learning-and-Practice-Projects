def plus_one(digits: list[int]) -> list[int]:
    """
    Function to increment a large integer represented as a list of digits by one.
    :param digits: List[int] -> List of digits representing the large integer
    :return: List[int] -> The list representing the integer after incrementing

    Description:
    You are given a large integer represented as an integer array digits, where each digits[i] is the i-th digit of the
    integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer
     does not contain any leading zeroes.
    Write a function to increment the large integer by one and return the resulting array of digits.

    Input Parameters:
    digits (List[int]): A list of integers where each integer represents a digit of a large number.

    Output:
    List[int]: The list representing the number after incrementing it by one.

    Example:
    Input: digits = [1, 2, 3]
    Output: [1, 2, 4]

    Input: digits = [4, 3, 2, 1]
    Output: [4, 3, 2, 2]

    Input: digits = [9, 9, 9]
    Output: [1, 0, 0, 0]
    """
    # Start from the last digit
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    # If all digits are 9, the result will be a list of zeros with a 1 at the beginning
    return [1] + digits

digits_1 = [1, 2, 3]
digits_2 = [4, 3, 2, 1]
digits_3 = [9, 9, 9]
digits = [digits_1, digits_2, digits_3]

for digit in digits:
    print(plus_one(digit))
