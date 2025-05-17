import math

def calculate_hypotenuse(side_length_one, side_length_two):
    """
    Pythagorean Theorem: c = (a**2 + b**2) ** 0.5
    """
    # Your code goes here
    return math.sqrt(side_length_one ** 2 + side_length_two ** 2)

side_length_one = 3
side_length_two = 4
result = calculate_hypotenuse(side_length_one, side_length_two)
print(result)
