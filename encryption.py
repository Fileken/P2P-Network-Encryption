import random
from re import findall

# Function to find all numeric sequences in a given text
def regular(text):
    return findall(r"[0-9]+", text)

# Function for Caesar Cipher encryption or decryption
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            # Encrypt or decrypt based on the Caesar Cipher algorithm
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            result += char
    return result

# Function for a custom cipher, either encryption or decryption
def custom_cipher(text, mode):
    result = ""
    for char in text:
        if mode == "E":
            if char.isalpha():
                shift_amount = 65 if char.isupper() else 97
                shift=random.randint(0,25)
                # Encrypt based on a random shift value
                for char in text:
                    result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            if char.isalpha():
                shift=int(input("Write the shift: "))
                shift_amount = 65 if char.isupper() else 97
                # Decrypt based on the user-provided shift value
                for char in text:
                    result += chr((ord(char) - shift_amount - shift) % 26 + shift_amount)
        return result, shift

# Function for an A-Z cipher, either encryption or decryption
def az_cipher(text, mode):
    result = ""
    alpha=tuple("abcdefghijklmnopqrstuvwxyz")
    if mode == "E":
        # Encrypt by converting characters to their position in the alphabet
        for char in text:
            result += "%hu "%(alpha.index(char)+1)
    else:
        # Decrypt by converting numeric sequences to corresponding alphabet characters
        for number in regular(text):
            result += "%c"%alpha[int(number)-1]
    return result

# Function for a replace cipher, either encryption or decryption
def replace_cipher(text, mode):
    result=""
    text.upper()
    symbolsAlpha = [chr(x) for x in range(65,91)]
    symbolsCrypt = ('!','@','#','$','%','^','&','*','(',')','-','=','+','?',':',';','<','>','/','[',']','{','}','|','.',',','~')
    keys = dict(zip(symbolsAlpha,symbolsCrypt))
    if mode == "E":
        # Encrypt by replacing characters with predefined symbols
        for char in text:
            if char in keys: result += keys[char]
    else:
        # Decrypt by finding the original character for each symbol
        for char in text:
            for key in keys:
                if char == keys[key]: result+=key
    return result

# Function for Vigenere cipher encryption or decryption
def vinzher_cipher(text, key, mode):
    result = ""
    text=text.upper()
    key=key.upper()
    mode=mode.upper()
    key *= len(text) // len(key) + 1
    for index, symbol in enumerate(text):
        if mode == 'E':
            # Encrypt based on the Vigenere Cipher algorithm
            temp = ord(symbol) + ord(key[index])
        else:
            # Decrypt based on the Vigenere Cipher algorithm
            temp = ord(symbol) - ord(key[index])
        result += chr(temp % 26 + ord('A'))
    return result

# Function for XOR cipher encryption or decryption
def xor_cipher(text, mode):
    result = []
    keys=[]
    if mode == "E":
        # Encrypt using XOR with a randomly generated key
        for symbol in text:
            key=random.randint(0,25)
            keys.append(str(key))
            result.append(str(ord(symbol)^key))
        return '.'.join(result), '.'.join(keys)
    else:
        # Decrypt using XOR with user-provided keys
        keys=input("Write the keys: ")
        for index, symbol in enumerate(regular(text)):
            result.append(chr(int(symbol) ^ int(regular(keys)[index])))
        return ''.join(result)

# Function to encrypt a message using a specified encryption function
def encrypt_message(message, encryption_function, *args):
    # Adjusting arguments based on the encryption function
    
    if encryption_function==vinzher_cipher:
        args=list(args)
        args.append("E")

    if encryption_function==custom_cipher:
        args=list(args)
        args.append("E")
        
    if encryption_function==xor_cipher:
        args=list(args)
        args.append("E")
        
    if encryption_function==az_cipher:
        args=list(args)
        args.append("E")
        
    if encryption_function==replace_cipher:
        args=list(args)
        args.append("E") 
    
        
    return encryption_function(message, *args)
    
# Function to decrypt a message using a specified decryption function
def decrypt_message(encrypted_message, decryption_function, *args):
    # Adjusting arguments based on the decryption function
    
    if decryption_function==caesar_cipher:
        args=list(args)
        args[0]=-args[0]
        
    if decryption_function==custom_cipher:
        args=list(args)
        args.append("D")
        
    if decryption_function==vinzher_cipher:
        args=list(args)
        args.append("D")
        
    if decryption_function==xor_cipher:
        args=list(args)
        args.append("D")
        
    if decryption_function==az_cipher:
        args=list(args)
        args.append("D")
        
    if decryption_function==replace_cipher:
        args=list(args)
        args.append("D")
        
        
    return decryption_function(encrypted_message, *args)
