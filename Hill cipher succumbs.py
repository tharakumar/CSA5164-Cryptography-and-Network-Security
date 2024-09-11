import numpy as np

# Convert a letter to its corresponding number (A=0, B=1, ..., Z=25)
def letter_to_num(letter):
    return ord(letter.upper()) - ord('A')

# Convert a number to its corresponding letter (0=A, 1=B, ..., 25=Z)
def num_to_letter(num):
    return chr(num + ord('A'))

# Function to encrypt a block of text using the Hill cipher
def hill_encrypt(plaintext_block, key_matrix):
    # Convert the plaintext block to a vector
    plaintext_vector = np.array([letter_to_num(c) for c in plaintext_block])
    
    # Perform matrix multiplication and take modulo 26
    ciphertext_vector = np.dot(key_matrix, plaintext_vector) % 26
    
    # Convert the resulting vector back to letters
    ciphertext = ''.join(num_to_letter(num) for num in ciphertext_vector)
    return ciphertext

# Function to decrypt a block of text using the Hill cipher
def hill_decrypt(ciphertext_block, key_matrix):
    # Calculate the inverse of the key matrix modulo 26
    det = int(np.round(np.linalg.det(key_matrix))) % 26
    if np.gcd(det, 26) != 1:
        raise ValueError(f"The determinant {det} is not invertible modulo 26")
    
    det_inv = pow(det, -1, 26)  # Modular inverse of determinant modulo 26
    key_matrix_inv = np.round(det_inv * np.linalg.inv(key_matrix) * det).astype(int) % 26

    # Convert the ciphertext block to a vector
    ciphertext_vector = np.array([letter_to_num(c) for c in ciphertext_block])
    
    # Perform matrix multiplication with the inverse key and take modulo 26
    plaintext_vector = np.dot(key_matrix_inv, ciphertext_vector) % 26
    
    # Convert the resulting vector back to letters
    plaintext = ''.join(num_to_letter(num) for num in plaintext_vector)
    return plaintext

# Function to find the encryption matrix using known plaintext and ciphertext pairs
def find_encryption_matrix(plaintext_pairs, ciphertext_pairs):
    # Convert plaintext and ciphertext pairs to numerical matrices
    plaintext_matrix = np.array([[letter_to_num(c) for c in block] for block in plaintext_pairs])
    ciphertext_matrix = np.array([[letter_to_num(c) for c in block] for block in ciphertext_pairs])
    
    # Find the determinant of the plaintext matrix and check invertibility
    det = int(np.round(np.linalg.det(plaintext_matrix))) % 26
    if np.gcd(det, 26) != 1:
        raise ValueError(f"The determinant {det} of the plaintext matrix is not invertible modulo 26")
    
    # Find the inverse of the plaintext matrix modulo 26
    det_inv = pow(det, -1, 26)  # Modular inverse of determinant modulo 26
    plaintext_matrix_inv = np.round(det_inv * np.linalg.inv(plaintext_matrix) * det).astype(int) % 26
    
    # Multiply ciphertext matrix by the inverse of the plaintext matrix to find the key
    key_matrix = np.dot(ciphertext_matrix, plaintext_matrix_inv) % 26
    return key_matrix

def main():
    # Example known plaintext and ciphertext pairs (for a 2x2 Hill cipher)
    plaintext_pairs = ["HI", "BY"]
    ciphertext_pairs = ["KM", "ZR"]

    try:
        # Find the encryption matrix using known plaintext-ciphertext pairs
        key_matrix = find_encryption_matrix(plaintext_pairs, ciphertext_pairs)
        
        print("Recovered encryption matrix:")
        print(key_matrix)

        # Test encryption and decryption
        plaintext = "HI"
        print(f"Plaintext: {plaintext}")
        ciphertext = hill_encrypt(plaintext, key_matrix)
        print(f"Encrypted: {ciphertext}")
        
        decrypted_text = hill_decrypt(ciphertext, key_matrix)
        print(f"Decrypted: {decrypted_text}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
