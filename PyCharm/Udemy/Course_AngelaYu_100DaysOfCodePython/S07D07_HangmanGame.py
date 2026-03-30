import random

from Utilities.hangman_art import stages, logo
from Utilities.hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = len(stages) - 1
display = ["_"] * word_length
wrong_letters = []

print(logo)
print("\t\t\tWelcome to Hangman")
print()
print(f"You have to guess the word for {''.join(display)}")
print(f"It consists of {len(display)} letters.")
# print(f"The solution is: {chosen_word}")
print()

while True:
    guess = input("Guess a letter: ").lower()

    if (guess in display) or (guess in wrong_letters):
        print(f"You've already guessed {guess}")
        continue

    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = guess

    print()
    print(f"Current status of the word: {''.join(display)}")
    print()

    if guess not in chosen_word:
        wrong_letters.append(guess)
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print("You lose! End of Game!")
            print(f"The solution is: {chosen_word}")
            break

    if "_" not in display:
        print("You win!! End of Game!!")
        break

    print(stages[lives])
