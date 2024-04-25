def encrypt(key, plaintext):
    # Define the alphabet that we will use as the basis for our encryption
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # Initialize the result string
    result = ''

    # Iterate over each character in the plaintext
    for char in plaintext.upper():
        # If the character is in our defined alphabet
        if char in alphabet:
            # Find the current index of the character
            old_index = alphabet.index(char)
            # Calculate the new index by adding the key and taking the modulus by the length of the alphabet
            new_index = (old_index + key) % len(alphabet)
            # Add the character at the new index to our result string
            result += alphabet[new_index]
        else:
            # If the character is not in our alphabet (like a space or punctuation), just add it to the result as is
            result += char

    # Return the encrypted string
    return result

def decrypt(key, ciphertext):
    # To decrypt, we simply encrypt with the negative of the key
    return encrypt(-key, ciphertext)
