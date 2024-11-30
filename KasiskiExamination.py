from collections import Counter
import itertools

# Step 1: Find repeated patterns and distances
def find_repeated_patterns(ciphertext, min_pattern_length=3, min_occurrences=2):
    patterns = {}
    ciphertext_length = len(ciphertext)
    
    # all possible lengths of the key
    for length in range(min_pattern_length, ciphertext_length // 2):
        seen_patterns = {}

        # skip the last length of words
        # find patterns 
        for i in range(ciphertext_length - length):
            pattern = ciphertext[i:i + length]
            if pattern in seen_patterns:
                distance = i - seen_patterns[pattern]
                if pattern not in patterns:
                    patterns[pattern] = []
                # all the distances this pattern matches, for example it could be 2, 3
                patterns[pattern].append(distance)
            seen_patterns[pattern] = i
    
    # Filter patterns with fewer than the required occurrences
    patterns = {p: d for p, d in patterns.items() if len(d) >= min_occurrences}
    
    return patterns


# Step 2: Find the most likely key length
def find_key_length(distances):
    factors = []
    for distance in distances:
        for i in range(2, distance + 1):
            if distance % i == 0:
                factors.append(i)
    common_factors = Counter(factors)
    return [length for length, _ in common_factors.most_common(3)]  # Return top 3 likely lengths

# Step 3: Split ciphertext into key-length groups
def split_into_groups(ciphertext, key_length):
    groups = ['' for _ in range(key_length)]
    for i, char in enumerate(ciphertext):
        groups[i % key_length] += char
    return groups

# Step 4: Frequency analysis to find the key
def frequency_analysis(group):
    english_frequency = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
    letter_counts = Counter(group)
    most_common_letter, _ = letter_counts.most_common(1)[0]
    shifts = []
    
    for letter in english_frequency[:3]:  # Test top 3 most common letters in English
        shift = (ord(most_common_letter) - ord(letter)) % 26
        shifts.append(shift)
    return shifts

# Step 5: Decrypt using the key
def decrypt_vigenere(ciphertext, key):
    plaintext = ''
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            shift_base = 65 if char.isupper() else 97
            plaintext += chr((ord(char) - shift_base - shift) % 26 + shift_base)
            key_index = (key_index + 1) % len(key)
        else:
            plaintext += char
    return plaintext

# Main Function: Crack Vigenère Cipher
def kasiski_examination(ciphertext):
    # Find repeating patterns and distances
    patterns = find_repeated_patterns(ciphertext)
    distances = [dist for dists in patterns.values() for dist in dists]
    
    if not distances:
        print("No repeated patterns found. Ciphertext may be too short or unbreakable.")
        return
    
    # Determine the most likely key lengths
    likely_lengths = find_key_length(distances)
    print(f"Likely key lengths: {likely_lengths}")
    
    # Try each likely key length
    for key_length in likely_lengths:
        print(f"\nTesting key length: {key_length}")
        
        # Split ciphertext into groups based on the key length
        groups = split_into_groups(ciphertext, key_length)
        
        # Perform frequency analysis on each group
        possible_keys = []
        for group in groups:
            shifts = frequency_analysis(group)
            possible_keys.append(shifts)
        
        # Generate all possible key combinations
        key_combinations = itertools.product(*possible_keys)
        
        for key_comb in key_combinations:
            key = ''.join(chr(shift + ord('A')) for shift in key_comb)
            plaintext = decrypt_vigenere(ciphertext, key)
            
            # Check if plaintext contains common English words
            if "the" in plaintext.lower() or "and" in plaintext.lower():
                print(f"Possible key: {key}")
                print(f"Decrypted text: {plaintext}")
                return

if __name__ == "__main__":
    ciphertext = "RIJVSUYVJNRIJVSUYVJN"  # Example ciphertext
    kasiski_examination(ciphertext)
