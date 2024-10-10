import random

CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

"""
Function to generate a Caesar cipher for a given input string.
Args:
    key: int - The number of positions to shift the characters by.
    input_string: str - The input string to generate the cipher for.
Returns:
    str - The generated cipher with spaces and case sensitivity preserved.
"""
def generate_cipher(input_string: str, key: int) -> str:
    cipher = ""
    for char in input_string:
        if char.isalpha():
            if char.isupper():
                cipher += CHARACTERS[(CHARACTERS.index(char) + key) % 26]
            else:
                cipher += CHARACTERS[(CHARACTERS.index(char.upper()) + key) % 26].lower()
        else:
            cipher += char
    return cipher

def main():
    key = input("Enter the key to shift the characters by: ")
    if not key or not key.isdigit():
        key = random.randint(1, 25)
        print(f"No key provided, using random key {key}")
    else:
        key = int(key)
    input_string = input("Enter the string to generate the cipher for: ")
    print(f"The generated cipher is: {generate_cipher(input_string, key)}")

if __name__ == "__main__":
    main()
