def create_cipher_alphabet(keyword):
    """Creates a substitution cipher alphabet based on the given keyword."""
    seen = set()
    keyword_unique = ''.join([char for char in keyword if not (char in seen or seen.add(char))])
    remaining_letters = ''.join([chr(i) for i in range(97, 123) if chr(i) not in keyword_unique])
    cipher_alphabet = keyword_unique + remaining_letters
    if len(cipher_alphabet) != 26:
        raise ValueError("Cipher alphabet must have exactly 26 characters.")
    return cipher_alphabet

def monoalphabetic_cipher(text, cipher_alphabet, mode='encrypt'):
    """Encrypts or decrypts the text using the given cipher alphabet."""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if mode == 'encrypt':
        translation_table = str.maketrans(alphabet, cipher_alphabet)
    elif mode == 'decrypt':
        translation_table = str.maketrans(cipher_alphabet, alphabet)
    result = text.translate(translation_table)
    return result

def main():
    # Input text
    text = input("Enter the text: ").lower()
    # Input keyword for cipher alphabet
    keyword = input("Enter the keyword for the cipher alphabet: ").lower()

    if len(set(keyword)) < 26:
        print("Keyword must contain at least 26 unique characters.")
        return

    # Create cipher alphabet
    cipher_alphabet = create_cipher_alphabet(keyword)

    # Encrypt the text
    encrypted_text = monoalphabetic_cipher(text, cipher_alphabet, mode='encrypt')
    print(f"Encrypted text: {encrypted_text}")

    # Decrypt the text
    decrypted_text = monoalphabetic_cipher(encrypted_text, cipher_alphabet, mode='decrypt')
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
