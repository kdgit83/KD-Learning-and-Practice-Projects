"""Tip Calculator - Calculates per-person bill amount including tip."""


def calculate_tip():
    """Calculate and display the per-person bill amount including tip."""
    bill = float(input("What was the total bill amount?\n==> $"))
    tip_pct = int(input("How much tip percentage would you like to give? (10, 12, or 15)\n==> "))
    persons = int(input("How many people to split the bill?\n==> "))

    total_bill = bill * (1 + tip_pct / 100)
    per_person_amt = round(total_bill / persons, 2)

    print(f"Each person should pay: ${per_person_amt}\n")


def main():
    """Main function to run the tip calculator in a loop."""
    print("\nWelcome to the tip calculator!")

    while True:
        calculate_tip()
        again = input("Calculate another bill? (Yes/No)\n==> ").strip().lower()
        if again in ("no", "n"):
            print("Thank you for using the tip calculator!")
            break


if __name__ == "__main__":
    main()
