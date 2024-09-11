def encrypt_caesar(plaintext, shift):
    encrypted_message = ""
    for char in plaintext:
        if char.isalpha():  # Check if character is a letter
            shift_base = ord('a') if char.islower() else ord('A')
            encrypted_message += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_message += char  # Non-alphabetic characters remain unchanged
    return encrypted_message

def decrypt_caesar(ciphertext, shift):
    decrypted_message = ""
    for char in ciphertext:
        if char.isalpha():  # Check if character is a letter
            shift_base = ord('a') if char.islower() else ord('A')
            decrypted_message += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_message += char  # Non-alphabetic characters remain unchanged
    return decrypted_message

# Example usage
if __name__ == "__main__":
    message = "defend the east wall of the castle"
    shift = 1

    # Encrypt the message
    encrypted_message = encrypt_caesar(message, shift)
    print("Encrypted message:", encrypted_message)

    # Decrypt the message
    decrypted_message = decrypt_caesar(encrypted_message, shift)
    print("Decrypted message:", decrypted_message)
