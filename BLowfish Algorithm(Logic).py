import warnings
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

# Suppress CryptographyDeprecationWarning for Blowfish
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Blowfish encryption class
class BlowfishCipher:
    def __init__(self, key: bytes):
        self.key = key
        self.backend = default_backend()
        # Blowfish requires a block size of 8 bytes
        self.block_size = 8

    # Method to pad plaintext data to make it a multiple of the block size
    def pad(self, data: bytes) -> bytes:
        padder = padding.PKCS7(self.block_size * 8).padder()
        return padder.update(data) + padder.finalize()

    # Method to unpad the decrypted data
    def unpad(self, padded_data: bytes) -> bytes:
        unpadder = padding.PKCS7(self.block_size * 8).unpadder()
        return unpadder.update(padded_data) + unpadder.finalize()

    # Encrypt the given plaintext using Blowfish in ECB mode
    def encrypt(self, plaintext: bytes) -> bytes:
        cipher = Cipher(algorithms.Blowfish(self.key), modes.ECB(), backend=self.backend)
        encryptor = cipher.encryptor()
        padded_plaintext = self.pad(plaintext)
        ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
        return ciphertext

    # Decrypt the given ciphertext using Blowfish in ECB mode
    def decrypt(self, ciphertext: bytes) -> bytes:
        cipher = Cipher(algorithms.Blowfish(self.key), modes.ECB(), backend=self.backend)
        decryptor = cipher.decryptor()
        decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()
        return self.unpad(decrypted_padded)

# Example usage
if __name__ == "__main__":
    key = b'YourKey16Bytes'  # Blowfish keys can be up to 56 bytes long
    plaintext = b"Hello, Blowfish!"

    # Create a Blowfish cipher object
    blowfish_cipher = BlowfishCipher(key)

    # Encrypt the plaintext
    encrypted_data = blowfish_cipher.encrypt(plaintext)
    print("Encrypted:", encrypted_data)

    # Decrypt the ciphertext
    decrypted_data = blowfish_cipher.decrypt(encrypted_data)
    print("Decrypted:", decrypted_data.decode())
