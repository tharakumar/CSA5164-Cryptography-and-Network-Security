from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii

def compute_cbc_mac(key, message, block_size=16):
    """
    Compute the CBC MAC of the given message using the provided key.
    """
    cipher = AES.new(key, AES.MODE_ECB)  # CBC mode requires an IV, but for MAC we use ECB
    # Pad message to block size
    padded_message = pad(message, block_size)
    
    # Initialize variables
    mac = bytes(block_size)
    
    # Process each block
    for i in range(0, len(padded_message), block_size):
        block = padded_message[i:i+block_size]
        mac = cipher.encrypt(bytes(a ^ b for a, b in zip(mac, block)))
    
    return mac

def main():
    # Get user input for the key and message
    key_input = input("Enter a 16-byte key in hexadecimal format (e.g., '1234567890abcdef'): ")
    key = bytes.fromhex(key_input)
    
    message_input = input("Enter a message (must be 16 bytes or a multiple of 16 bytes) in hexadecimal format: ")
    message = bytes.fromhex(message_input)
    
    if len(key) != 16:
        print("Error: Key must be exactly 16 bytes (128 bits).")
        return
    
    if len(message) % 16 != 0:
        print("Error: Message must be a multiple of 16 bytes.")
        return

    # Compute MAC for the message X
    mac = compute_cbc_mac(key, message)
    
    # Adversary constructs X || (X ⊕ T)
    xor_message = bytes(a ^ b for a, b in zip(message, mac))
    combined_message = message + xor_message
    
    # Compute MAC for the two-block message X || (X ⊕ T)
    combined_mac = compute_cbc_mac(key, combined_message)
    
    # Display results
    print(f"Original message X: {binascii.hexlify(message).decode()}")
    print(f"MAC of X (T): {binascii.hexlify(mac).decode()}")
    print(f"XORed message (X ⊕ T): {binascii.hexlify(xor_message).decode()}")
    print(f"Combined message X || (X ⊕ T): {binascii.hexlify(combined_message).decode()}")
    print(f"MAC of combined message: {binascii.hexlify(combined_mac).decode()}")
    print(f"Is the MAC of combined message the same as T? {'Yes' if mac == combined_mac else 'No'}")

if __name__ == "__main__":
    main()
