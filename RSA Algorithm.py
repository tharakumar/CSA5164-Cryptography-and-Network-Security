from sympy import mod_inverse

def factorize_n_using_common_factor(n, common_factor):
    """ Factorize n using a common factor. """
    if common_factor <= 1 or n % common_factor != 0:
        print(f"Error: The common factor {common_factor} does not divide n = {n} correctly.")
        raise ValueError("Invalid common factor.")
    
    p = common_factor
    q = n // p
    return p, q

def rsa_private_key(e, n, common_factor):
    """ Calculate the private key d for RSA encryption. """
    # Step 1: Factorize n using the common factor
    p, q = factorize_n_using_common_factor(n, common_factor)
    print(f"Prime factors: p = {p}, q = {q}")
    
    # Step 2: Calculate φ(n)
    phi_n = (p - 1) * (q - 1)
    print(f"φ(n) = {phi_n}")

    # Step 3: Find the multiplicative inverse of e mod φ(n)
    try:
        d = mod_inverse(e, phi_n)
    except ValueError as ve:
        print(f"Error finding modular inverse: {ve}")
        raise
    
    return d

def main():
    e = int(input("Enter public exponent e: "))
    n = int(input("Enter modulus n: "))
    common_factor = int(input("Enter common factor with plaintext block: "))

    private_key = rsa_private_key(e, n, common_factor)
    print(f"Private key d = {private_key}")

if __name__ == "__main__":
    main()
