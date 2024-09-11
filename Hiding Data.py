def caesar_cipher_encrypt(plaintext, shift):
    """Encrypts plaintext using Caesar cipher with the given shift."""
    encrypted_text = []
    for char in plaintext:
        if char.isalpha():  # Check if character is a letter
            shift_amount = shift % 26
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift_amount) % 26 + base)
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)  # Non-alphabet characters are not encrypted
    return ''.join(encrypted_text)

def caesar_cipher_decrypt(ciphertext, shift):
    """Decrypts ciphertext using Caesar cipher with the given shift."""
    return caesar_cipher_encrypt(ciphertext, -shift)

def main():
    plaintext = input("Enter the plaintext: ")
    shift = int(input("Enter the shift value (integer): "))
    
    encrypted = caesar_cipher_encrypt(plaintext, shift)
    print(f'Encrypted text: {encrypted}')
    
    decrypted = caesar_cipher_decrypt(encrypted, shift)
    print(f'Decrypted text: {decrypted}')

if __name__ == "__main__":
    main()
