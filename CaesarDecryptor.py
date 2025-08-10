from wordfreq import zipf_frequency

def real_word_checker(word):
    return zipf_frequency(word.lower(), 'en') > 0
        
def caesar_decrypt(ciphertext, shift):
    decrypted = ""
    shift = shift % 26  

    for char in ciphertext:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += char
    print(real_word_checker(decrypted)) 
    return decrypted


def read_file(file_name):
    lines_as_words = []  

    with open(file_name, "r") as file:
        for line in file:
            words = line.strip().split()  
            lines_as_words.append(words) 

    return lines_as_words

        


encrypted_string = "dbo"
print(caesar_decrypt(encrypted_string, 2))


#result = read_file("CipherText.txt")
#print(result)






