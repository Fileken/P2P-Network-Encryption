import socket
import encryption  # Импортируем модуль для шифрования и дешифрования сообщений

# Создаем сокет клиента
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 12345)

while True:
    message = input("Введите сообщение: ")

    # Шифруем сообщение с использованием шифра Цезаря перед отправкой
    encrypted_message = encryption.encrypt_message(message, encryption.caesar_cipher, shift=3)  # Используем сдвиг 3 как пример
    client.send(encrypted_message.encode())

client.close()
