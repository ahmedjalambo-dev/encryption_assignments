# Name: Ahmed Marwan Omer Jalambo
# ID: 2049011002
def caesar_encrypt(plaintext, shift):
    """
    Encrypts plaintext using Caesar cipher with the given shift value.

    Args:
        plaintext: The text to encrypt
        shift: The number of positions to shift (positive integer)

    Returns:
        The encrypted ciphertext
    """
    ciphertext = ""

    for char in plaintext:
        if char.isalpha():
            # Determine if uppercase or lowercase
            start = ord("A") if char.isupper() else ord("a")
            # Shift the character and wrap around using modulo
            shifted = (ord(char) - start + shift) % 26
            ciphertext += chr(start + shifted)
        else:
            # Keep non-alphabetic characters unchanged
            ciphertext += char

    return ciphertext


def caesar_decrypt(ciphertext, shift):
    """
    Decrypts ciphertext using Caesar cipher with the given shift value.

    Args:
        ciphertext: The text to decrypt
        shift: The number of positions that were shifted during encryption

    Returns:
        The decrypted plaintext
    """
    # Decryption is just encryption with negative shift
    return caesar_encrypt(ciphertext, -shift)


def main():
    print("=== Caesar Cipher ===\n")

    # Get user choice
    choice = input("Choose operation:\n1. Encrypt\n2. Decrypt\nEnter choice (1/2): ")

    if choice not in ["1", "2"]:
        print("Invalid choice!")
        return

    # Get input text
    text = input("\nEnter text: ")

    # Get shift value
    try:
        shift = int(input("Enter shift value (0-25): "))
        if shift < 0 or shift > 25:
            print("Shift value must be between 0 and 25!")
            return
    except ValueError:
        print("Invalid shift value! Please enter a number.")
        return

    # Perform operation
    if choice == "1":
        result = caesar_encrypt(text, shift)
        print(f"\nPlaintext:  {text}")
        print(f"Ciphertext: {result}")
    else:
        result = caesar_decrypt(text, shift)
        print(f"\nCiphertext: {text}")
        print(f"Plaintext:  {result}")


if __name__ == "__main__":
    main()
