import string
from utilities.caesarcipher_art import logo

print(logo)
alphabets = list(string.ascii_lowercase)
alpha_count = len(alphabets)


def caeser(start_text: str, shift_amount: int, cipher_direction: str) -> None:
    end_text = ""
    char_is_upper = False
    for char in start_text:
        if char.isupper():
            char_is_upper = True
            char = char.lower()
        if char in alphabets:
            position = alphabets.index(char)
            if cipher_direction in ["d", "decode"]:
                cipher_direction = "decode"
                if (position - shift_amount) >= 0:
                    if char_is_upper:
                        end_text += alphabets[position - shift_amount].upper()
                    else:
                        end_text += alphabets[position - shift_amount]
                elif (position - shift_amount) < 0:
                    if char_is_upper:
                        end_text += alphabets[position - shift_amount + alpha_count].upper()
                    else:
                        end_text += alphabets[position - shift_amount + alpha_count]
            elif cipher_direction in ["e", "encode"]:
                cipher_direction = "encode"
                if (position + shift_amount) <= alpha_count - 1:
                    if char_is_upper:
                        end_text += alphabets[position + shift_amount].upper()
                    else:
                        end_text += alphabets[position + shift_amount]
                elif (position + shift_amount) > alpha_count - 1:
                    if char_is_upper:
                        end_text += alphabets[position + shift_amount - alpha_count].upper()
                    else:
                        end_text += alphabets[position + shift_amount - alpha_count]
        else:
            end_text += char
        char_is_upper = False

    print(f"The {cipher_direction}d text is: {end_text}")


while True:
    direction = input("Type letter either 'e' to Encrypt or 'd' to Decrypt:\n===> ").lower()
    if direction == '0':
        break
    if direction not in ['e', 'encode', 'd', 'decode']:
        continue
    text = input("\nType your message:\n")
    while True:
        shift = input("\nType the shift number, a positive integer number:\n")
        if shift.isnumeric():
            break
        else:
            continue
    shift = int(shift) % alpha_count
    caeser(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("\nPress '0' to exit the program.\n")
    if restart == '0':
        print("Goodbye!!")
        break
