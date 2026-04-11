from typing import TypeAlias, TypedDict

IngredientName: TypeAlias = str
DrinkName: TypeAlias = str
IngredientAmounts: TypeAlias = dict[IngredientName, int]


class DrinkRecipe(TypedDict):
    ingredients: IngredientAmounts
    cost: float


Menu: TypeAlias = dict[DrinkName, DrinkRecipe]
