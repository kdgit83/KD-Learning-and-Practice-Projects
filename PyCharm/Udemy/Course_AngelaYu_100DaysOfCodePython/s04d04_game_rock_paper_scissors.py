"""Rock-Paper-Scissors Game - A text-based game against the computer."""
import random

CHOICES = {
    0: "Rock",
    1: "Paper",
    2: "Scissors"
}

IMAGES = {
    0: """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    1: """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    2: """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

WINNING_COMBOS = {
    (0, 2),  # Rock beats Scissors
    (1, 0),  # Paper beats Rock
    (2, 1)   # Scissors beats Paper
}


def get_user_choice():
    """Get and validate user's choice."""
    while True:
        try:
            choice = int(
                input(
                    "Enter a number between 0 and 2 "
                    "(0=Rock, 1=Paper, 2=Scissors).\n===> "
                )
            )
            if choice in CHOICES:
                return choice
            print("Invalid choice! Please enter 0, 1, or 2.\n")
        except ValueError:
            print("Invalid input! Please enter a number.\n")


def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "Draw"
    if (user_choice, computer_choice) in WINNING_COMBOS:
        return "Win"
    return "Lose"


def display_choices(user_choice, computer_choice):
    """Display the choices made by user and computer."""
    print(f"You chose {CHOICES[user_choice]}:")
    print(IMAGES[user_choice])
    print(f"Computer chose {CHOICES[computer_choice]}:")
    print(IMAGES[computer_choice])


def play_game():
    """Play a single round of Rock-Paper-Scissors."""
    computer_choice = random.randint(0, 2)
    user_choice = get_user_choice()

    display_choices(user_choice, computer_choice)

    result = determine_winner(user_choice, computer_choice)
    if result == "Win":
        print("🎉 You Win!")
    elif result == "Lose":
        print("😔 You Lose!")
    else:
        print("🤝 It's a Draw!")


def main():
    """Main function to run the game in a loop."""
    print("\n🎮 Welcome to Rock-Paper-Scissors Game!\n")

    while True:
        play_game()
        again = input("\nDo you want to play again? (Yes/No)\n===> ").strip().lower()
        if again in ("no", "n"):
            print("Thanks for playing! Goodbye! 👋\n")
            break


if __name__ == "__main__":
    main()
