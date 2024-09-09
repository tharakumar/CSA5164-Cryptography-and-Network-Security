import binascii

# Initial Permutation (IP) table
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# Final Permutation (FP) table
FP = [40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41, 9, 49, 17, 57, 25]

# Key schedule shift values
SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# Permuted Choice 1 (PC1) table
PC1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]

# Permuted Choice 2 (PC2) table
PC2 = [14, 17, 11, 24, 1, 5, 3, 28,
       15, 6, 21, 10, 23, 19, 12, 4,
       26, 8, 16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55, 30, 40,
       51, 45, 33, 48, 44, 49, 39, 56,
       34, 53, 46, 42, 50, 36, 29, 32]

# Expansion permutation table
EXPANSION = [32, 1, 2, 3, 4, 5,
             4, 5, 6, 7, 8, 9,
             8, 9, 10, 11, 12, 13,
             12, 13, 14, 15, 16, 17,
             16, 17, 18, 19, 20, 21,
             20, 21, 22, 23, 24, 25,
             24, 25, 26, 27, 28, 29,
             28, 29, 30, 31, 32, 1]

# S-Box example (you'll need all 8 S-Boxes in practice)
SBOX = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
]

# Permutation function for arbitrary tables
def permute(block, table):
    return ''.join([block[i - 1] for i in table])

# Left circular shift function
def left_shift(bits, shift_amount):
    return bits[shift_amount:] + bits[:shift_amount]

# Generate the round keys in reverse for decryption
def generate_reverse_keys(key):
    key = permute(key, PC1)
    C, D = key[:28], key[28:]
    round_keys = []

    for shift in SHIFT_SCHEDULE:
        C = left_shift(C, shift)
        D = left_shift(D, shift)
        combined_key = C + D
        round_key = permute(combined_key, PC2)
        round_keys.append(round_key)

    return round_keys[::-1]  # Reverse the keys for decryption

# DES Decryption
def des_decrypt(ciphertext, key):
    # Generate reverse round keys
    round_keys = generate_reverse_keys(key)
    
    # Apply initial permutation
    ciphertext = permute(ciphertext, IP)

    # Split into left and right halves
    L, R = ciphertext[:32], ciphertext[32:]

    # 16 rounds of decryption
    for i in range(16):
        old_R = R
        R = permute(R, EXPANSION)
        R = bin(int(R, 2) ^ int(round_keys[i], 2))[2:].zfill(48)

        # Simplified S-Box substitution (use all S-boxes in reality)
        R = ''.join([bin(SBOX[0][int(R[i * 6:(i + 1) * 6][:1], 2)][int(R[i * 6:(i + 1) * 6][1:5], 2)])[2:].zfill(4) for i in range(8)])
        
        R = bin(int(L, 2) ^ int(R, 2))[2:].zfill(32)
        L = old_R

    # Combine L and R
    combined = R + L

    # Apply final permutation
    plaintext = permute(combined, FP)
    return plaintext

# Input from user
ciphertext = input("Enter 64-bit ciphertext (in binary): ")
key = input("Enter 64-bit key (in binary): ")

# Perform DES decryption
plaintext = des_decrypt(ciphertext, key)
print(f"Decrypted plaintext (in binary): {plaintext}")
