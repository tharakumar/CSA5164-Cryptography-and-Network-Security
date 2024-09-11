from collections import Counter
import string

# Frequency distribution of letters in typical English text (percentage-based)
ENGLISH_FREQUENCIES = {
    'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75,
    'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78,
    'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
    'P': 1.93, 'B': 1.49, 'V': 0.98, 'K': 0.77, 'X': 0.15, 'J': 0.15,
    'Q': 0.10, 'Z': 0.07
}

# Function to get letter frequency distribution from the ciphertext
def get_ciphertext_frequencies(ciphertext):
    # Count the frequency of each letter in the ciphertext
    letter_count = Counter(ciphertext.upper())
    total_letters = sum(letter_count[char] for char in string.ascii_uppercase)
    
    # Calculate the percentage frequency of each letter
    frequencies = {}
    for letter in string.ascii_uppercase:
        frequencies[letter] = (letter_count[letter] / total_letters) * 100 if total_letters else 0
    return frequencies

# Function to create a frequency mapping between ciphertext and English letters
def create_frequency_mapping(cipher_frequencies):
    # Sort the English letters and ciphertext letters by frequency
    english_sorted = sorted(ENGLISH_FREQUENCIES.items(), key=lambda x: x[1], reverse=True)
    cipher_sorted = sorted(cipher_frequencies.items(), key=lambda x: x[1], reverse=True)

    # Create a mapping from ciphertext letters to English letters
    mapping = {}
    for (cipher_letter, _), (english_letter, _) in zip(cipher_sorted, english_sorted):
        mapping[cipher_letter] = english_letter
    return mapping

# Function to decrypt the ciphertext based on the mapping
def decrypt_with_mapping(ciphertext, mapping):
    plaintext = []
    for char in ciphertext:
        if char.upper() in mapping:
            decrypted_char = mapping[char.upper()]
            plaintext.append(decrypted_char.lower() if char.islower() else decrypted_char)
        else:
            plaintext.append(char)  # Non-alphabet characters remain unchanged
    return ''.join(plaintext)

# Function to perform letter frequency attack
def letter_frequency_attack(ciphertext, top_n=10):
    # Get the letter frequency distribution of the ciphertext
    cipher_frequencies = get_ciphertext_frequencies(ciphertext)

    # Generate the frequency mapping
    mapping = create_frequency_mapping(cipher_frequencies)

    # Decrypt the ciphertext using the initial frequency mapping
    possible_plaintexts = [decrypt_with_mapping(ciphertext, mapping)]

    # Generate top-n possible plaintexts by slightly tweaking the frequency mapping
    for i in range(1, top_n):
        # Swap two random letters in the mapping for variation
        swapped_mapping = mapping.copy()
        letter1, letter2 = list(mapping.keys())[i % 26], list(mapping.keys())[(i + 1) % 26]
        swapped_mapping[letter1], swapped_mapping[letter2] = swapped_mapping[letter2], swapped_mapping[letter1]

        possible_plaintexts.append(decrypt_with_mapping(ciphertext, swapped_mapping))

    return possible_plaintexts

def main():
    # Get user input for ciphertext and number of top plaintexts to display
    ciphertext = input("Enter the ciphertext: ")
    top_n = int(input("Enter the number of top possible plaintexts to display: "))

    # Perform the letter frequency attack
    possible_plaintexts = letter_frequency_attack(ciphertext, top_n)

    # Display the top possible plaintexts
    print("\nTop possible plaintexts:")
    for i, plaintext in enumerate(possible_plaintexts):
        print(f"{i + 1}. {plaintext}")

if __name__ == "__main__":
    main()
