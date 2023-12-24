from Diffie_Hellman import Diffie_Hellman_Class
import socket
import random
import ast

Server_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Host = '127.0.0.1'
Port = 12345
Server_Socket.bind((Host, Port))

Server_Socket.listen()

print(f"Server listening on {Host}:{Port}")

Client_Socket, Client_Address = Server_Socket.accept()
print(f"Connection established from {Client_Address}")

Q = Client_Socket.recv(1024).decode('utf-8')
Q = int(Q)
print(f"Recieved Q: {Q}")


Response = f"Q Recieved: {Q}"
Client_Socket.send(Response.encode('utf-8'))
print(f"Response sent")

A = int(Client_Socket.recv(1024).decode('utf-8'))
A = int(A)
print(f"Recieved A: {A}")

Private_Key = random.randint(1, Q - 1)
Diffie_Hellman_Object = Diffie_Hellman_Class(Q, A, Private_Key)

if Diffie_Hellman_Object.Problem == "No Problem":
    Public_Key = Diffie_Hellman_Object.Generate_Public_Keys(Q, A, Private_Key)
    print(f"Public key: {Public_Key}")

    Other_User_Public_Key = Client_Socket.recv(1024).decode('utf-8')
    Other_User_Public_Key = int(Other_User_Public_Key)
    print(f" Other user public key: {Other_User_Public_Key}")

    Client_Socket.send(str(Public_Key).encode('utf-8'))
    print(f"Public key sent: {Public_Key}")

    Session_Key = Diffie_Hellman_Object.Generate_Session_Key(Q, Private_Key, Other_User_Public_Key)
    print(f"Session Key: {Session_Key}")

    Binary_Key = Diffie_Hellman_Object.Convert_to_Binary(Session_Key)
    Expansion = Client_Socket.recv(1024).decode('utf-8')
    Expansion = ast.literal_eval(Expansion)
    Final_Key = Diffie_Hellman_Object.Expand(Binary_Key, Expansion)

    print(f"Final Key: {Final_Key}")
    print(f"Final Key Length: {len(str(Final_Key))}")

else:
    print(Diffie_Hellman_Object.Problem, Diffie_Hellman_Object.Details)