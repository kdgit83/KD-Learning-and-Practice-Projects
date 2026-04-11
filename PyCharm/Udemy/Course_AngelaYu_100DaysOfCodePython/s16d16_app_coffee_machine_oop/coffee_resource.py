"""Resource storage and ingredient operations for the OOP coffee machine."""

from dataclasses import dataclass, field

try:
    from .coffee_types import IngredientAmounts, IngredientName
except ImportError:
    from coffee_types import IngredientAmounts, IngredientName

INGREDIENT_UNITS: dict[IngredientName, str] = {"water": "ml", "milk": "ml", "coffee": "g"}
INGREDIENT_ALIASES: dict[str, IngredientName] = {"w": "water", "m": "milk", "c": "coffee"}


@dataclass(slots=True)
class CoffeeResource:
    """Tracks available ingredients and provides refill/report operations."""

    resources: IngredientAmounts = field(
        init=False,
        default_factory=lambda: {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        },
    )

    def add(self, ingredient_name: IngredientName, ingredient_amount: int) -> None:
        """Adds the supplied ingredient quantity to the given ingredient."""
        self.resources[ingredient_name] += ingredient_amount

    def is_sufficient(self, required_ingredients: IngredientAmounts) -> bool:
        """Returns True when all required ingredients are available."""
        shortages = [
            ingredient
            for ingredient, amount in required_ingredients.items()
            if amount > self.resources[ingredient]
        ]
        for ingredient in shortages:
            print(f"Sorry, there is not enough {ingredient}.")
        return not shortages

    def consume(self, required_ingredients: IngredientAmounts) -> None:
        """Deducts the supplied ingredients from the current resources."""
        for ingredient, amount in required_ingredients.items():
            self.resources[ingredient] -= amount

    def report(self) -> None:
        """Prints the current coffee resources."""
        for ingredient, amount in self.resources.items():
            print(f"{ingredient}: {amount}{INGREDIENT_UNITS.get(ingredient, '')}")

    def resolve_ingredient(self, raw_choice: str) -> IngredientName | None:
        """Maps user input to a valid ingredient name when possible."""
        choice = raw_choice.lower().strip()
        return INGREDIENT_ALIASES.get(choice[:1]) if choice else None
