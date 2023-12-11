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
        if mode == 'e':
            temp = ord(symbol) + ord(key[index])
        else:
            temp = ord(symbol) - ord(key[index])
        result += chr(temp % 26 + ord('A'))
    return result



def encrypt_message(message, encryption_function, *args):
    return encryption_function(message, *args)

def decrypt_message(encrypted_message, decryption_function, *args):
    if decryption_function==caesar_cipher:
        args=list(args)
        args[0]=-args[0]
    return decryption_function(encrypted_message, *args)
