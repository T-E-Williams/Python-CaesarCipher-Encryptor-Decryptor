
def caesar_decrypt (ciphertext, shift):

    decrypted = ""
    
    for char in ciphertext:
        
        decrypted += chr(96+((ord(char)-shift)%26))

    print(decrypted)
    
encrypted_string = "dbo"

caesar_decrypt(encrypted_string, -1)