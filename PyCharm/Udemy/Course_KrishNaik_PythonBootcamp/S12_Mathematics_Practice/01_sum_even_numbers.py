def sum_of_even_numbers(n: int) -> int:
    """
    Function to return the sum of the first n even natural numbers.

    Parameters:
    n (int): The number of even numbers to sum.

    Returns:
    int: The sum of the first n even natural numbers.
    """
    # Your code here
    total = 0
    current_even_num = 2
    for i in range(n):
        total += current_even_num
        current_even_num += 2
    return total

for i in [3, 5]:
    print(sum_of_even_numbers(i))
