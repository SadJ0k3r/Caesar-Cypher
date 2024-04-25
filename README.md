# Caesar Cipher

The **Caesar Cipher** is a simple encryption technique that shifts each letter in a message by a fixed number of positions down the alphabet. It's named after Julius Caesar, who allegedly used it to communicate secretly.

## How It Works

1. **Alphabet Definition**:
   - We define an alphabet containing uppercase and lowercase letters: `ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`.

2. **Encryption (Shift Right)**:
   - To encrypt a message, we shift each letter by a specified key value to the right (positive shift).
   - Non-alphabetic characters (such as spaces or punctuation) remain unchanged.

3. **Decryption (Shift Left)**:
   - To decrypt a ciphertext, we shift each letter by the negative of the key value (leftward shift).

## Usage

1. **Encrypt**:
   - Call the `encrypt` function with a positive key value and the plaintext you want to encrypt.
   - Example: `encrypt(3, "HELLO")` results in `"KHOOR"`.

2. **Decrypt**:
   - Call the `decrypt` function with the negative of the key value and the ciphertext you want to decrypt.
   - Example: `decrypt(3, "KHOOR")` results in `"HELLO"`.

## Example

```python
# Encrypt
encrypted_text = encrypt(5, "SECRET MESSAGE")
print("Encrypted:", encrypted_text)  # Output: "XJHWJY RJXXFLJ"

# Decrypt
decrypted_text = decrypt(5, encrypted_text)
print("Decrypted:", decrypted_text)  # Output: "SECRET MESSAGE"
```

Feel free to experiment with different keys and messages! 🗝️🔒
