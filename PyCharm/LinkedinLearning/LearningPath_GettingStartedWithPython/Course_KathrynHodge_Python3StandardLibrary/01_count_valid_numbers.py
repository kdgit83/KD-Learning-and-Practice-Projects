def count_valid(numbers: list, lower: int, upper: int) -> int:
    """
    Given a list of integers, count the number of valid integers those fall within the range between lower and upper.
    """
    # Your code goes here
    return len([num for num in numbers if abs(num) in range(lower, upper+1)])

numbers = [-2, 5, -20, 30, -56]
lower = 1
upper = 30
result = count_valid(numbers, lower, upper)
print(result)
