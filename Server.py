import socket
import threading

def handle_client(client_socket, other_client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Received from Client: {message}")
            other_client_socket.send(message.encode('utf-8'))
        except Exception as e:
            print(f"Error: {e}")
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 5000))
    server.listen(2)
    print("Server listening on port 5000")

    clients = []

    while len(clients) < 2:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        clients.append(client_socket)

    for i in range(2):
        other_client = clients[1 - i]
        client_handler = threading.Thread(target=handle_client, args=(clients[i], other_client))
        client_handler.start()

if __name__ == "__main__":
    start_server()
