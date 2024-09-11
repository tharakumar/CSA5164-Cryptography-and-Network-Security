import random
from math import gcd
from sympy import mod_inverse, isprime

# Function to compute modular exponentiation
def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

# Function to generate large prime numbers
def generate_prime(bits=512):
    prime = 4
    while not isprime(prime):
        prime = random.getrandbits(bits)
    return prime

# Function to generate RSA keys
def generate_rsa_keys():
    # Generate two large primes p and q
    p = generate_prime(512)
    q = generate_prime(512)
    
    # Compute n = p * q
    n = p * q
    
    # Compute Euler's totient function phi(n) = (p-1) * (q-1)
    phi_n = (p - 1) * (q - 1)
    
    # Choose e such that 1 < e < phi(n) and gcd(e, phi_n) = 1
    e = random.randint(2, phi_n - 1)
    while gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)
    
    # Compute the private key d as the modular inverse of e modulo phi(n)
    d = mod_inverse(e, phi_n)
    
    return (e, d, n)

# Helper functions for converting between bytes and integers
def text_to_int(plaintext):
    # Apply padding before converting text to integer
    padded_text = plaintext + '|PAD|'  # Using a unique delimiter for padding
    return int.from_bytes(padded_text.encode('utf-8'), byteorder='big')

def int_to_text(cipher_int):
    byte_length = (cipher_int.bit_length() + 7) // 8
    decrypted_bytes = cipher_int.to_bytes(byte_length, byteorder='big')
    
    try:
        # Decode and remove padding
        decrypted_text = decrypted_bytes.decode('utf-8')
        if '|PAD|' in decrypted_text:
            return decrypted_text.split('|PAD|')[0]
        else:
            return decrypted_text
    except UnicodeDecodeError as e:
        print(f"Error decoding text: {e}")
        return None

# Encryption function
def encrypt(plaintext, e, n):
    # Convert plaintext to an integer
    plaintext_int = text_to_int(plaintext)
    # Encrypt using RSA formula: ciphertext = (plaintext^e) mod n
    ciphertext = mod_exp(plaintext_int, e, n)
    return ciphertext

# Decryption function
def decrypt(ciphertext, d, n):
    # Decrypt using RSA formula: plaintext = (ciphertext^d) mod n
    decrypted_int = mod_exp(ciphertext, d, n)
    # Convert the integer back to text
    plaintext = int_to_text(decrypted_int)
    return plaintext

# Main function
def main():
    print("Generating RSA keys for Bob...")
    (e, d, n) = generate_rsa_keys()  # Initial key generation
    
    print(f"Bob's Public Key (e, n): ({e}, {n})")
    print(f"Bob's Private Key (d, n): ({d}, {n})")
    
    # Input plaintext
    plaintext = input("\nEnter the plaintext message to be encrypted: ")
    
    # Encrypt the plaintext using Bob's public key
    ciphertext = encrypt(plaintext, e, n)
    print(f"\nEncrypted ciphertext (as integer): {ciphertext}")
    
    # Simulate Bob leaking his private key
    print("\nOops! Bob's private key has been leaked!")
    
    # Regenerate the entire RSA key pair (including a new modulus)
    print("Bob regenerates a completely new key pair.")
    new_e, new_d, new_n = generate_rsa_keys()  # Generate new e, d, and n
    
    print(f"\nBob's New Public Key (e, n): ({new_e}, {new_n})")
    print(f"Bob's New Private Key (d, n): ({new_d}, {new_n})")
    
    # Decrypt using Bob's new private key
    try:
        decrypted_text = decrypt(ciphertext, new_d, new_n)
        if decrypted_text:
            print(f"\nDecrypted text with new private key: {decrypted_text}")
        else:
            print("\nDecryption failed. Decoded text is invalid.")
    except Exception as e:
        print(f"\nError during decryption: {e}")

    # Check if the decrypted text matches the original plaintext
    if decrypted_text == plaintext:
        print("\nDecryption successful with the new private key!")
    else:
        print("\nDecryption failed with the new private key!")

if __name__ == "__main__":
    main()
