def left_rotate(value, shift, bits=32):
    """Rotate left a 32-bit integer value by shift bits."""
    return ((value << shift) | (value >> (bits - shift))) & ((1 << bits) - 1)

def generate_message_schedule(initial_words):
    """Generate the 80-word message schedule array from the initial 16 words."""
    W = initial_words[:]  # Make a copy of the initial words
    for i in range(16, 80):
        W_i = left_rotate(W[i-3] ^ W[i-8] ^ W[i-14] ^ W[i-16], 1)
        W.append(W_i)
    return W

def print_words(W):
    """Print the first 20 words of the message schedule."""
    for i in range(20):
        print(f"W{i:02d}: {W[i]:08X}")

def main():
    # Example initial 16 words (in hexadecimal)
    initial_words = [
        0x12345678, 0x9ABCDEF0, 0x23456789, 0x34567890,
        0x45678901, 0x56789012, 0x67890123, 0x78901234,
        0x89012345, 0x90123456, 0xA0123456, 0xB1234567,
        0xC2345678, 0xD3456789, 0xE4567890, 0xF5678901
    ]

    # Generate the 80-word message schedule
    message_schedule = generate_message_schedule(initial_words)

    # Print the values of W16, W17, W18, W19
    print("Message Schedule (First 20 Words):")
    print_words(message_schedule)

if __name__ == "__main__":
    main()
