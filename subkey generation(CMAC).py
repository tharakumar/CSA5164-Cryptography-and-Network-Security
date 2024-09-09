from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii

def left_shift_one_bit(block):
    """
    Perform a left shift of one bit on a block of bytes.
    """
    shifted_block = bytearray(len(block))
    carry = 0

    for i in range(len(block)):
        byte = block[i]
        shifted_block[i] = ((byte << 1) | carry) & 0xFF
        carry = (byte >> 7) & 0x01

    return shifted_block

def xor_with_constant(block, constant):
    """
    XOR the block with the given constant.
    """
    return bytearray(b ^ constant for b in block)

def generate_subkeys(key, block_size):
    """
    Generate CMAC subkeys for a given block size.
    """
    cipher = AES.new(key, AES.MODE_ECB)
    
    # Create the initial block of all zero bits
    zero_block = bytes(block_size // 8)

    # Encrypt the zero block to get the initial subkey
    l = cipher.encrypt(zero_block)

    # Determine the constant based on the block size
    if block_size == 128:
        constant = 0x87
    elif block_size == 64:
        constant = 0x1B
    else:
        raise ValueError("Unsupported block size")

    # Generate the first subkey (K1)
    k1 = left_shift_one_bit(l)
    if l[0] & 0x80:
        k1 = xor_with_constant(k1, constant)

    # Generate the second subkey (K2)
    k2 = left_shift_one_bit(k1)
    if k1[0] & 0x80:
        k2 = xor_with_constant(k2, constant)

    return k1, k2

def main():
    # Get user input for key and block size
    key_input = input("Enter a key in hexadecimal format (e.g., '1234567890abcdef1234567890abcdef'): ")
    key = bytes.fromhex(key_input)

    block_size = int(input("Enter the block size (64 or 128 bits): "))

    if len(key) != 16:
        print("Error: Key must be exactly 16 bytes (128 bits).")
        return

    if block_size not in [64, 128]:
        print("Error: Unsupported block size. Use 64 or 128 bits.")
        return

    # Generate the subkeys
    k1, k2 = generate_subkeys(key, block_size)
    
    # Display results
    print(f"Subkey K1: {binascii.hexlify(k1).decode()}")
    print(f"Subkey K2: {binascii.hexlify(k2).decode()}")

if __name__ == "__main__":
    main()
