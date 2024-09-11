import numpy as np
import random

SIZE = 5  # SHA-3 state matrix dimensions
LANE_BITS = 1024  # Number of bits per lane
LANE_COUNT = SIZE * SIZE  # Total number of lanes

def initialize_state():
    """Initialize the state matrix with random nonzero values."""
    state = np.zeros((SIZE, SIZE), dtype=np.uint64)
    for i in range(SIZE):
        for j in range(SIZE):
            # Generate a random nonzero 1024-bit value
            state[i][j] = random.getrandbits(64) | 1  # Ensure at least one bit is set
    return state

def print_state(state):
    """Print the state matrix."""
    for row in state:
        print(" ".join(f"{x:016x}" for x in row))
    print()

def all_capacity_lanes_nonzero(state):
    """Check if all lanes have at least one non-zero bit."""
    return np.all(state != 0)

def update_state(state):
    """Update the state matrix by randomly setting more bits to 1."""
    for i in range(SIZE):
        for j in range(SIZE):
            bit_pos = random.randint(0, 63)  # Random bit position (0 to 63)
            state[i][j] ^= (1 << bit_pos)  # Toggle the bit at bit_pos

def main():
    # Initialize the state matrix
    state = initialize_state()
    print("Initial state matrix:")
    print_state(state)
    
    iterations = 0

    while not all_capacity_lanes_nonzero(state):
        update_state(state)
        iterations += 1
        # Print state matrix and iteration number for debugging
        # print_state(state)
        # print(f"Iteration: {iterations}")

    print(f"Number of iterations to ensure all capacity lanes have at least one non-zero bit: {iterations}")

if __name__ == "__main__":
    main()
