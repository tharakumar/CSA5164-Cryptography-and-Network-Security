import numpy as np

def initialize_state(size):
    """
    Initialize the state matrix with zeros.
    `size` should be a tuple (rows, columns, depth)
    """
    return np.zeros(size, dtype=np.uint8)

def update_state(state, message_block):
    """
    Update the state matrix with the given message block.
    This function simulates updating the state based on the input block P0.
    """
    # Flatten the state to update it with the message block
    flat_state = state.flatten()
    
    # Apply the message block to the state (assuming message block is 1024 bits)
    flat_state[:len(message_block)] = message_block
    
    # Reshape back to the original state matrix shape
    return flat_state.reshape(state.shape)

def check_nonzero_lanes(state, capacity_start_index):
    """
    Check if all lanes in the capacity portion of the state matrix
    have at least one nonzero bit.
    """
    capacity_lanes = state[capacity_start_index:]
    return np.all(capacity_lanes > 0)

def main():
    # State matrix dimensions for SHA-3 with 1024-bit block size
    rows, columns, depth = 5, 5, 64  # 5x5 lanes, each lane 64 bits (8 bytes)
    
    # Initialize state matrix with zeros
    state = initialize_state((rows, columns, depth))
    
    # Get user input for the message block (should be 128 bytes or 1024 bits)
    print("Enter a 1024-bit message block (128 bytes):")
    message_input = input("Enter a string of 128 bytes (hexadecimal format, e.g., '0000ff...'): ")
    
    # Convert the input string to a numpy array of bytes
    message_block = np.array([int(message_input[i:i+2], 16) for i in range(0, len(message_input), 2)], dtype=np.uint8)
    
    if len(message_block) != 128:
        print("Error: The message block must be exactly 128 bytes (1024 bits).")
        return

    # Index to the start of the capacity portion (last 128 bytes)
    capacity_start_index = (rows * columns * (depth - 128))
    
    # Counter to track the number of updates
    update_count = 0
    
    # Apply message block and check state
    while not check_nonzero_lanes(state, capacity_start_index):
        state = update_state(state, message_block)
        update_count += 1
        
        # Simulate changing the message block for next update (e.g., XOR with an increment)
        message_block = np.roll(message_block, 1)  # Just a simple simulation of change
    
    print(f"Number of updates needed before all lanes in the capacity portion have at least one nonzero bit: {update_count}")

if __name__ == "__main__":
    main()
