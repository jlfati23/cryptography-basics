
def encrypt(plaintext, key):
    ciphertext = ''
    key = key.upper()
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            base_shift = 65 if char.isupper() else 97
            shift = ord(key[key_index]) - ord('A')
            encrypted_text = chr((ord(char) - base_shift + shift) % 26 + base_shift)
            ciphertext += encrypted_text
            key_index  = (key_index + 1) % len(key)
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    key = key.upper()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            base_shift = 65 if char.isupper() else 97
            shift = ord(key[key_index]) - ord('A')
            decrypted_text = chr((ord(char) - base_shift - shift) % 26 + base_shift)
            plaintext += decrypted_text
            key_index  = (key_index + 1) % len(key)
        else:
            plaintext += char
    return plaintext

if __name__ == '__main__':
    plaintext = 'Hello, World'
    key = 'KEY'
    encrypted_text = encrypt(plaintext, key)
    print("Encrypted text is : ", encrypted_text )
    decrypted_text = decrypt(encrypted_text, key)
    print("Decrypted text is : ", decrypted_text )