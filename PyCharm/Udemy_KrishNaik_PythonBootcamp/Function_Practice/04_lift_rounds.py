def calculate_lift_rounds(n: int, capacity: int) -> int:
    """
    Function to calculate the number of rounds the lift needs to cover.

    Parameters:
    n (int): Total number of people.
    capacity (int): Maximum number of people the lift can carry in one round.

    Returns:
    int: The number of rounds required to transport all people to the top floor.

    Problem Description:
    You are given n, the total number of people, and capacity, the maximum number of people the lift can carry at a
    time. All people want to go from the ground floor to the top floor. Your task is to calculate the number of rounds
    the lift has to make to transport all the people to the top floor.
    Input:
    Two integers, n and capacity, where n is the total number of people, and capacity is the maximum number of people
    the lift can carry in one round.
    Output:
    An integer representing the number of rounds the lift needs to cover to transport all people to the top floor.
    Example:
    Input: n = 10, capacity = 3
    Output: 4
    Input: n = 7, capacity = 4
    Output: 2
    """
    # Your code here
    return (n // capacity) + 1 if (n % capacity > 0) else (n // capacity)

for i, j in [(10, 3), (7, 4), (87, 8)]:
    print(calculate_lift_rounds(i, j))
