"""Coffee machine simulation: takes orders, processes coins, and manages resources."""

COFFEE_MENU = {
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

COIN_VALUES = {
    "quarters": 0.25,
    "dimes":    0.10,
    "nickels":  0.05,
    "pennies":  0.01,
}

INGREDIENT_UNITS = {"water": "ml", "milk": "ml", "coffee": "g"}
INGREDIENT_ALIASES = {"w": "water", "m": "milk", "c": "coffee"}

PROFIT = [0]  # mutable container – avoids a global statement in functions
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resource_addition(ingredient_name: str, ingredient_amount: int) -> None:
    """Adds the supplied ingredient quantity to the given ingredient."""
    resources[ingredient_name] += ingredient_amount


def resource_report(coffee_resources: dict, money_profit: float) -> None:
    """Prints the current coffee resources and money profit."""
    for ingredient, amount in coffee_resources.items():
        unit = INGREDIENT_UNITS.get(ingredient, "")
        print(f"{ingredient}: {amount}{unit}")
    print(f"Money: ${money_profit}")


def is_resource_sufficient(order_ingredients: dict) -> bool:
    """Returns True when order can be made, False if ingredients are insufficient."""
    short = [item for item, qty in order_ingredients.items() if qty > resources[item]]
    for item in short:
        print(f"Sorry, there is not enough {item}.")
    return not short


def process_coins(drink_name: str, drink_cost: float) -> float:
    """Returns the total calculated from coins inserted."""
    print(f"{drink_name} costs ${drink_cost}")
    print("Please insert coins.")
    return sum(
        int(input(f"How many {coin} (${value:.2f})?: ")) * value
        for coin, value in COIN_VALUES.items()
    )


def is_transaction_successful(money_received: float, drink_cost: float) -> bool:
    """Returns True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change." if change else "Thank you for the exact drink price.")
        PROFIT[0] += drink_cost
        return True
    print(f"Sorry that's not enough money. Money refunded ${money_received}.")
    return False


def make_coffee(drink_name: str, order_ingredients: dict) -> None:
    """Deducts the required ingredients from the resources."""
    for item, amount in order_ingredients.items():
        resources[item] -= amount
    print(f"Here is your {drink_name} ☕️. Enjoy!")


MENU_PROMPT = f"What would you like? ({'/'.join(COFFEE_MENU)}): "

while True:
    user_input = input(MENU_PROMPT).lower().strip()

    if user_input == "off":
        print("Machine is now shutting down for maintenance.")
        break
    if user_input == "report":
        resource_report(resources, PROFIT[0])
    elif user_input == "add":
        while True:
            add_prompt = "Which ingredient would you like to add? Water, Milk or Coffee: "
            raw = input(add_prompt).lower().strip()
            coffee_ingredient = INGREDIENT_ALIASES.get(raw[:1])
            if not coffee_ingredient:
                break
            ingredient_quantity = int(
                input(f"How much {coffee_ingredient} would you like to add? ")
            )
            resource_addition(coffee_ingredient, ingredient_quantity)
    elif user_input in COFFEE_MENU:
        drink = COFFEE_MENU[user_input]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins(user_input, drink["cost"])
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_input, drink["ingredients"])
    else:
        print("Invalid input. Please try again.")
