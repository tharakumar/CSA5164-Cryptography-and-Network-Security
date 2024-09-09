def permute(bits, table):
    return ''.join(bits[i - 1] for i in table)

def left_shift(bits, shift_amount):
    return bits[shift_amount:] + bits[:shift_amount]

def generate_keys(key):
    # Permuted Choice 1 (PC1) tables
    PC1_C = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36]
    PC1_D = [63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
    
    # Permuted Choice 2 (PC2) table
    PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
    
    # Key schedule shift values
    SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    
    # Apply PC1 to split key into C and D
    key = permute(key, PC1_C + PC1_D)
    C, D = key[:28], key[28:]
    
    round_keys = []
    for shift in SHIFT_SCHEDULE:
        C = left_shift(C, shift)
        D = left_shift(D, shift)
        combined = C + D
        round_key = permute(combined, PC2)
        round_keys.append(round_key)
    
    return round_keys

def des_encrypt(plaintext, key):
    # Generate round keys
    round_keys = generate_keys(key)
    
    # Placeholder encryption (not a full DES implementation)
    print("Round keys:")
    for i, key in enumerate(round_keys):
        print(f"Round {i + 1} Key: {key}")
    
    # Placeholder ciphertext (for demonstration)
    return plaintext

def hex_to_bin(hex_str):
    return bin(int(hex_str, 16))[2:].zfill(64)

def bin_to_hex(bin_str):
    return hex(int(bin_str, 2))[2:].zfill(16)

def main():
    # User input
    key_hex = input("Enter 64-bit key in hexadecimal (e.g., 133457799BBCDFF1): ")
    plaintext_hex = input("Enter 64-bit plaintext in hexadecimal (e.g., 0123456789ABCDEF): ")
    
    # Convert hexadecimal input to binary strings
    key_bin = hex_to_bin(key_hex)
    plaintext_bin = hex_to_bin(plaintext_hex)
    
    # Perform DES encryption
    ciphertext_bin = des_encrypt(plaintext_bin, key_bin)
    
    # Output encrypted result (for demonstration)
    ciphertext_hex = bin_to_hex(ciphertext_bin)
    print(f"Encrypted ciphertext (placeholder): {ciphertext_hex}")

if __name__ == "__main__":
    main()
