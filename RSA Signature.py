from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes

# Generate a DSA private key
private_key = dsa.generate_private_key(key_size=2048)

# Function to sign a message
def sign_message(message):
    # Generate a signature using DSA
    signature = private_key.sign(
        message.encode('utf-8'),
        hashes.SHA256()
    )
    return signature

# Function to verify the signature
def verify_signature(message, signature):
    public_key = private_key.public_key()
    try:
        # Verify the signature
        public_key.verify(
            signature,
            message.encode('utf-8'),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False

def main():
    message = input("Enter the message to sign: ")

    # Sign the message
    signature_1 = sign_message(message)
    print("Signature 1:", signature_1.hex())

    # Sign the message again
    signature_2 = sign_message(message)
    print("Signature 2:", signature_2.hex())

    # Check if signatures are different
    if signature_1 != signature_2:
        print("\nSignatures are different, as expected in DSA.")
    else:
        print("\nSignatures are the same.")

    # Verify both signatures
    if verify_signature(message, signature_1):
        print("\nSignature 1 is valid.")
    else:
        print("\nSignature 1 is invalid.")

    if verify_signature(message, signature_2):
        print("Signature 2 is valid.")
    else:
        print("Signature 2 is invalid.")

if __name__ == "__main__":
    main()
