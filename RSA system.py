from sympy import mod_inverse

def find_primes(n):
    """ Factorize n into its prime factors p and q. """
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i, n // i
    return None, None

def rsa_private_key(e, n):
    """ Calculate the private key d for RSA encryption. """
    # Step 1: Factorize n
    p, q = find_primes(n)
    if p is None or q is None:
        raise ValueError("Failed to factorize n into primes.")
    
    print(f"Prime factors: p = {p}, q = {q}")
    
    # Step 2: Calculate φ(n)
    phi_n = (p - 1) * (q - 1)
    print(f"φ(n) = {phi_n}")

    # Step 3: Find the multiplicative inverse of e mod φ(n)
    d = mod_inverse(e, phi_n)
    
    return d

def main():
    e = int(input("Enter public exponent e: "))
    n = int(input("Enter modulus n: "))

    private_key = rsa_private_key(e, n)
    print(f"Private key d = {private_key}")

if __name__ == "__main__":
    main()
