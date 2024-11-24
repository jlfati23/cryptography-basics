ALPHABET  = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = 5

def caesar_encrypt(plaintext):
    ciphertext = ''
    for p in plaintext:
        index = ALPHABET.find(p)
        if index != -1:
            ciphertext += ALPHABET[(index + key) % len(ALPHABET)]
        else:
            ciphertext += p
    return ciphertext


def caesar_decrypt(ciphertext):
    plaintext = ''
    for c in ciphertext:
        index = ALPHABET.find(c)
        if index != -1:
            plaintext += ALPHABET[(index - key) % len(ALPHABET)]
        else:
            plaintext += c
    return plaintext

if __name__ == '__main__':
    plaintext = input("Enter a message: ")
    ciphertext = caesar_encrypt(plaintext)
    print("Ciphertext: ", ciphertext)
    decrypted_text = caesar_decrypt(ciphertext)
    print("Decrypted text: ", decrypted_text)
            
