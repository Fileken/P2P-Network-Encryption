# server.py

import socket
import threading
import signal
import sys

clients = {}

def handle_client(client_socket, addr):
    username = client_socket.recv(1024).decode('utf-8')
    clients[addr] = (client_socket, username)
    print(f"New connection from {addr} with username '{username}'. Total clients: {len(clients)}")

    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            broadcast(f"{username}: {message}")
    except Exception as e:
        print(f"Error handling client {addr}: {e}")
    finally:
        del clients[addr]
        client_socket.close()
        print(f"Connection from {addr} with username '{username}' closed. Total clients: {len(clients)}")

def broadcast(message):
    for client_socket, _ in clients.values():
        try:
            client_socket.sendall(message.encode('utf-8'))
        except:
            pass  # Handle any exceptions that might occur when sending to a client

def signal_handler(sig, frame):
    print("Shutting down server...")
    for client_socket, _ in clients.values():
        client_socket.close()
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.0', 8888))
    server.listen()

    print("Server listening on port 8888")

    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler.start()

if __name__ == '__main__':
    main()
