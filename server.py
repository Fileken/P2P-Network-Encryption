import socket
import encryption  # Импортируем модуль для шифрования и дешифрования сообщений

# Создаем сокет сервера
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 12345))
server.listen(1)

print("Сервер слушает на порту 12345")

# Принимаем подключение клиента
client, client_addr = server.accept()
print(f"Подключение от {client_addr}")

while True:
    data = client.recv(1024)
    if not data:
        break

    # Расшифровываем полученное сообщение с использованием шифра Цезаря
    decrypted_data = encryption.decrypt_message(data.decode(), encryption.caesar_cipher, shift=-3)  # Используем сдвиг -3 как пример
    print(f"Получено сообщение: {decrypted_data}")

client.close()
server.close()
