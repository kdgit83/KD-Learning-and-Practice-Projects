"""Menu definitions and lookup helpers for the OOP coffee machine."""

from dataclasses import dataclass, field

try:
    from .coffee_types import DrinkRecipe, IngredientAmounts, Menu
except ImportError:
    from coffee_types import DrinkRecipe, IngredientAmounts, Menu

COFFEE_MENU: Menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


@dataclass(slots=True)
class CoffeeMenu:
    """Provides access to available drinks, ingredients, and costs."""

    menu_details: Menu = field(init=False, default_factory=lambda: COFFEE_MENU)

    @property
    def options(self) -> str:
        """Returns all the names of the available menu items."""
        return "/".join(self.menu_details)

    def get(self, drink_name: str) -> DrinkRecipe | None:
        """Returns the drink details."""
        return self.menu_details.get(drink_name)

    def __contains__(self, drink_name: str) -> bool:
        """Returns True when the given drink exists in the menu."""
        return drink_name in self.menu_details

    def ingredients_for(self, item_name: str) -> IngredientAmounts:
        """Returns ingredients of the given item name."""
        drink = self.get(item_name)
        return drink["ingredients"] if drink else {}

    def cost_for(self, item_name: str) -> float:
        """Returns cost of the given item name."""
        drink = self.get(item_name)
        return drink["cost"] if drink else 0.0
