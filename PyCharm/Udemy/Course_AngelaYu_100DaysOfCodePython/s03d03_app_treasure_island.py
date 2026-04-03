"""Treasure Island - A text adventure game."""
from utilities.treasureisland_art import logo  # pylint: disable=import-error


def choose_door(choice):
    """Handle the final door choice and determine the outcome."""
    doors = {
        "red": "It's a room full of fire. Game Over.",
        "blue": "You enter a room of beasts. Game Over.",
        "yellow": "You found the treasure. You Win!"
    }
    return doors.get(choice, "You chose a door that doesn't exist. Game Over.")


def play_game():
    """Main game logic for the Treasure Island adventure."""
    print(logo)
    print("\nWelcome to Treasure Island.\nYour mission is to find the treasure.\n")

    # First choice: Left or Right
    choice1 = input("You're at a crossroad, where do you want to go? "
                    "Type \"Left\" or \"Right\".\n==> ").lower()

    if choice1 != "left":
        print("You fell into a hole. Game Over.")
        return

    # Second choice: Wait or Swim
    choice2 = input("You've come to a lake, there is an island in the middle of the lake. "
                    "Type \"Wait\" to wait for a boat. Type \"Swim\" to swim across.\n==> "
                    ).lower()

    if choice2 != "wait":
        print("You got attacked by an angry trout. Game Over.")
        return

    # Third choice: Door color
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. "
                    "One \"Red\", one \"Blue\" and one \"Yellow\". "
                    "Which colour do you choose?\n==> ").lower()

    print(choose_door(choice3))


def main():
    """Main function to run the game in a loop until user exits."""
    while True:
        play_game()
        again = input("\nDo you want to play again? (Yes/No)\n==> ").strip().lower()
        if again in ("no", "n"):
            print("Thanks for playing Treasure Island!")
            break
        print("\n" + "="*50 + "\n")


if __name__ == "__main__":
    main()
