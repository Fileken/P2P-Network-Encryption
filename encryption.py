import random
from re import findall

def regular(text):
    return findall(r"[0-9]+", text)

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            result += char
    return result

def vinzher_cipher(text, key, mode):
    result = ""
    text=text.upper()
    key=key.upper()
    mode=mode.upper()
    key *= len(text) // len(key) + 1
    for index, symbol in enumerate(text):
        if mode == 'E':
            temp = ord(symbol) + ord(key[index])
        else:
            temp = ord(symbol) - ord(key[index])
        result += chr(temp % 26 + ord('A'))
    return result

def xor_cipher(text, mode):
    result = []
    keys=[]
    if mode == "E":
        for symbol in text:
            key=random.randint(0,25)
            keys.append(str(key))
            result.append(str(ord(symbol)^key))
        return '.'.join(result), '.'.join(keys)
    else:
        keys=input("Write the keys: ")
        for index, symbol in enumerate(regular(text)):
            result.append(chr(int(symbol) ^ int(regular(keys)[index])))
        return ''.join(result)

def encrypt_message(message, encryption_function, *args):
    
    if encryption_function==vinzher_cipher:
        args=list(args)
        args.append("E")
    if encryption_function==xor_cipher:
        args=list(args)
        args.append("E")
        
    return encryption_function(message, *args)

def decrypt_message(encrypted_message, decryption_function, *args):
    
    if decryption_function==caesar_cipher:
        args=list(args)
        args[0]=-args[0]
    if decryption_function==vinzher_cipher:
        args=list(args)
        args.append("D")
    if decryption_function==xor_cipher:
        args=list(args)
        args.append("D")
    return decryption_function(encrypted_message, *args)
