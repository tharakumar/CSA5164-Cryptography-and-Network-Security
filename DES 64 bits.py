from pyDes import des, CBC, PAD_PKCS5
import binascii

def des_encrypt(plaintext, key):
    # Ensure the key is exactly 8 bytes (64 bits) by padding if necessary
    if len(key) < 8:
        key = key.ljust(8, '0')  # Pad with '0' to make it 8 bytes

    # Convert the key and plaintext to bytes
    key_bytes = key.encode('utf-8')
    plaintext_bytes = plaintext.encode('utf-8')

    # DES encryption requires a 64-bit key (8 bytes) and a block size of 8 bytes
    des_cipher = des(key_bytes, CBC, b"12345678", pad=None, padmode=PAD_PKCS5)
    
    # Encrypt plaintext
    encrypted_bytes = des_cipher.encrypt(plaintext_bytes)
    encrypted_hex = binascii.hexlify(encrypted_bytes).decode('utf-8')

    return encrypted_hex

def des_decrypt(ciphertext_hex, key):
    # Ensure the key is exactly 8 bytes (64 bits) by padding if necessary
    if len(key) < 8:
        key = key.ljust(8, '0')  # Pad with '0' to make it 8 bytes
    
    # Convert the key to bytes
    key_bytes = key.encode('utf-8')
    
    # Convert the ciphertext from hex to bytes
    ciphertext_bytes = binascii.unhexlify(ciphertext_hex)
    
    # DES decryption requires the same key and initialization vector
    des_cipher = des(key_bytes, CBC, b"12345678", pad=None, padmode=PAD_PKCS5)
    
    # Decrypt ciphertext
    decrypted_bytes = des_cipher.decrypt(ciphertext_bytes)
    decrypted_text = decrypted_bytes.decode('utf-8')

    return decrypted_text

def main():
    # Get user input for plaintext and key
    plaintext = input("Enter a 64-bit block of plaintext (8 characters): ")
    key = input("Enter a 56-bit key (7 characters): ")

    if len(plaintext) != 8 or len(key) != 7:
        print("Error: Plaintext must be 8 characters and key must be 7 characters long.")
        return

    # Encrypt the plaintext
    encrypted_text = des_encrypt(plaintext, key)
    print(f"Encrypted Ciphertext: {encrypted_text}")

    # Decrypt the ciphertext
    decrypted_text = des_decrypt(encrypted_text, key)
    print(f"Decrypted Text: {decrypted_text}")

if __name__ == "__main__":
    main()
