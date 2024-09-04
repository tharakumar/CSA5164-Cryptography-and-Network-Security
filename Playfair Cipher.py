def create_playfair_matrix(key):
    """Create a 5x5 matrix for the Playfair cipher based on the key."""
    matrix = []
    seen = set()
    key = key.replace("j", "i")  
    for char in key:
        if char not in seen:
            seen.add(char)
            matrix.append(char)
    for char in "abcdefghiklmnopqrstuvwxyz":
        if char not in seen:
            seen.add(char)
            matrix.append(char)
    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    """Find the row and column of a character in the matrix."""
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def playfair_cipher(text, key, mode='encrypt'):
    """Encrypt or decrypt the text using the Playfair cipher."""
    matrix = create_playfair_matrix(key)
    result = []
    text = text.replace("j", "i")
    prepared_text = ""
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] != text[i + 1]:
            prepared_text += text[i] + text[i + 1]
            i += 2
        else:
            prepared_text += text[i] + 'x'
            i += 1
    if len(prepared_text) % 2 != 0:
        prepared_text += 'x'  
    for i in range(0, len(prepared_text), 2):
        char1, char2 = prepared_text[i], prepared_text[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)
        if row1 == row2:  
            if mode == 'encrypt':
                result.append(matrix[row1][(col1 + 1) % 5])
                result.append(matrix[row2][(col2 + 1) % 5])
            else:
                result.append(matrix[row1][(col1 - 1) % 5])
                result.append(matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:  
            if mode == 'encrypt':
                result.append(matrix[(row1 + 1) % 5][col1])
                result.append(matrix[(row2 + 1) % 5][col2])
            else:
                result.append(matrix[(row1 - 1) % 5][col1])
                result.append(matrix[(row2 - 1) % 5][col2])
        else:  
            result.append(matrix[row1][col2])
            result.append(matrix[row2][col1])

    return "".join(result)

def main():
    # Input text
    text = input("Enter the text: ").lower().replace(" ", "")
    # Input key
    key = input("Enter the key: ").lower().replace(" ", "")

    # Encrypt the text
    encrypted_text = playfair_cipher(text, key, mode='encrypt')
    print(f"Encrypted text: {encrypted_text}")

    # Decrypt the text
    decrypted_text = playfair_cipher(encrypted_text, key, mode='decrypt')
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
