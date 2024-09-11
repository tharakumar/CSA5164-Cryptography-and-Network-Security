import random

SIZE = 5  # SHA-3 state matrix dimensions

def initialize_state():
    """Initialize the state matrix with all zeros."""
    return [[0] * SIZE for _ in range(SIZE)]

def print_state(state):
    """Print the state matrix."""
    for row in state:
        print(" ".join(f"{x:016x}" for x in row))
    print()

def all_capacity_lanes_nonzero(state):
    """Check if all lanes have at least one non-zero bit."""
    return all(state[i][j] != 0 for i in range(SIZE) for j in range(SIZE))

def update_state(state):
    """Update the state matrix by setting a random bit to 1 in each lane."""
    for i in range(SIZE):
        for j in range(SIZE):
            bit_pos = random.randint(0, 63)  # Random bit position (0 to 63)
            state[i][j] ^= (1 << bit_pos)  # Set the bit at bit_pos to 1

def main():
    state = initialize_state()
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
