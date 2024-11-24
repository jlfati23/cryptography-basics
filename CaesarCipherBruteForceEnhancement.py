# Step 1: Define a function to decrypt Caesar Cipher with a given shift
def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():  # Only decrypt alphabetic characters
            shift_base = 65 if char.isupper() else 97  # ASCII base for uppercase and lowercase
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char  # Non-alphabetic characters remain unchanged
    return decrypted_text

# Step 2: Adding a dictionary-based check or Use Python’s nltk library or a similar tool to tokenize the text and match words to a dictionary.
def is_meaningful(text):
    dictionary = {"hello", "world", "quick", "brown", "fox", "jumps"}  # Example word set
    words = text.lower().split()
    recognized_words = [word for word in words if word in dictionary]
    return len(recognized_words) > 0  # Return True if any word matches

# Step 3: Define a brute force function to try all shifts
def brute_force_caesar_with_detection(ciphertext):
    for shift in range(26):
        decrypted_text = caesar_decrypt(ciphertext, shift)
        # Check if the word matches
        if is_meaningful(decrypted_text):
            print(f"Shift {shift}: {decrypted_text} (likely correct!)")
        else:
            print(f"Shift {shift}: {decrypted_text}")

# Step 3: Main function to get input and execute the brute force process
if __name__ == "__main__":
    # Ciphertext input
    ciphertext = input("Enter the ciphertext: ").strip()
    print("\nBrute forcing Caesar Cipher...\n")
    
    # Perform brute force decryption
    brute_force_caesar_with_detection(ciphertext)
