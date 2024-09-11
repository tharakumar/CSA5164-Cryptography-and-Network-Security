def xor_string(input_string, key):
    """XOR each character in the input string with the given key."""
    result = ''.join(chr(ord(char) ^ key) for char in input_string)
    return result

def main():
    # Initialize the string
    original_string = "Hello world"
    key = 0  # XOR key

    # Perform XOR operation
    xor_result = xor_string(original_string, key)

    # Display the results
    print("Original String:", original_string)
    print("XOR Result with key 0:", xor_result)

if __name__ == "__main__":
    main()
