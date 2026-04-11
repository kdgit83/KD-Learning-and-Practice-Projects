from contextlib import redirect_stdout
from io import StringIO
from unittest import TestCase, main
from unittest.mock import patch

try:
    from .coffee_input import INVALID_NUMBER_MESSAGE, read_non_negative_int
    from .coffee_maker import CoffeeMachine
    from .coffee_payment import CoffeePayment
    from .coffee_resource import CoffeeResource
except ImportError:
    from coffee_input import INVALID_NUMBER_MESSAGE, read_non_negative_int
    from coffee_maker import CoffeeMachine
    from coffee_payment import CoffeePayment
    from coffee_resource import CoffeeResource


class CoffeeInputTests(TestCase):
    def test_read_non_negative_int_retries_until_valid_number(self) -> None:
        output = StringIO()

        with patch("builtins.input", side_effect=["-1", "abc", "12"]), redirect_stdout(output):
            value = read_non_negative_int("Enter a number: ")

        self.assertEqual(value, 12)
        self.assertIn(INVALID_NUMBER_MESSAGE, output.getvalue())


class CoffeeMachineTests(TestCase):
    def test_make_coffee_consumes_resources_and_serves_drink(self) -> None:
        machine = CoffeeMachine()
        output = StringIO()

        with redirect_stdout(output):
            machine.make_coffee("espresso", {"water": 50, "coffee": 18})

        self.assertEqual(machine.coffee_resource.resources["water"], 250)
        self.assertEqual(machine.coffee_resource.resources["coffee"], 82)
        self.assertIn("Here is your espresso ☕️. Enjoy!", output.getvalue())

    def test_add_resources_updates_multiple_ingredients_until_invalid_choice(self) -> None:
        machine = CoffeeMachine()

        with patch("builtins.input", side_effect=["w", "50", "m", "25", "x"]):
            machine.add_resources()

        self.assertEqual(machine.coffee_resource.resources["water"], 350)
        self.assertEqual(machine.coffee_resource.resources["milk"], 225)
        self.assertEqual(machine.coffee_resource.resources["coffee"], 100)

    def test_add_resources_retries_until_quantity_is_a_non_negative_int(self) -> None:
        machine = CoffeeMachine()
        output = StringIO()

        with patch("builtins.input", side_effect=["w", "-1", "abc", "2.5", "50", "x"]), redirect_stdout(output):
            machine.add_resources()

        self.assertEqual(machine.coffee_resource.resources["water"], 350)
        self.assertIn("Invalid input. Please enter a non-negative whole number.", output.getvalue())

    def test_run_handles_invalid_input_and_shutdown(self) -> None:
        machine = CoffeeMachine()
        output = StringIO()

        with patch("builtins.input", side_effect=["mocha", "off"]), redirect_stdout(output):
            machine.run()

        printed = output.getvalue()
        self.assertIn("Invalid input. Please try again.", printed)
        self.assertIn("Machine is now shutting down for maintenance.", printed)

    def test_run_completes_successful_order_and_updates_state(self) -> None:
        machine = CoffeeMachine()
        output = StringIO()

        with patch("builtins.input", side_effect=["espresso", "6", "0", "0", "0", "off"]), redirect_stdout(output):
            machine.run()

        printed = output.getvalue()
        self.assertIn("Thank you for the exact drink price.", printed)
        self.assertIn("Here is your espresso ☕️. Enjoy!", printed)
        self.assertEqual(machine.coffee_payment.profit, 1.5)
        self.assertEqual(machine.coffee_resource.resources["water"], 250)
        self.assertEqual(machine.coffee_resource.resources["coffee"], 82)


class CoffeePaymentTests(TestCase):
    def test_make_payment_accepts_change_and_updates_profit(self) -> None:
        payment = CoffeePayment()
        output = StringIO()

        with patch("builtins.input", side_effect=["7", "0", "0", "0"]), redirect_stdout(output):
            accepted = payment.make_payment("espresso", 1.5)

        self.assertTrue(accepted)
        self.assertEqual(payment.profit, 1.5)
        self.assertIn("Here is $0.25 in change.", output.getvalue())

    def test_make_payment_refunds_when_money_is_insufficient(self) -> None:
        payment = CoffeePayment()
        output = StringIO()

        with patch("builtins.input", side_effect=["5", "0", "0", "0"]), redirect_stdout(output):
            accepted = payment.make_payment("espresso", 1.5)

        self.assertFalse(accepted)
        self.assertEqual(payment.profit, 0.0)
        self.assertIn("Sorry that's not enough money. Money refunded $1.25.", output.getvalue())

    def test_make_payment_retries_invalid_coin_inputs(self) -> None:
        payment = CoffeePayment()
        output = StringIO()

        with patch("builtins.input", side_effect=["-1", "abc", "7", "0", "0", "0"]), redirect_stdout(output):
            accepted = payment.make_payment("espresso", 1.5)

        self.assertTrue(accepted)
        self.assertEqual(payment.profit, 1.5)
        printed = output.getvalue()
        self.assertIn("Invalid input. Please enter a non-negative whole number.", printed)
        self.assertIn("Here is $0.25 in change.", printed)


class CoffeeResourceTests(TestCase):
    def test_is_sufficient_reports_all_shortages(self) -> None:
        resource = CoffeeResource()
        output = StringIO()

        with redirect_stdout(output):
            sufficient = resource.is_sufficient({"water": 350, "milk": 250, "coffee": 10})

        self.assertFalse(sufficient)
        printed = output.getvalue()
        self.assertIn("Sorry, there is not enough water.", printed)
        self.assertIn("Sorry, there is not enough milk.", printed)


if __name__ == "__main__":
    main()

