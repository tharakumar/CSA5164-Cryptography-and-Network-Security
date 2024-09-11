from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
import binascii

def encrypt_3des(plaintext, key):
    # Ensure the key length is 24 bytes for 3DES (3 * 8 bytes)
    if len(key) not in [16, 24]:
        raise ValueError("Key must be either 16 or 24 bytes long")
    
    # Create a Triple DES cipher object
    cipher = DES3.new(key, DES3.MODE_CBC)
    
    # Pad plaintext to be a multiple of 8 bytes
    padded_plaintext = pad(plaintext.encode(), DES3.block_size)
    
    # Encrypt the plaintext
    ciphertext = cipher.encrypt(padded_plaintext)
    
    # Return the IV and ciphertext combined
    return cipher.iv + ciphertext

def decrypt_3des(ciphertext_with_iv, key):
    # Extract the IV from the beginning of the ciphertext
    iv = ciphertext_with_iv[:DES3.block_size]
    ciphertext = ciphertext_with_iv[DES3.block_size:]
    
    # Create a Triple DES cipher object with the extracted IV
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    
    # Decrypt the ciphertext
    padded_plaintext = cipher.decrypt(ciphertext)
    
    # Unpad plaintext
    plaintext = unpad(padded_plaintext, DES3.block_size)
    return plaintext.decode()

def main():
    # Example key (must be either 16 or 24 bytes long for 3DES)
    key = b'123456789012345678901234'  # 24 bytes key (3 * 8 bytes)
    
    # Example plaintext
    plaintext = 'This is a test message.'
    
    # Encrypt the plaintext
    encrypted = encrypt_3des(plaintext, key)
    print(f'Encrypted (hex): {binascii.hexlify(encrypted).decode()}')
    
    # Decrypt the ciphertext
    decrypted = decrypt_3des(encrypted, key)
    print(f'Decrypted: {decrypted}')

if __name__ == "__main__":
    main()
