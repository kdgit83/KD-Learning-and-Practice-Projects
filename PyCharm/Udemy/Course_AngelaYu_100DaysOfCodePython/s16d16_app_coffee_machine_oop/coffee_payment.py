"""Payment and profit handling for the OOP coffee machine."""

from dataclasses import dataclass, field

try:
    from .coffee_input import read_non_negative_int
except ImportError:
    from coffee_input import read_non_negative_int


@dataclass(slots=True)
class CoffeePayment:
    """Handles coin processing and tracks earned profit."""

    currency_symbol: str = "$"
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01,
    }
    profit: float = field(init=False, default=0.0)

    def report(self) -> None:
        """Prints the current profit."""
        print(f"Money: {self.currency_symbol}{self.profit}")

    def process_coins(self, drink_name: str, drink_cost: float) -> float:
        """Returns the total calculated from coins inserted."""
        print(f"{drink_name} costs ${drink_cost}")
        print("Please insert coins.")
        return sum(
            read_non_negative_int(f"How many {coin} (${value:.2f})?: ") * value
            for coin, value in self.COIN_VALUES.items()
        )

    def make_payment(self, drink_name: str, cost: float) -> bool:
        """Returns True when payment is accepted or False if insufficient."""
        money_received = self.process_coins(drink_name, cost)
        if money_received >= cost:
            change = round(money_received - cost, 2)
            print(
                f"Here is {self.currency_symbol}{change} in change."
                if change
                else "Thank you for the exact drink price."
            )
            self.profit += cost
            return True
        print(f"Sorry that's not enough money. Money refunded ${round(money_received, 2)}.")
        return False
