"""
A Caesar cipher program that encodes or decodes text based on user input.

This program allows users to apply the Caesar cipher to a given text by specifying
the desired shift amount and cipher direction (encode or decode). It handles both
uppercase and lowercase characters, preserving their case during the transformation,
and leaves non-alphabetic characters unchanged. The program runs in a loop, allowing
multiple encryption or decryption until the user decides to exit.
"""
from typing import Optional

from utilities.caesarcipher_art import logo  # pylint: disable=import-error

def shift_character(char: str, shift_amount: int) -> str:
    """
    Shift a single character by the given amount using Caesar cipher.
    
    Args:
        char (str): The character to shift.
        shift_amount (int): The number of positions to shift.
        
    Returns:
        str: The shifted character, preserving case.
    """
    if not char.isalpha():
        return char

    # Determine if uppercase or lowercase
    start = ord('A') if char.isupper() else ord('a')
    shifted = (ord(char) - start + shift_amount) % 26

    return chr(start + shifted)


def caesar_cipher(original_text: str, shift_amount: int, cipher_direction: str) -> str:
    """
    Encodes or decodes a given text using a Caesar cipher.

    This function applies a Caesar cipher to the input string by shifting its 
    alphabetic characters forward (encode) or backward (decode) in accordance 
    with the shift_amount. It maintains the case of alphabetic characters and 
    leaves non-alphabetic characters unchanged.

    Args:
        original_text (str): The input text to encode or decode.
        shift_amount (int): The number of character positions to shift.
        cipher_direction (str): Either "encode"/"e" (shift forward) or 
                              "decode"/"d" (shift backward).

    Returns:
        str: Transformed text.
    """
    normalized_direction = cipher_direction.lower()
    if normalized_direction in {"d", "decode"}:
        shift_amount = -shift_amount
    elif normalized_direction not in {"e", "encode"}:
        raise ValueError("cipher_direction must be 'e'/'encode' or 'd'/'decode'.")

    # Apply Caesar cipher to each character
    output_text = "".join(shift_character(char, shift_amount) for char in original_text)
    return output_text


def get_valid_direction() -> Optional[str]:
    """Get and validate cipher direction from user."""
    valid_directions = {'e', 'encode', 'd', 'decode'}
    while True:
        direction = input("Type letter either 'e' to Encrypt or 'd' to Decrypt:\n===> ").lower()
        if direction in valid_directions:
            return direction
        if direction == '0':
            return None
        print("Invalid input. Please enter 'e'/'encode' or 'd'/'decode'.")


def get_valid_shift() -> int:
    """Get and validate shift amount from user."""
    while True:
        try:
            shift = int(input("\nType the shift number (positive integer):\n"))
            if shift > 0:
                return shift
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main() -> None:
    """Main program loop."""
    print(logo)

    while True:
        direction = get_valid_direction()
        if direction is None:
            print("Goodbye!!")
            break

        text = input("\nType your message:\n")
        shift = get_valid_shift()

        output_text = caesar_cipher(
            original_text=text,
            shift_amount=shift,
            cipher_direction=direction,
        )

        action = "decode" if direction in {"d", "decode"} else "encode"
        print(f"The {action}d result is: {output_text}")

        if (
            input("\nDo you want to continue? Type N or No to exit.\n")
            .strip()
            .lower()
            in {"n", "no"}
        ):
            print("Goodbye!!")
            break


if __name__ == "__main__":
    main()
