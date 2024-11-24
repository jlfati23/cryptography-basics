from collections import Counter

# Frequency of letters in English (ordered by commonality)
ENGLISH_FREQUENCY = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

# Step 1: Function to decrypt with a specific shift
def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text

# Step 2: Function to count letter frequencies in ciphertext
def letter_frequency_analysis(ciphertext):
    # Filter out non-alphabetic characters and convert to uppercase
    letters = [char.upper() for char in ciphertext if char.isalpha()]
    return Counter(letters)

# Step 3: Function to perform frequency analysis and decrypt
def frequency_analysis_caesar(ciphertext):
    # Get letter frequencies in the ciphertext
    frequencies = letter_frequency_analysis(ciphertext)
    
    # Sort letters in ciphertext by frequency
    sorted_letters = [letter for letter, _ in frequencies.most_common()]
    
    # Compare with expected English frequency and try shifts
    print("Trying frequency analysis...\n")
    for guess, most_common_letter in enumerate(sorted_letters[:5]):  # Try top 5 frequent letters
        # Assume the most frequent letter maps to 'E' (most common letter in English)
        shift_guess = (ord(most_common_letter) - ord('E')) % 26
        decrypted_text = caesar_decrypt(ciphertext, shift_guess)
        print(f"Shift Guess {guess + 1}: Assuming '{most_common_letter}' maps to 'E' → Decrypted: {decrypted_text}")

# Main function to run the process
if __name__ == "__main__":
    # Input ciphertext
    ciphertext = input("Enter the ciphertext: ").strip()
    
    # Perform frequency analysis
    frequency_analysis_caesar(ciphertext)
