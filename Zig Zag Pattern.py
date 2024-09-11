def encrypt_rail_fence(plaintext, num_rails):
    if num_rails == 1:
        return plaintext  # No need for encryption if there's only one rail
    
    # Create an empty list for each rail
    rails = [''] * num_rails
    rail_direction = 1  # To determine the direction of movement (down/up)
    current_rail = 0    # Start at the top rail (0-indexed)

    # Place each character in the appropriate rail
    for char in plaintext:
        rails[current_rail] += char
        if current_rail == 0:
            rail_direction = 1  # Move down if we hit the top
        elif current_rail == num_rails - 1:
            rail_direction = -1  # Move up if we hit the bottom
        current_rail += rail_direction

    # Combine the rails to form the final ciphertext
    ciphertext = ''.join(rails)
    return ciphertext

# Example usage
if __name__ == "__main__":
    message = "RAILFENCE"
    num_rails = 3

    # Encrypt the message
    encrypted_message = encrypt_rail_fence(message, num_rails)
    print("Encrypted message:", encrypted_message)
