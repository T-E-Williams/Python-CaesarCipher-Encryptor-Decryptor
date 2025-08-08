
def caesar_decrypt (ciphertext, shift):

    decrypted = ""
    
    for char in ciphertext:

        decrypted += chr(ord(char)-shift)


    print(decrypted)
    


encrypted_string = "dbo"

caesar_decrypt(encrypted_string, 3)