import numpy as np

def mod_inverse(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, modulus)
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    return (det_inv * adjugate) % modulus

def hill_encrypt(plaintext, key_matrix):
    n = len(key_matrix)
    plaintext_vector = [ord(char) - 65 for char in plaintext]
    plaintext_vector = np.array(plaintext_vector).reshape(-1, n).T
    encrypted_vector = (key_matrix @ plaintext_vector) % 26
    return ''.join(chr(int(num) + 65) for num in encrypted_vector.T.flatten())

def hill_decrypt(ciphertext, key_matrix):
    n = len(key_matrix)
    ciphertext_vector = [ord(char) - 65 for char in ciphertext]
    ciphertext_vector = np.array(ciphertext_vector).reshape(-1, n).T
    inverse_key_matrix = mod_inverse(key_matrix, 26)
    decrypted_vector = (inverse_key_matrix @ ciphertext_vector) % 26
    return ''.join(chr(int(num) + 65) for num in decrypted_vector.T.flatten())

key_size = int(input("Enter key matrix size (e.g., 2 for 2x2 matrix): "))
key_matrix = []
for i in range(key_size):
    row = list(map(int, input(f"Enter row {i + 1} of key matrix: ").split()))
    key_matrix.append(row)
key_matrix = np.array(key_matrix)

plaintext = input("Enter plaintext (in uppercase, length multiple of key size): ")
ciphertext = hill_encrypt(plaintext, key_matrix)
decrypted_text = hill_decrypt(ciphertext, key_matrix)

print(f"Encrypted ciphertext: {ciphertext}")
print(f"Decrypted plaintext: {decrypted_text}")
