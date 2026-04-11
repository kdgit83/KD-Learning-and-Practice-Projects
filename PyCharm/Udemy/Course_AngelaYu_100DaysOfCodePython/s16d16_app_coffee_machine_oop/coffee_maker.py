"""Main command-loop module for the OOP coffee machine application."""

from dataclasses import dataclass, field

try:
    from .coffee_input import read_non_negative_int
    from .coffee_menu import CoffeeMenu
    from .coffee_payment import CoffeePayment
    from .coffee_resource import CoffeeResource
    from .coffee_types import DrinkRecipe, IngredientAmounts
except ImportError:
    from coffee_input import read_non_negative_int
    from coffee_menu import CoffeeMenu
    from coffee_payment import CoffeePayment
    from coffee_resource import CoffeeResource
    from coffee_types import DrinkRecipe, IngredientAmounts


@dataclass(slots=True)
class CoffeeMachine:
    """Coordinates menu, payment, and resource operations for the coffee machine."""

    coffee_menu: CoffeeMenu = field(init=False, default_factory=CoffeeMenu)
    coffee_payment: CoffeePayment = field(init=False, default_factory=CoffeePayment)
    coffee_resource: CoffeeResource = field(init=False, default_factory=CoffeeResource)

    def make_coffee(self, drink_name: str, order_ingredients: IngredientAmounts) -> None:
        """Deducts the required ingredients from the resources and serves the drink."""
        self.coffee_resource.consume(order_ingredients)
        print(f"Here is your {drink_name} ☕️. Enjoy!")

    def add_resources(self) -> None:
        """Allows the operator to refill resources until an invalid ingredient is entered."""
        while True:
            prompt = "Which ingredient would you like to add? Water, Milk or Coffee: "
            ingredient = self.coffee_resource.resolve_ingredient(input(prompt))
            if not ingredient:
                break
            quantity = read_non_negative_int(f"How much {ingredient} would you like to add? ")
            self.coffee_resource.add(ingredient, quantity)

    def run(self) -> None:
        """Runs the coffee machine command loop."""
        options = self.coffee_menu.options

        while True:
            user_input = input(f"What would you like? ({options}): ").lower().strip()

            if user_input == "off":
                print("Machine is now shutting down for maintenance.")
                break
            if user_input == "report":
                self.coffee_resource.report()
                self.coffee_payment.report()
            elif user_input == "add":
                self.add_resources()
            elif user_input in self.coffee_menu:
                drink: DrinkRecipe | None = self.coffee_menu.get(user_input)
                if (
                    drink
                    and self.coffee_resource.is_sufficient(drink["ingredients"])
                    and self.coffee_payment.make_payment(user_input, drink["cost"])
                ):
                    self.make_coffee(user_input, drink["ingredients"])
            else:
                print("Invalid input. Please try again.")


if __name__ == "__main__":
    CoffeeMachine().run()
