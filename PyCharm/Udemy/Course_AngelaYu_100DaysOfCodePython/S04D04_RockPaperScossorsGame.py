import random

# Rock Paper Scissors ASCII Art

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]

while True:
    print("\nWelcome to Rock-Paper-Scissors Game!!")
    print("0 for Rock, 1 for Paper, 2 for Scissors.\n")

    computer_choice = random.randint(0, 2)
    user_choice = int(input("Enter a number between 0 and 2. \n===> "))
    if user_choice in [0, 1, 2]:
        print("You chose: ")
        print(game_images[user_choice])
        print()
        print("Computer chose: ")
        print(game_images[computer_choice])

    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number. You Lose!")
    elif user_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose!")
    elif  computer_choice > user_choice:
        print("You Lose!")
    elif  user_choice > computer_choice:
        print("You Win!")
    elif computer_choice == user_choice:
        print("It's a Draw!")

    user_wish = input("\nType 'N' if you want to exit the game ==> ")
    if user_wish.isalpha() and user_wish.lower() == 'n':
        break
