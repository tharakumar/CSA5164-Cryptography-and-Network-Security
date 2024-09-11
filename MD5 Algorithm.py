import struct

def pad_message(message_bits):
    """Pad the message to be a multiple of 512 bits."""
    original_length = len(message_bits)
    
    # Add the 1 bit
    message_bits += '1'
    
    # Pad with 0s until the length is 64 bits less than a multiple of 512
    while (len(message_bits) + 64) % 512 != 0:
        message_bits += '0'
    
    # Append the original length as a 64-bit integer
    length_bits = format(original_length, '064b')
    message_bits += length_bits
    
    # Convert the binary message to bytes
    message_bytes = int(message_bits, 2).to_bytes((len(message_bits) + 7) // 8, byteorder='big')
    
    return message_bytes

def md5_round_function(A, B, C, D, M, s, K):
    """Perform one round of the MD5 function."""
    F = (B & C) | (~B & D)
    A = (A + F + M + K) & 0xFFFFFFFF
    A = ((A << s) | (A >> (32 - s))) & 0xFFFFFFFF
    A += B
    return A

def main():
    # Example message in bits
    original_message = '1' * 1000  # 1000 bits of '1'
    
    # Pad the message
    padded_message = pad_message(original_message)
    
    # Print length of the padded message in bits and bytes
    print(f"Padded message length: {len(padded_message) * 8} bits")
    print(f"Padded message length: {len(padded_message)} bytes")

    # Example MD5 round function
    A, B, C, D = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476
    M = struct.unpack('<I', padded_message[:4])[0]  # First 32-bit chunk
    s = 7  # Example shift amount
    K = 0x5A827999  # Example constant
    
    # Perform one round of the MD5 function
    result_A = md5_round_function(A, B, C, D, M, s, K)
    
    print(f"Result of one MD5 round function: {result_A:08X}")

if __name__ == "__main__":
    main()
