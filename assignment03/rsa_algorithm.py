from random import randrange
from sympy import gcd, isprime


def multiplicative_inverse(e, phi):
    """
    Calculates the modular multiplicative inverse d such that:
    (d * e) % phi == 1
    This is used to generate the private key.
    """
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


def generate_keypair(p, q):
    """
    Generates the Public and Private keys based on primes p and q.
    """
    if not (isprime(p) and isprime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal.")

    # 1. Calculate nES = p * q
    n = p * q

    # 2. Calculate phi(n) = (p-1) * (q-1)
    phi = (p - 1) * (q - 1)

    # 3. Select integer e such that gcd(phi, e) = 1 and 1 < e < phi
    e = randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = randrange(1, phi)
        g = gcd(e, phi)

    # 4. Calculate d such that d * e = 1 (mod phi) === d = e^(-1) (mod phi)
    d = multiplicative_inverse(e, phi)

    # Public Key = (e, n), Private Key = (d, n)
    return ((e, n), (d, n))


def encrypt(public_key, plaintext):
    """
    Encrypts a string message into a list of integers.
    """
    e, n = public_key
    # Convert each character to its ASCII value and apply the formula
    cipher = [(ord(char) ** e) % n for char in plaintext]
    return cipher


def decrypt(private_key, ciphertext):
    """
    Decrypts a list of integers back into a string.
    Formula: M = C^d mod n (Slide 19)
    """
    d, n = private_key
    # Apply formula to each number and convert ASCII back to char
    plain = [chr((char**d) % n) for char in ciphertext]
    return "".join(plain)


# --- Main Simulation ---

if __name__ == "__main__":
    print("=" * 50)
    print("            RSA Algorithm Simulation")
    print("=" * 50)

    # ==========================================
    # Step 1: Key Generation by Alice
    # ==========================================
    print("\n>>> Key Generation by Alice <<<\n")

    # Select p and q (both prime, p != q)
    p = 73
    q = 151
    print(f"Select p = {p}, q = {q} (both prime, p != q)")

    # Calculate n = p x q
    n = p * q
    print(f"Calculate n = p x q = {p} x {q} = {n}")

    # Calculate phi(n) = (p-1)(q-1)
    phi = (p - 1) * (q - 1)
    print(f"Calculate phi(n) = (p-1)(q-1) = ({p}-1)({q}-1) = {phi}")

    # Generate keypair (e and d are calculated inside)
    public_key_alice, private_key_alice = generate_keypair(p, q)
    e, _ = public_key_alice
    d, _ = private_key_alice

    print(f"Select integer e such that gcd(phi(n), e) = 1 and 1 < e < phi(n)")
    print(f"  => e = {e}")
    print(f"Calculate d = e^(-1) (mod phi(n))")
    print(f"  => d = {d}")

    print(f"\nPublic Key  PU = {{e, n}} = {{{e}, {n}}}")
    print(f"Private Key PR = {{d, n}} = {{{d}, {n}}}")

    # ==========================================
    # Step 2: Encryption by Bob with Alice's Public Key
    # ==========================================
    print("\n" + "-" * 50)
    print("\n>>> Encryption by Bob with Alice's Public Key <<<\n")

    message = "How_are_you?"
    print(f"Plaintext M = '{message}'")
    print(f"(M must be < n, each char ASCII < {n})")

    # Bob encrypts using ALICE'S PUBLIC KEY
    # Formula: C = M^e mod n
    encrypted_msg = encrypt(public_key_alice, message)
    print(f"\nCiphertext C = M^e mod n")
    print(f"Encrypted message: {encrypted_msg}")

    # ==========================================
    # Step 3: Decryption by Alice with Alice's Private Key
    # ==========================================
    print("\n" + "-" * 50)
    print("\n>>> Decryption by Alice with Alice's Private Key <<<\n")

    print(f"Ciphertext C = {encrypted_msg}")

    # Alice decrypts using ALICE'S PRIVATE KEY
    # Formula: M = C^d mod n
    decrypted_msg = decrypt(private_key_alice, encrypted_msg)
    print(f"\nPlaintext M = C^d mod n")
    print(f"Decrypted message: '{decrypted_msg}'")

    print("\n" + "=" * 50)
    print("            Simulation Complete")
    print("=" * 50)
