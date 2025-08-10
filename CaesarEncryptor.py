def caesar_decrypt(ciphertext, shift):
    decrypted = ""
    shift = shift % 26  # normalize shift to 0–25

    for char in ciphertext:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            # subtract shift for decryption
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += char  # keep non-letters as-is
    return decrypted

encrypted_string = "dbo"
print(caesar_decrypt(encrypted_string, 1))   # -> "can"
print(caesar_decrypt(encrypted_string, 52))  # -> "dbo"
