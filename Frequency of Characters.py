from collections import Counter

def analyze_frequency(ciphertext):
    # Remove any non-alphabetic characters and make the text lowercase
    ciphertext = ''.join(filter(str.isalpha, ciphertext)).lower()
    
    # Calculate frequency of each letter
    frequency = Counter(ciphertext)
    
    # Sort by frequency in descending order
    sorted_frequency = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    
    return sorted_frequency

# Ciphertext provided
ciphertext = "cxknxawxccxkncqjcrbcqnzdnbcrxwfruurjvbqjtnbynjan"

# Analyze the frequency of characters
frequency_analysis = analyze_frequency(ciphertext)

print("Character frequency analysis:")
for char, freq in frequency_analysis:
    print(f"{char}: {freq}")
