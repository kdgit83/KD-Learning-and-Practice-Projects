from dataclasses import dataclass


@dataclass(eq=False)
class Asset():
    price: float

    def __post_init__(self):
        price = self.price

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


@dataclass(eq=False)
class Stock(Asset):
    ticker: str
    company: str


@dataclass(eq=False)
class Bond(Asset):
    description: str
    duration: int
    interest: float

ticker = "ABCD"
price = 200.00
description = "ABCD Corporation"

bondname = "30 Year US Treasury"
bondprice = 100.00
duration = 30
interest = 4.38

# ******* DO NOT CHANGE THIS CODE ********
stock = Stock(price, ticker, description)
bond = Bond(bondprice, bondname, duration, interest)

is_eq = (stock == bond)
is_gt = (stock > bond)
is_lt = (stock < bond)
is_gte = (stock >= bond)
is_lte = (stock <= bond)

print(is_eq)
print(is_gt)
print(is_lt)
print(is_gte)
print(is_lte)
