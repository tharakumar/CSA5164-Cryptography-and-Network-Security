def generate_key(text, key):
    """Generate a key by repeating or truncating the original key to match the text length."""
    key = list(key)
    if len(text) == len(key):
        return "".join(key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def vigenere_cipher(text, key, mode='encrypt'):
    """Encrypt or decrypt the text using the Vigenère cipher."""
    result = []
    key = generate_key(text, key)
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            shift = ord(key[i].lower()) - 97  # Convert key char to lower and calculate shift
            if mode == 'encrypt':
                if char.isupper():
                    result.append(chr((ord(char) + shift - 65) % 26 + 65))
                else:
                    result.append(chr((ord(char) + shift - 97) % 26 + 97))
            elif mode == 'decrypt':
                if char.isupper():
                    result.append(chr((ord(char) - shift - 65) % 26 + 65))
                else:
                    result.append(chr((ord(char) - shift - 97) % 26 + 97))
        else:
            result.append(char)  # Non-alphabet characters remain unchanged
    return "".join(result)

def main():
    # Input text
    text = input("Enter the text: ")
    # Input key
    key = input("Enter the key: ")

    # Encrypt the text
    encrypted_text = vigenere_cipher(text, key, mode='encrypt')
    print(f"Encrypted text: {encrypted_text}")

    # Decrypt the text
    decrypted_text = vigenere_cipher(encrypted_text, key, mode='decrypt')
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
