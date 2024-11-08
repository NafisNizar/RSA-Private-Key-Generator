from Crypto.PublicKey import RSA
from sympy import mod_inverse

def generate_rsa_private_key(p, q, e):
    # Step 1: Calculate n
    n = p * q

    # Step 2: Calculate φ(n)
    phi_n = (p - 1) * (q - 1)

    # Step 3: Ensure e is valid
    if e <= 1 or e >= phi_n or gcd(e, phi_n) != 1:
        raise ValueError("Invalid public exponent e")

    # Step 4: Calculate d
    d = mod_inverse(e, phi_n)

    return n, e, d, p, q

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Get user input for p , q and e
try:
    p = int(input("Enter a prime number p: "))
    q = int(input("Enter another prime number q: "))
    e = int(input("Enter value of public exponent e:"))
    # Generate RSA private key components
    n, e, d, p, q = generate_rsa_private_key(p, q, e)

    # Construct the RSA key
    key = RSA.construct((n, e, d, p, q))

    # Export the key to PEM format
    with open("private_key.pem", "wb") as f:
        f.write(key.export_key(format='PEM'))

    print("Private key saved to private_key.pem")
    print(f"Modulus n: {n}")
    print(f"Public exponent e: {e}")
    print(f"Private exponent d: {d}")

except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
