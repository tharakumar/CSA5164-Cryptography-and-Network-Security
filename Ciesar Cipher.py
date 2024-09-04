def caesar_cipher(text, shift, mode):
    result = []
    shift = shift % 26  # Ensure the shift is within the range of 0-25

    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - start + shift) % 26 + start))
        else:
            result.append(char)

    return ''.join(result)

def main():
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))

    encrypted_text = caesar_cipher(text, shift, 'encrypt')
    decrypted_text = caesar_cipher(encrypted_text, shift, 'decrypt')

    print(f"Encrypted text: {encrypted_text}")
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
