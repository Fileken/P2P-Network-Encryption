# client.py

import socket
import threading

def receive_messages(s):
    while True:
        received = s.recv(1024).decode('utf-8')
        if not received:
            break
        print(received)

def send_messages(s):
    while True:
        user_input = input("$: ")
        if user_input.strip() == 'exit':
            s.sendall(user_input.encode('utf-8'))
            break
        elif user_input.strip():
            s.sendall(user_input.encode('utf-8'))

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect(('127.0.0.0', 8888))

    receive_thread = threading.Thread(target=receive_messages, args=(s,))
    send_thread = threading.Thread(target=send_messages, args=(s,))

    receive_thread.start()
    send_thread.start()

    receive_thread.join()
    send_thread.join()

    s.close()
