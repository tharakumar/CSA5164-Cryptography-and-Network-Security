def sdes_key_schedule(key):
    # Key generation from 10-bit key (for simplicity, this is a basic implementation)
    return [key[:8], key[8:]]

def sdes_encrypt_block(block, key):
    # A simplified placeholder function for S-DES encryption
    # You would replace this with actual S-DES encryption logic
    return block[::-1]  # Reverse block as placeholder

def sdes_decrypt_block(block, key):
    # A simplified placeholder function for S-DES decryption
    # You would replace this with actual S-DES decryption logic
    return block[::-1]  # Reverse block as placeholder

def xor_blocks(block1, block2):
    return bytes(a ^ b for a, b in zip(block1, block2))

def pad_data(data, block_size):
    # Pad data to be a multiple of the block size
    padding = block_size - (len(data) % block_size)
    return data + bytes([padding] * padding)

def unpad_data(data):
    padding = data[-1]
    return data[:-padding]

def encrypt_sdes_cbc(key, iv, plaintext):
    block_size = len(iv)
    plaintext = pad_data(plaintext, block_size)
    cipher_text = bytearray()
    previous_block = iv

    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i + block_size]
        xor_block = xor_blocks(block, previous_block)
        encrypted_block = sdes_encrypt_block(xor_block, key)
        cipher_text.extend(encrypted_block)
        previous_block = encrypted_block

    return bytes(cipher_text)

def decrypt_sdes_cbc(key, iv, ciphertext):
    block_size = len(iv)
    plaintext = bytearray()
    previous_block = iv

    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i + block_size]
        decrypted_block = sdes_decrypt_block(block, key)
        plaintext_block = xor_blocks(decrypted_block, previous_block)
        plaintext.extend(plaintext_block)
        previous_block = block

    return unpad_data(plaintext)

def main():
    key_input = input("Enter binary key (10 bits, e.g., 0111111101): ")
    iv_input = input("Enter binary IV (8 bits, e.g., 10101010): ")
    plaintext_input = input("Enter binary plaintext (multiple of 8 bits, e.g., 0000000100100011): ")

    key = bytes(int(key_input[i:i + 8], 2) for i in range(0, len(key_input), 8))
    iv = bytes(int(iv_input[i:i + 8], 2) for i in range(0, len(iv_input), 8))
    plaintext = bytes(int(plaintext_input[i:i + 8], 2) for i in range(0, len(plaintext_input), 8))

    print(f"Original Plaintext: {''.join(format(byte, '08b') for byte in plaintext)}")

    # Encrypt plaintext
    ciphertext = encrypt_sdes_cbc(key, iv, plaintext)
    print(f"Ciphertext: {''.join(format(byte, '08b') for byte in ciphertext)}")

    # Decrypt ciphertext
    decrypted_plaintext = decrypt_sdes_cbc(key, iv, ciphertext)
    print(f"Decrypted Plaintext: {''.join(format(byte, '08b') for byte in decrypted_plaintext)}")

if __name__ == "__main__":
    main()
