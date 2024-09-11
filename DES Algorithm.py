from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

class DESCipher:
    def __init__(self, key: bytes):
        self.key = key
        self.block_size = DES.block_size

    # Encrypt the plaintext using DES
    def encrypt(self, plaintext: bytes) -> bytes:
        cipher = DES.new(self.key, DES.MODE_ECB)
        padded_plaintext = pad(plaintext, self.block_size)
        ciphertext = cipher.encrypt(padded_plaintext)
        return ciphertext

    # Decrypt the ciphertext using DES
    def decrypt(self, ciphertext: bytes) -> bytes:
        cipher = DES.new(self.key, DES.MODE_ECB)
        decrypted_padded = cipher.decrypt(ciphertext)
        plaintext = unpad(decrypted_padded, self.block_size)
        return plaintext

# Example usage
if __name__ == "__main__":
    # User A creates a DES cipher with a 8-byte key
    key = b'8bytekey'  # DES requires the key to be exactly 8 bytes
    des_cipher = DESCipher(key)

    # User A's plaintext message
    message = b"Meet me very urgently"

    # User A encrypts the message
    encrypted_message = des_cipher.encrypt(message)
    print("Encrypted message (sent by User A):", encrypted_message)

    # Receiver decrypts the message before forwarding to User B
    decrypted_message = des_cipher.decrypt(encrypted_message)
    print("Decrypted message (received by Receiver):", decrypted_message.decode())

    # Now the decrypted message can be sent to User B
