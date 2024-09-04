def rail_fence_encrypt(text, rails):
    """Encrypts the text using the Rail Fence cipher."""
    rail = [['' for _ in range(len(text))] for _ in range(rails)]
    dir_down = None
    row, col = 0, 0
    for char in text:
        if row == 0 or row == rails - 1:
            dir_down = not dir_down
        rail[row][col] = char
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    encrypted_text = ''.join([''.join(row) for row in rail])
    return encrypted_text
def rail_fence_decrypt(ciphertext, rails):
    """Decrypts the text using the Rail Fence cipher."""
    rail = [['' for _ in range(len(ciphertext))] for _ in range(rails)]
    dir_down = None
    row, col = 0, 0
    for char in ciphertext:
        if row == 0 or row == rails - 1:
            dir_down = not dir_down
        rail[row][col] = '*'
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    index = 0
    for i in range(rails):
        for j in range(len(ciphertext)):
            if ((rail[i][j] == '*') and (index < len(ciphertext))):
                rail[i][j] = ciphertext[index]
                index += 1
    result = []
    row, col = 0, 0
    for char in range(len(ciphertext)):
        if row == 0 or row == rails - 1:
            dir_down = not dir_down
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    return ''.join(result)
def main():
    text = input("Enter the text: ").replace(" ", "").upper()
    rails = int(input("Enter the number of rails: "))
    encrypted_text = rail_fence_encrypt(text, rails)
    print(f"Encrypted text: {encrypted_text}")
    decrypted_text = rail_fence_decrypt(encrypted_text, rails)
    print(f"Decrypted text: {decrypted_text}")
if __name__ == "__main__":
    main()
