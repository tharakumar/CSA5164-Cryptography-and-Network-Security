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
    letter_count = Counter(ciphertext.upper())
    total_letters = sum(letter_count[char] for char in string.ascii_uppercase)
    frequencies = {}
    for letter in string.ascii_uppercase:
        frequencies[letter] = (letter_count[letter] / total_letters) * 100 if total_letters else 0
    return frequencies

# Function to decrypt the ciphertext with a given shift
def decrypt_with_shift(ciphertext, shift):
    plaintext = []
    for char in ciphertext:
        if char.upper() in string.ascii_uppercase:
            shifted = (letter_to_num(char) - shift) % 26
            plaintext.append(num_to_letter(shifted).lower() if char.islower() else num_to_letter(shifted))
        else:
            plaintext.append(char)
    return ''.join(plaintext)

# Function to score plaintext based on letter frequencies
def score_plaintext(plaintext):
    plaintext_frequencies = get_ciphertext_frequencies(plaintext)
    score = 0
    for letter, freq in ENGLISH_FREQUENCIES.items():
        score += abs(freq - plaintext_frequencies.get(letter, 0))
    return score

# Function to perform a letter frequency attack
def letter_frequency_attack(ciphertext, top_n=10):
    # Store possible plaintexts and their scores
    possible_plaintexts = []
    
    # Try all possible shifts (0 to 25)
    for shift in range(26):
        plaintext = decrypt_with_shift(ciphertext, shift)
        score = score_plaintext(plaintext)
        possible_plaintexts.append((plaintext, score))
    
    # Sort possible plaintexts by score (lower score is better)
    possible_plaintexts.sort(key=lambda x: x[1])
    
    # Return the top_n possible plaintexts
    return possible_plaintexts[:top_n]

def letter_to_num(letter):
    return ord(letter.upper()) - ord('A')

def num_to_letter(num):
    return chr(num + ord('A'))

def main():
    # Get user input for ciphertext
    ciphertext = input("Enter the ciphertext: ")

    # Get user input for number of top plaintexts to display
    while True:
        try:
            top_n = int(input("Enter the number of top possible plaintexts to display: "))
            break  # Break the loop if valid input is received
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    
    # Perform the letter frequency attack
    possible_plaintexts = letter_frequency_attack(ciphertext, top_n)
    
    # Display the top possible plaintexts
    print("\nTop possible plaintexts:")
    for i, (plaintext, score) in enumerate(possible_plaintexts):
        print(f"{i + 1}. {plaintext} (Score: {score:.2f})")

if __name__ == "__main__":
    main()
