import random

# Diffie-Hellman key exchange (traditional)
def diffie_hellman_protocol(q, a):
    # Each participant selects a secret number x
    alice_secret = random.randint(2, q - 1)
    bob_secret = random.randint(2, q - 1)

    # Alice and Bob send each other a^x mod q
    alice_public = pow(a, alice_secret, q)
    bob_public = pow(a, bob_secret, q)

    print(f"Alice's secret: {alice_secret}")
    print(f"Bob's secret: {bob_secret}")
    print(f"Alice sends to Bob: {alice_public}")
    print(f"Bob sends to Alice: {bob_public}")

    # Both compute the shared key: a^(x * y) mod q
    alice_shared_key = pow(bob_public, alice_secret, q)
    bob_shared_key = pow(alice_public, bob_secret, q)

    print(f"Alice's computed shared key: {alice_shared_key}")
    print(f"Bob's computed shared key: {bob_shared_key}")
    
    return alice_shared_key, bob_shared_key

# Modified version where x * a is sent instead of a^x mod q
def modified_diffie_hellman(q, a):
    # Each participant selects a secret number x
    alice_secret = random.randint(2, q - 1)
    bob_secret = random.randint(2, q - 1)

    # Alice and Bob send each other x * a instead of a^x mod q
    alice_sends = alice_secret * a
    bob_sends = bob_secret * a

    print(f"Alice's secret: {alice_secret}")
    print(f"Bob's secret: {bob_secret}")
    print(f"Alice sends to Bob: {alice_sends}")
    print(f"Bob sends to Alice: {bob_sends}")

    # Both compute the "shared key" using the modified method
    # This is fundamentally flawed and will not be secure
    alice_shared_key = bob_sends * alice_secret
    bob_shared_key = alice_sends * bob_secret

    print(f"Alice's computed 'shared key': {alice_shared_key}")
    print(f"Bob's computed 'shared key': {bob_shared_key}")
    
    return alice_shared_key, bob_shared_key

def main():
    # Example prime q and generator a (these are public)
    q = 23  # Small prime number (in real protocols, q should be much larger)
    a = 5   # Generator

    print("Traditional Diffie-Hellman Protocol:")
    diffie_hellman_protocol(q, a)

    print("\nModified Diffie-Hellman Protocol (Sending x * a):")
    modified_diffie_hellman(q, a)

if __name__ == "__main__":
    main()
