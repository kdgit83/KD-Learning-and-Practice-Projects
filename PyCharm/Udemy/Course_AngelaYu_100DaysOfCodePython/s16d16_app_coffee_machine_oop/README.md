# OOP Coffee Machine

Object-oriented version of the coffee machine app from `s15d15_app_coffee_machine.py`.

## Files

- `coffee_maker.py` - main app loop
- `coffee_menu.py` - drink menu and lookups
- `coffee_input.py` - shared input validation helpers
- `coffee_payment.py` - coin handling and profit tracking
- `coffee_resource.py` - ingredient storage and resource logic
- `coffee_types.py` - shared type aliases
- `test_coffee_machine.py` - automated tests

## Run the app

```powershell
python -u coffee_maker.py
```

The app now safely retries when coin counts or refill quantities are entered as invalid values such as blanks, words, decimals, or negative numbers.

## Run the tests

From the `PyCharm` project root:

```powershell
python -m unittest Udemy.Course_AngelaYu_100DaysOfCodePython.s16d16_app_coffee_machine_oop.test_coffee_machine -v
```

