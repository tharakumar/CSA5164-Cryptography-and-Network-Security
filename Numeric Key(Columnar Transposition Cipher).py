def encrypt_columnar_transposition(plaintext, key):
    """Encrypts plaintext using Columnar Transposition Cipher with the given key."""
    # Remove spaces from plaintext and ensure key is valid
    plaintext = plaintext.replace(" ", "")
    num_cols = len(key)
    num_rows = len(plaintext) // num_cols + (1 if len(plaintext) % num_cols > 0 else 0)
    
    # Pad plaintext to fit the grid if necessary
    padded_length = num_cols * num_rows
    plaintext += 'X' * (padded_length - len(plaintext))
    
    # Create the grid
    grid = [plaintext[i * num_cols:(i + 1) * num_cols] for i in range(num_rows)]
    
    # Order the columns by the key
    sorted_columns = sorted(range(num_cols), key=lambda k: key[k])
    
    # Read columns according to the sorted key
    ciphertext = ''.join(''.join(grid[row][col] for row in range(num_rows)) for col in sorted_columns)
    
    return ciphertext

def decrypt_columnar_transposition(ciphertext, key):
    """Decrypts ciphertext using Columnar Transposition Cipher with the given key."""
    num_cols = len(key)
    num_rows = len(ciphertext) // num_cols
    
    # Create an empty grid
    grid = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    
    # Order the columns by the key
    sorted_columns = sorted(range(num_cols), key=lambda k: key[k])
    
    # Fill columns according to the sorted key
    index = 0
    for col in sorted_columns:
        for row in range(num_rows):
            grid[row][col] = ciphertext[index]
            index += 1
    
    # Read rows to form the plaintext
    plaintext = ''.join(''.join(grid[row]) for row in range(num_rows))
    
    # Remove padding (X characters added for padding)
    return plaintext.rstrip('X')

def main():
    plaintext = input("Enter the plaintext message: ")
    key = input("Enter the numeric key (a string of numbers): ")
    
    encrypted = encrypt_columnar_transposition(plaintext, key)
    print(f'Encrypted text: {encrypted}')
    
    decrypted = decrypt_columnar_transposition(encrypted, key)
    print(f'Decrypted text: {decrypted}')

if __name__ == "__main__":
    main()
