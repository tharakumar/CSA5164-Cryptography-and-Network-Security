from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
import binascii

def encrypt_blowfish(plaintext, key):
    cipher = Blowfish.new(key, Blowfish.MODE_CBC)
    # Pad plaintext to be multiple of 8 bytes
    padded_plaintext = pad(plaintext.encode(), Blowfish.block_size)
    # Encrypt the plaintext
    ciphertext = cipher.encrypt(padded_plaintext)
    # Return the IV and ciphertext combined
    return cipher.iv + ciphertext

def decrypt_blowfish(ciphertext_with_iv, key):
    iv = ciphertext_with_iv[:Blowfish.block_size]
    ciphertext = ciphertext_with_iv[Blowfish.block_size:]
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    # Decrypt the ciphertext
    padded_plaintext = cipher.decrypt(ciphertext)
    # Unpad plaintext
    plaintext = unpad(padded_plaintext, Blowfish.block_size)
    return plaintext.decode()

def main():
    # Example key (must be between 1 and 56 bytes for Blowfish)
    key = b'secret_key_1234'
    
    # Example plaintext
    plaintext = 'This is a test message.'
    
    # Encrypt the plaintext
    encrypted = encrypt_blowfish(plaintext, key)
    print(f'Encrypted (hex): {binascii.hexlify(encrypted).decode()}')
    
    # Decrypt the ciphertext
    decrypted = decrypt_blowfish(encrypted, key)
    print(f'Decrypted: {decrypted}')

if __name__ == "__main__":
    main()
