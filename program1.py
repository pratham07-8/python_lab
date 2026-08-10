import sys


def caesar_cipher(text, shift, mode):
    result = ""

    if mode == "decode":
        shift = -shift

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


# Take input from command line if provided
if len(sys.argv) >= 3:
    text = sys.argv[1]
    shift = sys.argv[2]

    if len(sys.argv) >= 4:
        mode = sys.argv[3].lower()
    else:
        mode = "encode"

else:
    text = input("Enter the text: ")
    shift = input("Enter shift key: ")
    mode = input("Enter mode (encode/decode): ").lower()


# Validate shift key
if not shift.lstrip("-").isdigit():
    print("Error: Shift key must be an integer.")
    sys.exit(1)

shift = int(shift)

# Validate mode
if mode not in ("encode", "decode"):
    print("Error: Mode must be 'encode' or 'decode'.")
    sys.exit(1)

# Perform cipher
result = caesar_cipher(text, shift, mode)

print("\nOriginal Text :", text)
print("Shift Key     :", shift)
print("Mode          :", mode)
print("Result        :", result)