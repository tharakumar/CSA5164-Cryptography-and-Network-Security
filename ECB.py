from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def encrypt_des_ecb(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plaintext = pad(plaintext, DES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def decrypt_des_ecb(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext, DES.block_size)
    return plaintext

def main():
    key = b'12345678'  # 8-byte key for DES
    
    # User input for plaintext
    plaintext = input("Enter plaintext: ").encode()
    
    # Perform encryption
    ciphertext = encrypt_des_ecb(key, plaintext)
    
    # Perform decryption
    decrypted = decrypt_des_ecb(key, ciphertext)

    # Output ciphertext and decrypted plaintext in hex format
    print(f"Ciphertext: {ciphertext.hex()}")
    print(f"Decrypted plaintext: {decrypted.decode()}")

if __name__ == "__main__":
    main()
