from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_3des_cbc(key, iv, plaintext):
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    padded_plaintext = pad(plaintext, DES3.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def main():
    key = b'0123456789abcdef01234567'  # 24-byte key for 3DES
    iv = get_random_bytes(DES3.block_size)  # Random 8-byte IV
    
    # User input for plaintext
    plaintext = input("Enter plaintext: ").encode()
    
    # Perform encryption
    ciphertext = encrypt_3des_cbc(key, iv, plaintext)

    # Output IV and ciphertext in hex format
    print(f"IV: {iv.hex()}")
    print(f"Ciphertext: {ciphertext.hex()}")

if __name__ == "__main__":
    main()
