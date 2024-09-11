import string
import math

# Function to check if 'a' is coprime with 26
def is_coprime(a):
    return math.gcd(a, 26) == 1

# Function to find modular inverse of a under mod 26
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"No modular inverse for a={a} under mod {m}.")

# Function to encrypt the plaintext using affine Caesar cipher
def affine_encrypt(plaintext, a, b):
    if not is_coprime(a):
        raise ValueError(f"The value of 'a' must be coprime with 26. {a} is not coprime with 26.")
    
    encrypted_text = []
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            p = ord(char) - base
            # Apply the affine cipher: (a * p + b) % 26
            C = (a * p + b) % 26
            encrypted_text.append(chr(C + base))
        else:
            encrypted_text.append(char)  # Non-alphabet characters remain unchanged
    return ''.join(encrypted_text)

# Function to decrypt the ciphertext using affine Caesar cipher
def affine_decrypt(ciphertext, a, b):
    if not is_coprime(a):
        raise ValueError(f"The value of 'a' must be coprime with 26. {a} is not coprime with 26.")
    
    decrypted_text = []
    mod_inv_a = mod_inverse(a, 26)
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            C = ord(char) - base
            # Apply the decryption formula: mod_inv_a * (C - b) % 26
            p = (mod_inv_a * (C - b)) % 26
            decrypted_text.append(chr(p + base))
        else:
            decrypted_text.append(char)  # Non-alphabet characters remain unchanged
    return ''.join(decrypted_text)

def main():
    # Get user input for plaintext, a, and b
    plaintext = input("Enter the plaintext: ")
    a = int(input("Enter the value of a (must be coprime with 26): "))
    b = int(input("Enter the value of b: "))

    # Encrypt the plaintext
    try:
        ciphertext = affine_encrypt(plaintext, a, b)
        print(f"Encrypted text: {ciphertext}")

        # Decrypt the ciphertext
        decrypted_text = affine_decrypt(ciphertext, a, b)
        print(f"Decrypted text: {decrypted_text}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
