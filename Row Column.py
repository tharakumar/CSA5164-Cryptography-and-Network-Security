import math

def create_matrix(text, rows, cols):
    """Create a matrix from the given text, padding with 'X' if needed."""
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    index = 0
    for r in range(rows):
        for c in range(cols):
            if index < len(text):
                matrix[r][c] = text[index]
                index += 1
            else:
                matrix[r][c] = 'X'  # Padding if text is shorter
    return matrix

def encrypt(text, key):
    """Encrypt the text using Row Column Transposition Cipher with the provided key."""
    text = text.replace(" ", "").upper()
    cols = len(key)
    rows = math.ceil(len(text) / cols)
    
    matrix = create_matrix(text, rows, cols)
    
    # Key order should be zero-based index
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    
    encrypted_text = []
    for k in key_order:
        for r in range(rows):
            encrypted_text.append(matrix[r][k])
    
    return ''.join(encrypted_text)

def decrypt(ciphertext, key):
    """Decrypt the text using Row Column Transposition Cipher with the provided key."""
    cols = len(key)
    rows = math.ceil(len(ciphertext) / cols)
    
    # Create an empty matrix
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    
    # Key order should be zero-based index
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    
    # Fill the matrix with ciphertext
    index = 0
    for k in key_order:
        for r in range(rows):
            if index < len(ciphertext):
                matrix[r][k] = ciphertext[index]
                index += 1

    decrypted_text = []
    for r in range(rows):
        for c in range(cols):
            decrypted_text.append(matrix[r][c])
    
    return ''.join(decrypted_text).rstrip('X')  # Remove padding 'X'

def main():
    # Input text and key
    text = input("Enter the text: ").replace(" ", "").upper()
    key = list(map(int, input("Enter the key (comma separated): ").split(',')))
    
    # Check key length
    cols = len(key)
    rows = math.ceil(len(text) / cols)
    
    # Encrypt the text
    encrypted_text = encrypt(text, key)
    print(f"Encrypted text: {' '.join(encrypted_text[i:i + 5] for i in range(0, len(encrypted_text), 5))}")

    # Decrypt the text
    decrypted_text = decrypt(encrypted_text, key)
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
