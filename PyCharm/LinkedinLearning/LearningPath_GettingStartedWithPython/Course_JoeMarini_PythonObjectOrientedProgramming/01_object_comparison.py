class Stock:
    def __init__(self, ticker, price, company):
        self.ticker = ticker
        self.price = price
        self.company = company

    # Put your comparison logic here.
    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __le__(self, other):
        return self.price <= other.price

ticker1 = "XYZ"
ticker2 = "ABCD"
price1 = 100.0
price2 = 105.1
company1 = "XYZ Corporation"
company2 = "ABCD Company"

# ***** DO NOT CHANGE THIS CODE ******
stock1 = Stock(ticker1, price1, company1)
stock2 = Stock(ticker2, price2, company2)

is_eq = (stock1 == stock2)
is_gt = (stock1 > stock2)
is_lt = (stock1 < stock2)
is_gte = (stock1 >= stock2)
is_lte = (stock1 <= stock2)

print(is_eq)
print(is_gt)
print(is_lt)
print(is_gte)
print(is_lte)
