import os

def generate_random_key(length):
    """
    Generate a truly random key of the given length using os.urandom.
    Each byte is converted to a character in the range 'A' to 'Z'.
    """
    return ''.join(chr((byte % 26) + ord('A')) for byte in os.urandom(length))

def otp_encrypt(plaintext, key):
    """
    Encrypt plaintext using the One-Time Pad (OTP).
    """
    if len(plaintext) != len(key):
        raise ValueError("Key must be the same length as plaintext")

    ciphertext = ''
    for p, k in zip(plaintext, key):
        if p.isalpha():  # Encrypt only alphabetic characters
            shift_base = ord('A') if p.isupper() else ord('a')
            shift = (ord(k.upper()) - ord('A'))
            encrypted_char = chr(((ord(p) - shift_base + shift) % 26) + shift_base)
            ciphertext += encrypted_char
        else:
            ciphertext += p  # Leave non-alphabetic characters unchanged
    return ciphertext

def otp_decrypt(ciphertext, key):
    """
    Decrypt ciphertext using the One-Time Pad (OTP).
    """
    if len(ciphertext) != len(key):
        raise ValueError("Key must be the same length as ciphertext")

    plaintext = ''
    for c, k in zip(ciphertext, key):
        if c.isalpha():  # Decrypt only alphabetic characters
            shift_base = ord('A') if c.isupper() else ord('a')
            shift = (ord(k.upper()) - ord('A'))
            decrypted_char = chr(((ord(c) - shift_base - shift) % 26) + shift_base)
            plaintext += decrypted_char
        else:
            plaintext += c  # Leave non-alphabetic characters unchanged
    return plaintext

if __name__ == '__main__':
    # Example Usage
    plaintext = "HELLO WORLD"
    key = generate_random_key(len(plaintext))
    print("Plaintext:", plaintext)
    print("Key:", key)

    # Encrypt
    ciphertext = otp_encrypt(plaintext, key)
    print("Ciphertext:", ciphertext)

    # Decrypt
    decrypted_text = otp_decrypt(ciphertext, key)
    print("Decrypted Text:", decrypted_text)
