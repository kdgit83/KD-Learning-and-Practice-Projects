from fractions import Fraction

def add_fractions(numerator1: int, denominator1: int, numerator2: int, denominator2: int) -> tuple:
    # Your code goes here
    fraction1 = Fraction(numerator1, denominator1)
    fraction2 = Fraction(numerator2, denominator2)
    sum = fraction1 + fraction2
    return sum.numerator, sum.denominator

numerator1 = 1
denominator1 = 2
numerator2 = 1
denominator2 = 3
result = add_fractions(numerator1, denominator1, numerator2, denominator2)
print(result)
