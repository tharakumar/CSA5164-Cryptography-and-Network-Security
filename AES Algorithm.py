from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

class AESCipher:
    def __init__(self, key: bytes):
        self.key = key
        self.block_size = AES.block_size

    # Encrypt the plaintext using AES
    def encrypt(self, plaintext: bytes) -> bytes:
        # Create a random Initialization Vector (IV) for AES encryption
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        padded_plaintext = pad(plaintext, self.block_size)
        ciphertext = iv + cipher.encrypt(padded_plaintext)  # Prepend IV to ciphertext
        return ciphertext

    # Decrypt the ciphertext using AES
    def decrypt(self, ciphertext: bytes) -> bytes:
        # Extract the IV from the beginning of the ciphertext
        iv = ciphertext[:AES.block_size]
        actual_ciphertext = ciphertext[AES.block_size:]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted_padded = cipher.decrypt(actual_ciphertext)
        plaintext = unpad(decrypted_padded, self.block_size)
        return plaintext

# Example usage
if __name__ == "__main__":
    # User C creates an AES cipher with a 16-byte key
    key = b'sixteenbytekey12'  # AES-128 requires the key to be exactly 16 bytes
    aes_cipher = AESCipher(key)

    # User C's plaintext message
    message = b"welcome to CSE"

    # User C encrypts the message
    encrypted_message = aes_cipher.encrypt(message)
    print("Encrypted message (sent by User C):", encrypted_message)

    # User D decrypts the message upon receiving it
    decrypted_message = aes_cipher.decrypt(encrypted_message)
    print("Decrypted message (received by User D):", decrypted_message.decode())
