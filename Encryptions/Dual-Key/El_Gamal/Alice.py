from El_Gamal import El_Gamal_Class
import socket
import random

Server_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Host = '127.0.0.1'
Port = 12345
Server_Socket.bind((Host, Port))
Server_Socket.listen()
print(f"Server listening on {Host}:{Port}")
Client_Socket, Client_Address = Server_Socket.accept()
print(f"Connection established from {Client_Address}")

Message_Text = "Hello"

# Message_Integer = int.from_bytes(Message_Text.encode(), byteorder='big')
Message_Integer = 17
print(f"M value: {Message_Integer}")

Q = Client_Socket.recv(1024).decode('utf-8')
Q = int(Q)
print(f"Recieved Q: {Q}")
Response = f"Q Recieved: {Q}"
Client_Socket.send(Response.encode('utf-8'))
print(f"Response sent")

A = int(Client_Socket.recv(1024).decode('utf-8'))
A = int(A)
print(f"Recieved A: {A}")
Response = f"A Recieved: {A}"
Client_Socket.send(Response.encode('utf-8'))
print(f"Response sent")

k = int(Client_Socket.recv(1024).decode('utf-8'))
k = int(k)
print(f"Recieved k: {k}")
Response = f"k Recieved: {k}"
Client_Socket.send(Response.encode('utf-8'))
print(f"Response sent")

Private_Key = random.randint(1, Q - 1)
Diffie_Hellman_Object = El_Gamal_Class(Q, A, k, Private_Key)

if Diffie_Hellman_Object.Problem == "No Problem":
    Other_User_Public_Key = Client_Socket.recv(1024).decode('utf-8')
    Other_User_Public_Key = int(Other_User_Public_Key)
    print(f"Other user public key: {Other_User_Public_Key}")

    K = Diffie_Hellman_Object.Generate_K_Key(Q, k, Other_User_Public_Key)
    print(f"K value: {K}")
    Cipher_1 = Diffie_Hellman_Object.Generate_Cipher_1(Q, A, k)
    print(f"Cipher_1: {Cipher_1}")
    Cipher_2 = Diffie_Hellman_Object.Generate_Cipher_2(Q, K, Message_Integer)
    print(f"Cipher_2: {Cipher_2}")

    Client_Socket.send(str(Cipher_1).encode('utf-8'))
    print(f"Cipher_1 sent: {Cipher_1}")
    Response = Client_Socket.recv(1024).decode('utf-8')
    print(Response)

    Client_Socket.send(str(Cipher_2).encode('utf-8'))
    print(f"Cipher_1 sent: {Cipher_2}")
    Response = Client_Socket.recv(1024).decode('utf-8')
    print(Response)
else:
    print(Diffie_Hellman_Object.Problem, Diffie_Hellman_Object.Details)