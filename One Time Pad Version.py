import random
import string

# Function to generate a random key (list of shifts)
def generate_key(length):
    return [random.randint(0, 25) for _ in range(length)]

# Function to encrypt the plaintext
def encrypt_vigenere(plaintext, key):
    encrypted_text = []
    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = key[i]
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)  # Keep non-alphabet characters unchanged
    return ''.join(encrypted_text)

# Function to decrypt the ciphertext
def decrypt_vigenere(ciphertext, key):
    decrypted_text = []
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = key[i]
            base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)  # Keep non-alphabet characters unchanged
    return ''.join(decrypted_text)

def main():
    # Get user input for plaintext
    plaintext = input("Enter the plaintext: ")

    # Generate a random key based on the length of the plaintext
    key = generate_key(len(plaintext))

    print(f"Generated key (shifts): {key}")

    # Encrypt the plaintext
    ciphertext = encrypt_vigenere(plaintext, key)
    print(f"Encrypted text: {ciphertext}")

    # Decrypt the ciphertext
    decrypted_text = decrypt_vigenere(ciphertext, key)
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
