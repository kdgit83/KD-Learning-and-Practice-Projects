import random
import string

# For lowercase alphabets only
all_lower_letters = list(string.ascii_lowercase)

# For uppercase alphabets only
all_upper_letters = list(string.ascii_uppercase)

# For all lowercase and uppercase alphabets combined
all_alphabets = list(string.ascii_letters)

# For all digits only
all_digits = list(string.digits)

# For all punctuations only
all_punctuations = list(string.punctuation)

password_ingredients = [all_lower_letters, all_upper_letters, all_digits, all_punctuations]

print("Welcome to Password Generator!")

while True:
    nr_lower_letters = int(input("How many lowercase letters would you like in your password?\n==> "))
    if nr_lower_letters <= len(all_lower_letters):
        break
    else:
        print(f"Too long count. Limit within {len(all_lower_letters)} chars.")

while True:
    nr_upper_letters = int(input("How many uppercase letters would you like in your password?\n==> "))
    if nr_upper_letters <= len(all_upper_letters):
        break
    else:
        print(f"Too long count. Limit within {len(all_upper_letters)} chars.")

while True:
    nr_digits = int(input("How many numbers would you like in your password?\n==> "))
    if nr_digits <= len(all_digits):
        break
    else:
        print(f"Too long count. Limit within {len(all_digits)} chars.")

while True:
    nr_punctuations = int(input("How many symbols would you like in your password?\n==> "))
    if nr_punctuations <= len(all_punctuations):
        break
    else:
        print(f"Too long count. Limit within {len(all_punctuations)} chars.")

password_ingredient_count = [nr_lower_letters, nr_upper_letters, nr_digits, nr_punctuations]
password_chars = []

for item in range(len(password_ingredients)):
    for num in range(password_ingredient_count[item]):
        while True:
            random_char = random.choice(password_ingredients[item])
            if random_char not in password_chars:
                password_chars.append(random_char)
                break

random.shuffle(password_chars)
password = ''.join(password_chars)
print(f"Your Password is: {password}")
