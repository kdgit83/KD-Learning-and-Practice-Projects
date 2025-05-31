def is_prime(n: int) -> bool:
    """
    Function to check if a number is prime.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if n is prime, False otherwise.
    """
    # Your code here
    for i in range(n):
        for factor in range(2, int(n ** 0.5) + 1):
            if n % factor == 0:
                return False
    return True

for i in [5, 4, 9, 13]:
    print(is_prime(i))
