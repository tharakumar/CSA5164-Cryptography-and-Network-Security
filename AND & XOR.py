def and_operation(input_string, mask):
    """AND each character in the input string with the given mask."""
    return ''.join(chr(ord(char) & mask) for char in input_string)

def xor_operation(input_string, mask):
    """XOR each character in the input string with the given mask."""
    return ''.join(chr(ord(char) ^ mask) for char in input_string)

def main():
    # Initialize the string
    original_string = "Hello world"
    mask = 127  # Mask value

    # Perform AND and XOR operations
    and_result = and_operation(original_string, mask)
    xor_result = xor_operation(original_string, mask)

    # Display the results
    print("Original String:", original_string)
    print("AND Result with mask 127:", and_result)
    print("XOR Result with mask 127:", xor_result)

if __name__ == "__main__":
    main()
