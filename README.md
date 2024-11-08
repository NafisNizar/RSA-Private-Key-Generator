RSA Private Key Generator

Overview

This repository contains a Python script that generates RSA private keys from two user-provided prime numbers pp and qq. The script utilizes the pycryptodome library for key construction and the sympy library for calculating the modular inverse.

RSA Algorithm

  RSA (Rivest-Shamir-Adleman) is a widely used asymmetric cryptographic algorithm. It relies on the mathematical properties of prime numbers to provide security in data
  transmission. The key generation process involves:

    Calculating the Modulus n: n=p×q

    Calculating the Totient ϕ(n): ϕ(n)=(p−1)(q−1)

    Choosing a Public Exponent e: Commonly set to 65537.

    Calculating the Private Exponent d: The modular inverse of e modulo ϕ(n).

Getting Started

Prerequisites

  Make sure you have Python installed. You'll also need to install the required libraries. You can do this using pip:

  pip install pycryptodome sympy

Usage

  1.Clone the repository:

    git clone https://github.com/NafisNizar/RSA-Private-Key-Generator.git

    cd RSA-Private-Key-Generator

  2.Run the script:

    python rsa_key_generator.py

  Enter the two prime numbers pp and qq when prompted.

The script will generate the RSA private key components and save the private key in PEM format to private_key.pem. It will also display the modulus nn, public exponent e, and private exponent dd in the console.

Example

  Enter a prime number p: 61

  Enter another prime number q: 53

  Private key saved to private_key.pem

  Modulus n: 3233

  Public exponent e: 65537

  Private exponent d: 2753

Code Explanation

  generate_rsa_private_key(p, q, e=65537): This function generates the RSA key components from the provided primes.

  gcd(a, b): A helper function to compute the greatest common divisor.

  Error Handling: The script includes error handling for invalid inputs, ensuring robust execution.

Security Considerations

  Ensure that the prime numbers p and q are sufficiently large to guarantee the security of the RSA keys.

  Avoid using small prime numbers in real-world applications.

Contributing

  Contributions are welcome! Feel free to submit issues or pull requests to enhance this project.

License

  This project is licensed under the MIT License.
