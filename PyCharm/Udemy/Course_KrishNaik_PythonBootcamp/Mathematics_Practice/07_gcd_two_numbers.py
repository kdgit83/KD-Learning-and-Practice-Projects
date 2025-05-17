def gcd(n, m):
    """
    Function to find the GCD of two integers without using built-in functions and recursion.

    Parameters:
    n (int): The first integer.
    m (int): The second integer.

    Returns:
    int: The GCD of n and m.
    """
    # Your code here
    if n == m:
        gcd = n
    elif n > m:
        for i in range(m, 0, -1):
            if n % i == 0 and m % i == 0:
                gcd = i
                break
    else:
        for i in range(n, 0, -1):
            if n % i == 0 and m % i == 0:
                gcd = i
                break
    return gcd

for i, j  in [(48, 18), (56, 98)]:
    print(gcd(i, j))
