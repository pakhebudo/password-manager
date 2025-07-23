def enc(word, shift):
    encrypted_word = ""
    for char in word:
        if char.isupper():
            char = chr((( ord(char) - ord('A') + shift) % 26) + ord('A'))
            encrypted_word += char

        elif char.islower():
            char = chr((( ord(char) - ord('a') + shift) % 26) + ord('a'))
            encrypted_word += char

        else: 
            encrypted_word += char

    return encrypted_word

def dec(word, shift):
    decrypted_word = ""
    for char in word:
        if char.isupper():
            char = chr((( ord(char) - ord('A') - shift) % 26) + ord('A'))
            decrypted_word += char
        
        elif char.islower(): 
            char = chr((( ord(char) - ord('a') - shift) % 26) + ord('a'))
            decrypted_word += char

        else:
            decrypted_word += char

    return decrypted_word