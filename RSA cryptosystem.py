import sympy
import random

# Function to compute GCD
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to compute modular inverse
def mod_inverse(e, phi):
    return pow(e, -1, phi)

# RSA Key Generation with large primes
def generate_keys():
    # Generate large prime numbers p and q
    print("Generating RSA keys with large modulus (n):")
    p = sympy.randprime(1000, 5000)
    q = sympy.randprime(1000, 5000)

    n = p * q
    phi = (p - 1) * (q - 1)

    # Public key 'e' generation (choosing large e)
    e = random.randrange(100, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(100, phi)

    # Private key 'd' calculation
    d = mod_inverse(e, phi)

    print(f"Public key (e, n): ({e}, {n})")
    print(f"Private key (d, n): ({d}, {n})")

    return (e, n), (d, n)

# Mapping characters to numbers (A=0, ..., Z=25)
def char_to_num(char):
    return ord(char.upper()) - ord('A')

# Mapping numbers back to characters
def num_to_char(num):
    return chr(num + ord('A'))

# RSA Encryption
def encrypt_char(char, public_key):
    num = char_to_num(char)
    e, n = public_key
    return pow(num, e, n)

# RSA Decryption
def decrypt_num(num, private_key):
    d, n = private_key
    decrypted_num = pow(num, d, n)
    return num_to_char(decrypted_num)

# Main function to demonstrate the RSA encryption and decryption process
def main():
    # Step 1: Generate RSA keys
    public_key, private_key = generate_keys()

    # Step 2: Get the message from the user (characters A-Z)
    message = input("Enter the message to encrypt (A-Z): ").upper()

    # Step 3: Encrypt the message
    cipher_text = [encrypt_char(char, public_key) for char in message]
    print(f"Encrypted message: {cipher_text}")

    # Step 4: Decrypt the message
    decrypted_message = ''.join([decrypt_num(num, private_key) for num in cipher_text])
    print(f"Decrypted message: {decrypted_message}")

# Run the RSA encryption scheme
if __name__ == "__main__":
    main()
