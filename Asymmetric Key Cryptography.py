from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

# Step 1: User B generates RSA public and private keys
def generate_rsa_keypair():
    key = RSA.generate(2048)  # Generate a 2048-bit RSA key pair
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# Step 2: User A encrypts the message using User B's public key
def encrypt_message(public_key, message):
    rsa_key = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(rsa_key)
    ciphertext = cipher_rsa.encrypt(message)
    return ciphertext

# Step 3: User B decrypts the message using their private key
def decrypt_message(private_key, ciphertext):
    rsa_key = RSA.import_key(private_key)
    cipher_rsa = PKCS1_OAEP.new(rsa_key)
    plaintext = cipher_rsa.decrypt(ciphertext)
    return plaintext

# Example usage
if __name__ == "__main__":
    # User B generates RSA keys
    private_key, public_key = generate_rsa_keypair()
    
    # Display the generated keys
    print("User B's Private Key:", private_key.decode())
    print("User B's Public Key:", public_key.decode())

    # User A's plaintext message
    message = b"Hello, User B! This is a secure message."

    # User A encrypts the message using User B's public key
    encrypted_message = encrypt_message(public_key, message)
    print("\nEncrypted message (sent by User A):", encrypted_message)

    # User B decrypts the message using their private key
    decrypted_message = decrypt_message(private_key, encrypted_message)
    print("\nDecrypted message (received by User B):", decrypted_message.decode())
