from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

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

def encrypt_des_cbc(key, iv, plaintext):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    padded_plaintext = pad(plaintext, DES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def decrypt_des_cbc(key, iv, ciphertext):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext, DES.block_size)
    return plaintext

def encrypt_des_cfb(key, iv, plaintext):
    cipher = DES.new(key, DES.MODE_CFB, iv)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def decrypt_des_cfb(key, iv, ciphertext):
    cipher = DES.new(key, DES.MODE_CFB, iv)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def main():
    key = b'12345678'  # 8-byte key for DES
    iv = get_random_bytes(DES.block_size)  # Random 8-byte IV for CBC and CFB
    
    # User input for plaintext
    plaintext = input("Enter plaintext: ").encode()
    
    # Padding plaintext to be a multiple of block size
    padded_plaintext = pad(plaintext, DES.block_size)
    
    # Perform encryption and decryption in ECB mode
    ecb_ciphertext = encrypt_des_ecb(key, padded_plaintext)
    ecb_decrypted = decrypt_des_ecb(key, ecb_ciphertext)
    
    print("ECB Mode:")
    print(f"Ciphertext: {ecb_ciphertext.hex()}")
    print(f"Decrypted plaintext: {ecb_decrypted.decode()}")

    # Perform encryption and decryption in CBC mode
    cbc_ciphertext = encrypt_des_cbc(key, iv, padded_plaintext)
    cbc_decrypted = decrypt_des_cbc(key, iv, cbc_ciphertext)
    
    print("CBC Mode:")
    print(f"Ciphertext: {cbc_ciphertext.hex()}")
    print(f"Decrypted plaintext: {cbc_decrypted.decode()}")

    # Perform encryption and decryption in CFB mode
    cfb_ciphertext = encrypt_des_cfb(key, iv, padded_plaintext)
    cfb_decrypted = decrypt_des_cfb(key, iv, cfb_ciphertext)
    
    print("CFB Mode:")
    print(f"Ciphertext: {cfb_ciphertext.hex()}")
    print(f"Decrypted plaintext: {cfb_decrypted.decode()}")

if __name__ == "__main__":
    main()
