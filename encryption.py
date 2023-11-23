def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            result += char
    return result

def encrypt_message(message, encryption_function, *args):
    """
    Функция для шифрования сообщения с использованием заданной функции шифрования.

    :param message:                   Исходное сообщение, которое нужно зашифровать.
    :param encryption_function: Функция шифрования, которая будет применена к сообщению.
    :param *args:                         Дополнительные аргументы, передаваемые в функцию шифрования (например, ключи).
    :return:                                  Зашифрованное сообщение.
    """
    return encryption_function(message, *args)

def decrypt_message(encrypted_message, decryption_function, *args):
    """
    Функция для расшифровки сообщения с использованием заданной функции расшифрования.

    :param encrypted_message: Зашифрованное сообщение, которое нужно расшифровать.
    :param decryption_function: Функция расшифрования, которая будет применена к сообщению.
    :param *args:                         Дополнительные аргументы, передаваемые в функцию расшифрования (например, ключи).
    :return:                                  Расшифрованное сообщение.
    """
    return decryption_function(encrypted_message, *args)
